# -*- coding: utf-8 -*-
"""
cfd-with-python

1D Linear Convection
du/dt + c*du/dx = 0

"""

import numpy as np
import matplotlib.pyplot as plt

# ===========================Variable Declarations==============================

nx = 81             # number of grid points in x domain of  0 to 2
dx = 2 / (nx-1)     # distance between grid points in x domain
nt = 25             # nt is the number of timesteps to calculate
dt = 0.025          # dt is the amount of time each timestep covers (delta t)
c = 1               # assume wavespeed of c = 1
# if at time dt, the wave is travelling a distance which is greater than dx there will be numerical instability
# introduce the Courant number to insure stability. sigma = u*dt/dx <= sigmaMax
sigma = 1.0         # sigma = the Courant number
dt = sigma * dx     # dt is the amount of time each timestep covers (delta t)

x=np.linspace(0,2,nx)   # create array of x domain
u = np.ones(nx)         # create a (1 x n) vector of 1's

# ==========================Assign Initial Conditions===========================

# set hat function I.C. : u(.5<=x<=1) is 2
u[int(.5 / dx):int(1 / dx + 1)] = 2
# plt.plot( x, u,label='t=0')

# ================================Evaluate PDE==================================

for n in range(nt): # loop for values of n from 0 to nt, so it will run nt times
    un = u.copy()   #copy the existing values of u into un
    for i in range(1, nx):          # loop for of x from 0 to nx at current timestep
        u[i] = un[i] - c * dt / dx * (un[i] - un[i - 1])

# ================================Plot Results==================================

x=np.linspace(0,2,nx)
plt.plot( x, u,label='t=%0.3f' %(nt*dt))

plt.xlim(0,3)
plt.ylim(0,3)
plt.xlabel('Distance X')
plt.ylabel('Velocity U')
plt.legend()
plt.title('1D Linear Convection')
plt.show()
