# Silvernail Relational State Model — Paper 1 Reproducibility Repository

This public repository contains the recovered source scripts, regenerated numerical outputs, and verified manuscript figures supporting **Relational State Dynamics, Emergent Geometry, and Causal Propagation in the Silvernail Relational State Model**.

## Scope

The repository supports the bounded claims made in Paper 1:

- finite-system operator-commutator propagation;
- operational information-cone fits;
- state-responsive relational geometry;
- discrimination among simulation-start, emission-time, arrival-time, and history-averaged distances;
- the local Hermitian incidence-generator construction;
- infrared Dirac-type and Clifford-closure results.

It does **not** claim a complete microscopic derivation of general relativity, exact Lorentz invariance, or a thermodynamic-limit theorem.

## Repository structure

- `scripts/` — recovered Python simulations for V0.3, V0.4, V0.5, V0.6, V0.7, V0.9, and V0.10.
- `analytical/` — V0.71 and V0.72 analytical result records.
- `outputs/` — regenerated CSV and JSON outputs, grouped by model version.
- `figures/` — publication-oriented figures generated directly from the regenerated outputs.
- `requirements.txt` — minimal Python dependencies.
- `CITATION.cff` — citation metadata.
- `LICENSE` — software license.

## Reproduction

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run an individual version, for example:

```bash
python scripts/silvernail_relational_v09.py
```

The historical scripts write their outputs below `/mnt/data/`. To redirect them, edit the declared output directory near the top of each script before execution.

## Figure provenance

The figures in `figures/` were regenerated from the recovered scripts and their newly produced CSV outputs. They supersede earlier roadmap-only illustrations.

## Author

Aron Silvernail, Independent Researcher  
Contact: aronsilvernailj@gmail.com

## Manuscript status

Research manuscript draft. Numerical and analytical claims remain subject to peer review and independent replication.
