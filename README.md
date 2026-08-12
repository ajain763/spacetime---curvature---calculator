# GR Curvature Calculator

A Python/SymPy implementation of symbolic curvature calculations for the Schwarzschild spacetime in General Relativity.

## Overview

This project implements the calculation of several geometric quantities associated with the Schwarzschild metric using symbolic mathematics.

The tensor operations are explicitly implemented using Python, SymPy, and NumPy, starting from the metric tensor and building the relevant curvature quantities.

## Calculations

The program calculates:

* The inverse metric
* Christoffel symbols
* Riemann curvature tensor
* Covariant Riemann curvature tensor
* Contravariant Riemann curvature tensor
* Kretschmann scalar
* Ricci tensor
* Ricci scalar

## Schwarzschild Metric

The metric used in the calculation is

$$
ds^2 =
-\left(1-\frac{2M}{r}\right)dt^2
+
\left(1-\frac{2M}{r}\right)^{-1}dr^2
+
r^2d\theta^2
+
r^2\sin^2(\theta)d\phi^2
$$

The coordinates are

$$
(t,r,\theta,\phi)
$$

where $M$ is the mass parameter.

## Method

The calculation begins by defining the metric tensor $g_{\mu\nu}$ and obtaining its inverse $g^{\mu\nu}$.

The Christoffel symbols are calculated using

$$
\Gamma^\sigma_{\mu\nu}
======================

\frac{1}{2}g^{\sigma\tau}
\left(
\partial_\mu g_{\tau\nu}
+
\partial_\nu g_{\tau\mu}
------------------------

\partial_\tau g_{\mu\nu}
\right)
$$

The Riemann curvature tensor is then constructed from the Christoffel symbols:

$$
R^\mu_{\ \nu\rho\sigma}
=======================

## \partial_\rho\Gamma^\mu_{\nu\sigma}

\partial_\sigma\Gamma^\mu_{\nu\rho}
+
\Gamma^\mu_{\lambda\rho}\Gamma^\lambda_{\nu\sigma}
--------------------------------------------------

\Gamma^\mu_{\lambda\sigma}\Gamma^\lambda_{\nu\rho}
$$

The Kretschmann scalar is calculated by contracting the Riemann tensor:

$$
K =
R_{\mu\nu\rho\sigma}
R^{\mu\nu\rho\sigma}
$$

The Ricci tensor is obtained through contraction of the Riemann tensor, and the Ricci scalar is subsequently calculated by contracting the Ricci tensor with the inverse metric.

## Technologies

* **Python**
* **SymPy** – symbolic mathematics, differentiation, matrices, and algebraic simplification
* **NumPy** – tensor-array storage and iteration

## Files

* `curvature_calculator.py` – Python implementation of the symbolic curvature calculations
* `Symbolic_GR.ipynb` – Jupyter Notebook containing the symbolic calculation
* `README.md` – Project documentation
* `.gitignore` – Files and directories excluded from version control

## Requirements

Python 3.x

Install the required packages with:

```bash
pip install sympy numpy
```

## Running the Project

### Python script

Run the Python implementation with:

```bash
python curvature_calculator.py
```

### Jupyter Notebook

The notebook can be opened with:

```bash
jupyter notebook Symbolic_GR.ipynb
```

## Purpose

This project demonstrates the computational implementation of tensor calculus in General Relativity.

It combines mathematical formulation with explicit algorithmic implementation of tensor operations using Python and symbolic computation.

## Future Improvements

Possible extensions include:

* Allowing user-defined metric tensors as inputs
* Supporting additional spacetime metrics
* Automating tensor-index operations
* Adding additional curvature invariants
* Improving computational efficiency for symbolic calculations
