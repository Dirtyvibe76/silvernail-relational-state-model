# Reproducibility protocol

1. Clone this repository and create the clean environment described in `ENVIRONMENT.md`.
2. Install the exact package set in `requirements-lock.txt`.
3. Run the recovered scripts in `scripts/`. The historical scripts declare output paths under `/mnt/data`; change only the output directory when reproducing elsewhere.
4. Compare regenerated CSV and JSON values with the committed files under `outputs/`.
5. Run `python submission/make_verified_figures.py` to regenerate the manuscript figures from the committed numerical outputs.
6. Record the Git commit used for the reproduction.

## Interpretation boundary

The repository supports finite-system numerical observations and the stated algebraic constructions. It does not establish a thermodynamic-limit Lieb–Robinson theorem, exact Lorentz invariance, or a microscopic derivation of general relativity.

## Submission snapshot

The manuscript cites the public repository and a fixed submission commit. Future work should be added after that snapshot rather than rewriting the evidence used by Paper 1.
