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
├── cl_repo/repo1/      # Core zero-forcing and spectral algorithms
├── py_codes/           # Python implementations
│   └── DS_NDS/         # DS/NDS property checking (NetworkX + SageMath)
├── sage-learning/      # SageMath scripts and Jupyter notebooks
├── geo_graphs/         # GeoGebra graph visualization tools
└── petersen.gml        # Petersen graph sample file
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
cd py_codes/DS_NDS/prop_check && python main.py

# Compute zero-forcing number
cd cl_repo/repo1 && python zero_forcing.py

# Compute skew minimum rank
cd cl_repo/repo1 && python min_rank.py

# Search for cospectral graph pairs
cd cl_repo/repo1 && python cospectral_zf.py
```
