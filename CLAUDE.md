# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Coursework for a graduate Time Series course (Series de tiempo) in the Maestría en Ciencia de Datos at UC Chile. It is **not a software product** — it is a personal study repository. The deliverables are Jupyter notebooks (analysis, forecasts) and Spanish-language study notes. There is no application to build, no test suite, and `src/` and `tests/` are empty scaffolding.

## Environment

Conda environment `time-series-py313` (Python 3.13), defined in `environment.yml`.

```bash
conda env create -f environment.yml     # first-time setup
conda activate time-series-py313
```

Core analysis stack (some libraries are imported in notebooks but not yet pinned in `environment.yml` — `statsmodels`, `scikit-learn`): `darts` (imported as `darts`, package `u8darts`), `statsmodels`, `scikit-learn`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `scipy`, `openpyxl`/`xlrd` for Excel I/O.

## Running / verifying notebooks

The kernel is not run automatically. To check a notebook executes end-to-end:

```bash
jupyter nbconvert --to notebook --execute notebooks/w7_lab03.ipynb --output /tmp/out.ipynb
```

The VS Code interpreter is pinned in `.vscode/settings.json` to the conda env — open the folder and select the `time-series-py313` kernel to run interactively.

## Repository layout & conventions

- `notebooks/` — the active working area. Files are prefixed by course week: `w{N}_<kind>...` where kind is `Lab`, `Tutorial_`, `Tarea_`, `Ayudantia`, or `ClaseAplicada`. This is where new work goes.
- `data/raw/` — source datasets, also **week-prefixed** (`w{N}_...`, e.g. `w7_lab03_ipc.xlsx`). `data/processed/` is for derived data. The path scheme (`raw` / `interim` / `processed` / `external`) is codified in `utils/paths.py`.
- `knowledge/` — ~40 numbered Spanish markdown study notes (`NN-topic.md`) tracking the course syllabus from naive models → decomposition → ACF/PACF → AR/MA/ARMA → ARIMA/SARIMA → prediction. These are the conceptual backbone; consult them for the theory behind a notebook.
- `B6 Series de tiempo/` — the **original, read-only course materials** (instructor tutorials, ayudantías, tests, and reference PDFs/textbooks). The `notebooks/` versions are the student's reworkings of these. Treat this folder as source reference, not a place to edit.
- `utils/paths.py` — centralized `pathlib` path constants (`PROJECT_ROOT`, `DATA_RAW_DIR`, etc.). `utils/` is a package (`utils/__init__.py`).

### Known inconsistency

`utils/paths.py` defines the intended path convention, but most notebooks load data with bare relative paths (e.g. `pd.read_excel('ipc.xlsx')`) rather than importing from `utils.paths`. When editing data-loading cells, prefer the `utils.paths` constants (`DATA_RAW_DIR / "..."`) so paths work regardless of the kernel's working directory.

## Working language

Study notes, notebook prose, and analysis commentary are in **Spanish** (course language). Code, identifiers, and comments follow the existing per-notebook style. Match the surrounding notebook when editing.
