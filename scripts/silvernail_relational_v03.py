#!/usr/bin/env python3
"""
Silvernail Relational State Model V0.3
Exact finite-system causal-locality / Lieb-Robinson diagnostic.

This model:
- constructs a local spin-1/2 Hamiltonian on a relational ring,
- evolves a local operator in the Heisenberg picture,
- measures commutator growth C_ij(t) = ||[O_i(t), O_j]||_2,
- extracts threshold arrival times by graph distance,
- estimates an operational information-cone velocity,
- tests exponential suppression outside the fitted cone.

This is an exact finite-dimensional calculation for a small system.
It does not prove a thermodynamic-limit Lieb-Robinson theorem.

Dependencies:
    numpy
    scipy
"""

from __future__ import annotations

import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
from scipy.linalg import eigh


@dataclass(frozen=True)
class Config:
    qubits: int = 6
    coupling_j: float = 1.0
    anisotropy_delta: float = 0.7
    transverse_field: float = 0.35
    time_max: float = 4.0
    time_steps: int = 101
    source_site: int = 0
    arrival_threshold: float = 0.08
    outside_cone_mu: float = 1.0
    output_dir: str = "/mnt/data/silvernail_v03_output"


I2 = np.eye(2, dtype=np.complex128)
X = np.array([[0, 1], [1, 0]], dtype=np.complex128)
Y = np.array([[0, -1j], [1j, 0]], dtype=np.complex128)
Z = np.array([[1, 0], [0, -1]], dtype=np.complex128)


def kron_all(ops):
    out = ops[0]
    for op in ops[1:]:
        out = np.kron(out, op)
    return out


def local_operator(op, site: int, n: int):
    ops = [I2] * n
    ops = list(ops)
    ops[site] = op
    return kron_all(ops)


def two_site_operator(op_a, i: int, op_b, j: int, n: int):
    ops = [I2] * n
    ops = list(ops)
    ops[i] = op_a
    ops[j] = op_b
    return kron_all(ops)


def ring_distance(i: int, j: int, n: int) -> int:
    d = abs(i - j)
    return min(d, n - d)


def build_hamiltonian(cfg: Config):
    n = cfg.qubits
    dim = 2 ** n
    h = np.zeros((dim, dim), dtype=np.complex128)

    for i in range(n):
        j = (i + 1) % n
        h += cfg.coupling_j * (
            two_site_operator(X, i, X, j, n)
            + two_site_operator(Y, i, Y, j, n)
            + cfg.anisotropy_delta * two_site_operator(Z, i, Z, j, n)
        )

    for i in range(n):
        h += cfg.transverse_field * local_operator(X, i, n)

    if not np.allclose(h, h.conj().T, atol=1e-12):
        raise RuntimeError("Hamiltonian is not Hermitian")

    return h


def spectral_norm(matrix):
    return float(np.linalg.norm(matrix, ord=2))


def heisenberg_operator_from_eigendecomposition(eigenvalues, eigenvectors, operator, time_value: float):
    o_e = eigenvectors.conj().T @ operator @ eigenvectors
    phase = np.exp(1j * (eigenvalues[:, None] - eigenvalues[None, :]) * time_value)
    return eigenvectors @ (phase * o_e) @ eigenvectors.conj().T


def first_threshold_crossing(times, values, threshold):
    above = np.where(values >= threshold)[0]
    if len(above) == 0:
        return None
    idx = int(above[0])
    if idx == 0:
        return float(times[0])
    t0, t1 = times[idx - 1], times[idx]
    y0, y1 = values[idx - 1], values[idx]
    if y1 == y0:
        return float(t1)
    frac = (threshold - y0) / (y1 - y0)
    return float(t0 + frac * (t1 - t0))


def main():
    import shutil
    cfg = Config()
    if cfg.qubits < 4:
        raise ValueError("Use at least four qubits")
    if not (0 < cfg.arrival_threshold < 2):
        raise ValueError("arrival_threshold must lie between 0 and 2")

    out = Path(cfg.output_dir)
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True, exist_ok=True)

    h = build_hamiltonian(cfg)
    evals, evecs = eigh(h)
    n = cfg.qubits
    source = cfg.source_site
    source_op = local_operator(Z, source, n)
    target_ops = [local_operator(Z, j, n) for j in range(n)]
    distances = np.array([ring_distance(source, j, n) for j in range(n)], dtype=int)
    times = np.linspace(0.0, cfg.time_max, cfg.time_steps)
    commutators = np.zeros((len(times), n), dtype=float)

    for ti, t in enumerate(times):
        o_t = heisenberg_operator_from_eigendecomposition(evals, evecs, source_op, float(t))
        for j, target in enumerate(target_ops):
            comm = o_t @ target - target @ o_t
            commutators[ti, j] = spectral_norm(comm)

    unique_distances = sorted(set(int(d) for d in distances if d > 0))
    shell_curves, arrivals = {}, {}
    for d in unique_distances:
        sites = np.where(distances == d)[0]
        curve = np.max(commutators[:, sites], axis=1)
        shell_curves[d] = curve
        arrivals[d] = first_threshold_crossing(times, curve, cfg.arrival_threshold)

    valid = [(d, t) for d, t in arrivals.items() if t is not None and t > 0]
    if len(valid) >= 2:
        ds = np.array([x[0] for x in valid], dtype=float)
        ts = np.array([x[1] for x in valid], dtype=float)
        slope, intercept = np.polyfit(ds, ts, 1)
        velocity = float(1.0 / slope) if slope > 0 else None
    else:
        slope = intercept = velocity = None

    if velocity is not None:
        envelope_ratios, outside_samples = [], []
        for d in unique_distances:
            curve = shell_curves[d]
            for t, c in zip(times, curve):
                cone_coordinate = d - velocity * t
                ratio = c * np.exp(cfg.outside_cone_mu * cone_coordinate)
                envelope_ratios.append(float(ratio))
                if cone_coordinate > 0:
                    outside_samples.append((d, float(t), float(c), float(cone_coordinate), float(ratio)))
        empirical_A = max(envelope_ratios)
        outside_violations = sum(c > empirical_A * np.exp(-cfg.outside_cone_mu * xi) * (1 + 1e-10) for _, _, c, xi, _ in outside_samples)
    else:
        empirical_A = None
        outside_violations = None
        outside_samples = []

    arrival_sequence = [arrivals[d] for d in unique_distances if arrivals[d] is not None]
    monotonic_arrivals = all(arrival_sequence[i + 1] >= arrival_sequence[i] - 1e-9 for i in range(len(arrival_sequence) - 1))
    initial_nonlocal_commutator = float(np.max(commutators[0, distances > 0]))

    with (out / "commutator_growth.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["time"] + [f"site_{j}_distance_{distances[j]}" for j in range(n)])
        for ti, t in enumerate(times):
            writer.writerow([float(t)] + commutators[ti].tolist())

    with (out / "distance_shells.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["time"] + [f"distance_{d}" for d in unique_distances])
        for ti, t in enumerate(times):
            writer.writerow([float(t)] + [float(shell_curves[d][ti]) for d in unique_distances])

    with (out / "arrival_times.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["distance", "arrival_time", "threshold"])
        for d in unique_distances:
            writer.writerow([d, arrivals[d], cfg.arrival_threshold])

    summary = {
        "model": "Silvernail Relational State Model V0.3",
        "configuration": asdict(cfg),
        "hilbert_space_dimension": int(2 ** cfg.qubits),
        "hamiltonian": {"minimum_eigenvalue": float(evals.min()), "maximum_eigenvalue": float(evals.max()), "spectral_width": float(evals.max() - evals.min()), "hermiticity_error": float(np.linalg.norm(h - h.conj().T, ord=2))},
        "locality": {"initial_max_nonlocal_commutator": initial_nonlocal_commutator, "arrival_times_by_distance": {str(d): arrivals[d] for d in unique_distances}, "arrival_times_monotonic": bool(monotonic_arrivals), "arrival_fit_time_per_distance": None if slope is None else float(slope), "arrival_fit_intercept": None if intercept is None else float(intercept), "operational_cone_velocity": velocity},
        "empirical_exponential_envelope": {"mu": cfg.outside_cone_mu, "A": empirical_A, "form": "C(d,t) <= A exp[-mu(d-v*t)]", "outside_cone_samples": int(len(outside_samples)), "violations_against_fitted_covering_envelope": None if outside_violations is None else int(outside_violations)},
        "pass_conditions": {"equal_time_nonlocal_commutation": initial_nonlocal_commutator < 1e-10, "distance_ordered_arrivals": bool(monotonic_arrivals), "finite_positive_operational_velocity": velocity is not None and velocity > 0, "empirical_exponential_cover_exists": empirical_A is not None and outside_violations == 0},
        "limits": ["This is an exact finite ring, not an infinite-lattice theorem.", "The fitted velocity depends on operator choice and arrival threshold.", "The empirical envelope demonstrates compatibility with a cone, not a proof of the optimal Lieb-Robinson bound.", "The Hamiltonian is imposed; it has not yet emerged from a deeper selection principle.", "No Lorentz invariance is claimed."],
    }
    with (out / "summary.json").open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    print(json.dumps(summary, indent=2))
    print(f"\nOutputs written to: {out}")


if __name__ == "__main__":
    main()
