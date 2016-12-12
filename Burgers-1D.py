# -*- coding: utf-8 -*-
"""
cfd-with-python

Burgers' Equation, 1-D

du/dt + u*du/dx = v * d^2u/dx^2

"""

import numpy as np
import sympy as sp
from sympy.utilities.lambdify import lambdify
from sympy import init_printing
init_printing(use_latex=True)
import matplotlib.pyplot as plt
# import math as m


# =============== Periodic Boundary Condtion
x, nu, t = sp.symbols('x nu t')
phi = (sp.exp(-(x - 4 * t)**2 / (4 * nu * (t + 1))) +
       sp.exp(-(x - 4 * t - 2 * np.pi)**2 / (4 * nu * (t + 1))))
print(phi)

phiprime = phi.diff(x)
# phiprime = (-(-8*t + 2*x)*m.exp(-(-4*t + x)**2/(4*nu*(t + 1)))/(4*nu*(t + 1)) -
#             (-8*t + 2*x - 12.5663706143592)*m.exp(-(-4*t + x - 6.28318530717959)**2/(4*nu*(t + 1)))/(4*nu*(t + 1)))

u = -2 * nu * (phiprime / phi) + 4
# u = (-2*nu*(-(-8*t + 2*x)*m.exp(-(-4*t + x)**2/(4*nu*(t + 1)))/(4*nu*(t + 1)) - (-8*t + 2*x - 12.5663706143592)*
#     m.exp(-(-4*t + x - 6.28318530717959)**2/(4*nu*(t + 1)))/(4*nu*(t + 1)))/(m.exp(-(-4*t + x - 6.28318530717959)**2
#     /(4*nu*(t + 1))) + m.exp(-(-4*t + x)**2/(4*nu*(t + 1)))) + 4)

ufunc = lambdify((t, x, nu), u)

###variable declarations
nx = 101
nt = 100
dx = 2 * np.pi / (nx - 1)
nu = .07 #viscosity
dt = dx * nu

x = np.linspace(0, 2 * np.pi, nx)
un = np.empty(nx)
t = 0

u = np.asarray([ufunc(t, x0, nu) for x0 in x])

plt.figure(figsize=(11, 7), dpi=100)
plt.plot(x, u, marker='o', lw=2)
plt.xlim([0, 2 * np.pi])
plt.ylim([0, 10]);
plt.show()

for n in range(nt):
    un = u.copy()
    for i in range(1, nx - 1):
        u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i - 1]) + nu * dt / dx ** 2 * (un[i + 1] - 2 * un[i] + un[i - 1])
    u[0] = un[0] - un[0] * dt / dx * (un[0] - un[-2]) + nu * dt / dx ** 2 * (un[1] - 2 * un[0] + un[-2])
    u[-1] = un[-1] - un[-1] * dt / dx * (un[-1] - un[-2]) + nu * dt / dx ** 2 * (un[0] - 2 * un[-1] + un[-2])

u_analytical = np.asarray([ufunc(nt * dt, xi, nu) for xi in x])

plt.figure(figsize=(11, 7), dpi=100)
plt.plot(x,u, marker='o', lw=2, label='Computational')
plt.plot(x, u_analytical, label='Analytical')
plt.xlim([0, 2 * np.pi])
plt.ylim([0, 10])
plt.legend()
plt.show()