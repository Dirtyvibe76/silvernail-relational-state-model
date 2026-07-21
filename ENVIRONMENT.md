# Computational environment

The submission verification bundle was prepared with Python 3.12 on Linux x86_64.

Exact Python package versions are recorded in `requirements-lock.txt`.

The recovered finite-model scripts use explicit deterministic initial states. No stochastic sampling is used in the reported Paper 1 runs unless a script states otherwise.

Recommended clean environment:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-lock.txt
```
