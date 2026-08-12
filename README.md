# GR Curvature Calculator

A Python/SymPy implementation of symbolic curvature calculations for the Schwarzschild spacetime in General Relativity.

## Overview

This project implements the calculation of several geometric quantities associated with the Schwarzschild metric using symbolic mathematics.

The tensor operations are explicitly implemented using Python, SymPy, and NumPy, starting from the metric tensor and building the relevant curvature quantities.

## Calculations

The program calculates:

- The inverse metric
- Christoffel symbols
- Riemann curvature tensor
- Covariant Riemann curvature tensor
- Contravariant Riemann curvature tensor
- Kretschmann scalar
- Ricci tensor
- Ricci scalar

## Schwarzschild Metric

The metric used is the Schwarzschild metric in spherical coordinates:

`(t, r, θ, φ)`

with mass parameter `M`.

The metric components are implemented directly in the Python code.

## Method

The calculation begins by defining the metric tensor `g` and obtaining its inverse `g⁻¹`.

The Christoffel symbols are calculated from the metric and its derivatives using the standard definition:

`Γᵅ_ᵦᵧ = ½ gᵅᵟ (∂ᵦgᵟᵧ + ∂ᵧgᵟᵦ − ∂ᵟgᵦᵧ)`

The Riemann curvature tensor is then constructed from the Christoffel symbols and their derivatives.

The covariant Riemann tensor is obtained by lowering the first index of the Riemann tensor with the metric, while the contravariant Riemann tensor is obtained by raising the remaining three indices with the inverse metric.

The Kretschmann scalar is calculated through the full contraction:

`K = R<sub>μνρσ</sub> R<sup>μνρσ</sup>`

where `Rᵤᵥᵨₛ` is the fully covariant Riemann tensor and `Rᵘᵛᵨₛ` is the fully contravariant Riemann tensor.

The Ricci tensor is subsequently calculated by contraction of the Riemann tensor, followed by calculation of the Ricci scalar through contraction with the inverse metric.

## Technologies

- Python
- SymPy – symbolic mathematics, differentiation, matrices, and algebraic simplification
- NumPy – tensor-array storage and iteration

## Files

- `curvature_calculator.py` – Python implementation of the symbolic curvature calculations
- `Symbolic_GR.ipynb` – Jupyter Notebook containing the symbolic calculation
- `README.md` – Project documentation
- `.gitignore` – Files excluded from version control

## Requirements

Python 3.x

Install the required packages with:

```bash
pip install sympy numpy
