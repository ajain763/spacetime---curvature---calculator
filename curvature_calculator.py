#!/usr/bin/env python
# coding: utf-8

# In[82]:


import sympy as sp
import numpy as np
import math

# Define a metric tensor:
t, r, theta, phi, M = sp.symbols('t r theta phi M')
x,y = sp.symbols('x y')

g = sp.Matrix([[-(1-2*M/r), 0, 0, 0],
              [0, 1/(1-2*M/r), 0, 0],
              [0, 0, r**2, 0],
              [0, 0, 0, r**2 * sp.sin(theta)**2]])
g_inv = g.inv()

# Christoffel Symbols:
coords = [t,r, theta, phi]
gamma = np.zeros((4,4,4), dtype = object)
for sigma in range(4):
    for mu in range(4):
        for nu in range(4):
            for tau in range(4):
                gamma[sigma, mu, nu] += (1/2) * g_inv[sigma, tau] * (sp.diff(g[tau, nu], coords[mu]) + sp.diff(g[tau, mu], coords[nu]) - sp.diff(g[mu, nu], coords[tau]))


# Riemann Curvature Tensor:
Riem = np.zeros((4,4,4,4), dtype = object)
R_cov = np.zeros((4,4,4,4), dtype = object)
R_contra = np.zeros((4,4,4,4), dtype = object)
gammaprod = np.zeros((4,4,4,4), dtype = object)
Ricci = np.zeros((4,4), dtype = object)
for mu in range(4):
    for nu in range(4):
        for rho in range(4):
            for sigma in range(4):
                for lam in range(4):
                    gammaprod[mu, nu, rho, sigma] += gamma[mu, lam, rho] * gamma[lam, nu, sigma] - gamma[mu, lam, sigma] * gamma[lam, nu, rho]                  
for mu in range(4):
    for nu in range(4):
        for rho in range(4):
            for sigma in range(4):
                Riem[mu, nu, rho ,sigma] = sp.diff(gamma[mu, nu, sigma], coords[rho]) - sp.diff(gamma[mu, nu, rho], coords[sigma]) + gammaprod[mu, nu, rho, sigma]

for mu in range(4):
    for nu in range(4):
        for rho in range(4):
            for sigma in range(4):
                for alpha in range(4):
                    R_cov[mu, nu, rho, sigma] += g[mu, alpha] * Riem[alpha, nu, rho, sigma]

for mu in range(4):
    for nu in range(4):
        for rho in range(4):
            for sigma in range(4): 
                R_contra[mu, nu, rho, sigma] = sum(Riem[mu, alpha, beta, gamma] * g_inv[alpha, nu] * g_inv[beta, rho] * g_inv[gamma, sigma]
                                                     for alpha in range(4)
                                                     for beta in range(4)
                                                     for gamma in range(4)
                                                     )
# The Kretschmann scalar:                
Kretschmann = sum(R_cov[mu, nu, rho, sigma] * R_contra[mu, nu, rho, sigma]
       for mu in range(4)
       for nu in range(4)
       for rho in range(4)
       for sigma in range(4)
       )
K = Kretschmann.simplify() 

# Update loop for Ricci:
for mu in range(4):
    for nu in range(4):
        Ricci[mu, nu] = sum(Riem[alpha, mu, alpha, nu]
                           for alpha in range(4)
                           )
Ricci[3,3].simplify() 
R = sum(Ricci[mu, nu] * g_inv[mu, nu]
       for mu in range(4)
       for nu in range(4)
       )
R.simplify()

