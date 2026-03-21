# Spectral Project

A research codebase for **Graph Spectral Theory**, focusing on the relationships between spectral properties, zero-forcing parameters, and the "Determined by Spectrum" (DS) property of graphs.

---

## Overview

This project explores several core topics in algebraic and spectral graph theory:

- **Zero Forcing** — A graph coloring propagation problem used to bound the minimum rank of a graph. Includes brute-force and wavefront algorithms, zero-forcing polynomials, propagation time, and throttling numbers (standard, PSD, and skew variants).
- **Minimum Rank** — Computation of the skew-symmetric minimum rank of a graph using symbolic algebra (Gröbner bases via SymPy).
- **Cospectral Graphs** — Algorithmic search for non-isomorphic graph pairs that share identical spectra, using the `nauty` graph generation tool.
- **DS Property** — A heuristic (Godsil-McKay switching) to test whether a graph is uniquely determined by its spectrum. Implemented in both NetworkX and SageMath.
- **Graph Utilities** — Tools for parsing `graph6`/`sparse6` formats, constructing Hamming graphs, and generating GeoGebra visualizations.

---

## Repository Structure

```
spectral-project/
├── data/                       # Graph data files
│   ├── g6/                     # graph6-format graph files (.g6)
│   ├── gml/                    # GML graph files (e.g. Petersen graph)
│   └── ggb/                    # GeoGebra graph files (.ggb)
│
├── notebooks/                  # Jupyter / SageMath notebooks
│   ├── learning/               # Tutorial & lecture notebooks (Lect-1 … Lect-3)
│   ├── research/               # Research & analysis notebooks
│   └── scratch/                # Exploratory / untitled notebooks
│
└── src/                        # Source code
    ├── ds_nds/                 # DS / NDS property analysis
    │   ├── find_cospectral.py  # Enumerate cospectral graph pairs
    │   ├── ds_heuristic.py     # Godsil-McKay DS heuristic (NetworkX)
    │   ├── graph_utils.py      # Graph construction utilities
    │   ├── main.py             # DS property check entry point
    │   ├── sage/               # SageMath DS scripts (.sage)
    │   └── sage_analyze/       # SageMath DS analysis utilities
    ├── spectral/               # Spectral graph utilities
    │   └── hm_graph.py         # Hamming graph construction
    ├── zero_forcing/           # Zero-forcing & minimum-rank algorithms
    │   ├── zero_forcing.py     # Zero-forcing number algorithms
    │   ├── min_rank.py         # Skew minimum rank (SymPy)
    │   ├── cospectral_zf.py    # Cospectral + zero-forcing search
    │   ├── reg_cospectral_zf.py
    │   └── nauty_geng_reader.py
    └── geo/                    # GeoGebra visualisation tools
        ├── decode_ggb.py
        └── ggb_graph.py
```

---

## Dependencies

- [NetworkX](https://networkx.org/) — graph construction, manipulation, isomorphism checking
- [NumPy](https://numpy.org/) — linear algebra, eigenvalue computation
- [SymPy](https://www.sympy.org/) — symbolic computation, Gröbner bases
- [SageMath](https://www.sagemath.org/) — advanced graph operations and Jupyter notebooks
- [Matplotlib](https://matplotlib.org/) — graph visualization
- [Nauty](https://pallini.di.uniroma1.it/) — graph generation and canonical forms

---

## Usage

```bash
# Check DS property of a graph
cd src/ds_nds && python main.py

# Compute zero-forcing number
cd src/zero_forcing && python zero_forcing.py

# Compute skew minimum rank
cd src/zero_forcing && python min_rank.py

# Search for cospectral graph pairs
cd src/zero_forcing && python cospectral_zf.py
```
