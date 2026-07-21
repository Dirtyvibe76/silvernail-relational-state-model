#!/usr/bin/env python3
"""Generate the verified Paper 1 figures from regenerated SRSM outputs."""

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
FIGURES = ROOT / "figures"
FIGURES.mkdir(parents=True, exist_ok=True)

# V0.3 — exact commutator growth
v03 = pd.read_csv(OUTPUTS / "v03" / "commutator_growth.csv")
fig, ax = plt.subplots(figsize=(7.2, 4.8))
for col in [c for c in v03.columns if c != "time"]:
    ax.plot(v03["time"], v03[col], label=col.replace("_", " "))
ax.axhline(0.08, linestyle="--", linewidth=1, label="arrival threshold")
ax.set_xlabel("Time")
ax.set_ylabel(r"$\|[A_0(t),B_j]\|_2$")
ax.set_title("V0.3 exact commutator growth on the six-site ring")
ax.legend(ncol=2, fontsize=8)
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(FIGURES / "figure_v03_commutator_growth.svg")
plt.close(fig)

# V0.4 — velocity scaling
v04 = pd.read_csv(OUTPUTS / "v04" / "sweep_results.csv")
j_col = next(c for c in v04.columns if c.lower() in {"j", "coupling_j", "coupling"})
v_col = next(c for c in v04.columns if "velocity" in c.lower() and "over" not in c.lower())
fig, ax = plt.subplots(figsize=(7.2, 4.8))
if "topology" in v04.columns:
    for name, sub in v04.groupby("topology"):
        ax.scatter(sub[j_col], sub[v_col], label=str(name))
else:
    ax.scatter(v04[j_col], v04[v_col])
x = v04[j_col].to_numpy(float)
y = v04[v_col].to_numpy(float)
slope = float(np.dot(x, y) / np.dot(x, x))
xx = np.linspace(x.min(), x.max(), 100)
ax.plot(xx, slope * xx, linestyle="--", label=f"through-origin fit: v={slope:.3g}J")
ax.set_xlabel("Local interaction strength J")
ax.set_ylabel("Operational cone velocity")
ax.set_title("V0.4 operational velocity scales with local coupling")
ax.legend(fontsize=8)
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(FIGURES / "figure_v04_velocity_scaling.svg")
plt.close(fig)

# V0.7 — metric-history discrimination
v07 = pd.read_csv(OUTPUTS / "v07" / "dynamic_arrival_metric_analysis.csv")
fig, ax = plt.subplots(figsize=(7.2, 4.8))
for metric in ["initial_distance", "distance_at_arrival", "time_averaged_distance"]:
    ax.scatter(v07[metric], v07["arrival_time"], label=metric.replace("_", " "))
    coef = np.polyfit(v07[metric], v07["arrival_time"], 1)
    xx = np.linspace(v07[metric].min(), v07[metric].max(), 100)
    ax.plot(xx, np.polyval(coef, xx), linestyle="--")
ax.set_xlabel("Candidate relational distance")
ax.set_ylabel("Threshold arrival time")
ax.set_title("V0.7 discrimination among causal-distance histories")
ax.legend(fontsize=8)
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(FIGURES / "figure_v07_metric_discrimination.svg")
plt.close(fig)

# V0.9 — delayed-injection comparison
v09 = pd.read_csv(OUTPUTS / "v09" / "dynamic_metric_analysis.csv")
fig, ax = plt.subplots(figsize=(7.2, 4.8))
for metric in ["simulation_start_distance", "emission_distance"]:
    ax.scatter(v09[metric], v09["arrival_time"], label=metric.replace("_", " "))
    coef = np.polyfit(v09[metric], v09["arrival_time"], 1)
    xx = np.linspace(v09[metric].min(), v09[metric].max(), 100)
    ax.plot(xx, np.polyval(coef, xx), linestyle="--")
ax.set_xlabel("Relational distance")
ax.set_ylabel("Threshold arrival time")
ax.set_title("V0.9 delayed-injection test: emission geometry is more predictive")
ax.legend(fontsize=8)
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(FIGURES / "figure_v09_emission_metric.svg")
plt.close(fig)

# V0.10 — AIC sweep
v10 = pd.read_csv(OUTPUTS / "v10" / "sweep_results.csv")
fig, ax = plt.subplots(figsize=(7.2, 4.8))
for col, label in [
    ("start_aic", "simulation-start"),
    ("emission_aic", "emission-time"),
    ("arrival_aic", "arrival-time"),
    ("average_aic", "time-averaged"),
]:
    ax.plot(v10["pre_steps"], v10[col], marker="o", label=label)
ax.set_xlabel("Pre-injection evolution steps")
ax.set_ylabel("AIC (lower is better)")
ax.set_title("V0.10 causal-metric preference across injection times")
ax.legend(fontsize=8)
ax.grid(alpha=0.25)
fig.tight_layout()
fig.savefig(FIGURES / "figure_v10_aic_sweep.svg")
plt.close(fig)

print(f"Figures written to {FIGURES}")
