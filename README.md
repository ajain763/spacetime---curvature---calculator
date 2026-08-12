# GR Curvature Calculator

A Python/SymPy implementation of symbolic curvature calculations for the Schwarzschild spacetime in General Relativity.

## Overview

This project computes several geometric quantities associated with the Schwarzschild metric using symbolic mathematics. The tensor operations are implemented explicitly using Python loops, SymPy, and NumPy rather than relying on a dedicated General Relativity package.

The project was developed as a computational implementation of tensor calculus in General Relativity.

## Calculations

Starting from the Schwarzschild metric, the program calculates:

- The inverse metric
- Christoffel symbols
- The Riemann curvature tensor
- The covariant Riemann tensor
- The contravariant Riemann tensor
- The Kretschmann scalar
- The Ricci tensor
- The Ricci scalar

## Schwarzschild Metric

The metric used is

$$
ds^2 =
-\left(1-\frac{2M}{r}\right)dt^2
+\left(1-\frac{2M}{r}\right)^{-1}dr^2
+r^2d\theta^2
+r^2\sin^2\theta\,d\phi^2.
$$

The coordinates are

$$
(t,r,\theta,\phi)
$$

with $M$ representing the mass parameter.

## Method

The calculation proceeds from the metric tensor $g_{\mu\nu}$ and its inverse.

The Christoffel symbols are calculated using

$$
\Gamma^\sigma_{\mu\nu}
=
\frac{1}{2}g^{\sigma\tau}
\left(
\partial_\mu g_{\tau\nu}
+
\partial_\nu g_{\tau\mu}
-
\partial_\tau g_{\mu\nu}
\right).
$$

The Riemann curvature tensor is then constructed from the Christoffel symbols:

$$
R^\mu_{\ \nu\rho\sigma}
=
\partial_\rho\Gamma^\mu_{\nu\sigma}
-
\partial_\sigma\Gamma^\mu_{\nu\rho}
+
\Gamma^\mu_{\lambda\rho}\Gamma^\lambda_{\nu\sigma}
-
\Gamma^\mu_{\lambda\sigma}\Gamma^\lambda_{\nu\rho}.
$$

The Ricci tensor and Ricci scalar are subsequently obtained by contraction.

The Kretschmann scalar is calculated from

$$
K = R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}.
$$

## Technologies

- **Python**
- **SymPy** – symbolic differentiation, matrices and algebraic simplification
- **NumPy** – tensor-array storage and numerical-style iteration

## Files

- `curvature_calculator.py` – Python implementation of the calculations
- `Symbolic_GR.ipynb` – Jupyter Notebook containing the symbolic calculation
- `requirements.txt` – Python dependencies

## Purpose

This project demonstrates the computational implementation of tensor calculus and symbolic mathematical methods using Python.

It combines a mathematical formulation of General Relativity with explicit algorithmic implementation of the underlying tensor operations.

## Requirements

Python 3.x

Install the required packages with:

```bash
pip install sympy numpy
