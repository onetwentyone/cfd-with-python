# -*- coding: utf-8 -*-
"""
cfd-with-python

1-D Diffusion
~heat equation (if u = temperature)~
du/dt = v * d^2u/dx^2

Discretize forward in time, central in space 
u_i^(n+1) - u_i^n          u_(i+1)^n - 2u_i^n + u_(i-1)^n
-----------------  =  nu * ------------------------------
       dt                               dx^2

solve for: u_i^(n+1)
"""

import numpy as np
import matplotlib.pyplot as plt

# ===========================Variable Declarations==============================

nx = 41
dx = 2 / (nx - 1)
nt = 25             # the number of timesteps we want to calculate
nu = 0.3            # diffusion coefficient or the value of viscosity
sigma = .2          # Courant number
dt = sigma * dx ** 2 / nu   # dt is defined using sigma

u = np.ones(nx)     # a numpy array with nx elements all equal to 1.
un = np.ones(nx)    # our placeholder array, un, to advance the solution in time

# ==========================Assign Initial Conditions===========================

# set hat function I.C. : u(.5<=x<=1) is 2
u[int(.5 / dx):int(1 / dx + 1)] = 2  

# ================================Evaluate PDE==================================

for n in range(nt): # iterate through time
    un = u.copy()   # copy the existing values of u into un
    for i in range(1, nx - 1):
        u[i] = un[i] + nu * dt / dx ** 2 * (un[i + 1] - 2 * un[i] + un[i - 1])

# ================================Plot Results==================================

x = np.linspace(0, 2, nx)
plt.plot( x, u,label='t=%0.3f' %(nt*dt))

plt.xlim(0,2)
plt.ylim(0,2)
plt.xlabel('Distance X')
plt.ylabel('Velocity U')
plt.legend()
plt.title('1D Diffusion')
plt.show()
