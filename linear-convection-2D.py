# -*- coding: utf-8 -*-
"""
cfd-with-python

2D Linear Convection
du/dt + c*du/dx = 0

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# ===========================Variable Declarations==============================

nx = 81             # number of grid points in x domain of  0 to 2
ny = 81             # number of grid points in y domain of  0 to 2
dx = 2 / (nx-1)     # distance between grid points in x domain
dy = 2 / (ny-1)     # distance between grid points in y domain
nt = 100            # nt is the number of timesteps to calculate
dt = 0.01           # dt is the amount of time each timestep covers (delta t)
c = 1               # assume wave speed of c = 1
# if at time dt, the wave is travelling a distance which is greater than dx there will be numerical instability
# introduce the Courant number to insure stability. sigma = u*dt/dx + v*dt/dy <= sigmaMax
uMax = 2            # Max velocity
sigma = uMax*dt/dx + 0*dt/dy
print(sigma)        # keep Courant number under 1.0 for stability in current sim

x=np.linspace(0,2,nx)   # create array of x domain
y=np.linspace(0,2,ny)   # create array of y domain

u = np.ones((ny,nx))    # create a (n x n) array of 1's

# ==========================Assign Initial Conditions===========================

# set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
u[ int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2

# Plot Initial Condition
# the figsize parameter can be used to produce different sized images
fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = np.meshgrid(x, y)
surf = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)
plt.show()

# ================================Evaluate PDE (using lists)====================

# u = np.ones((ny, nx))     ##create a (1 x n) vector of 1's
# ##set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
# u[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2
#
# for n in range(nt + 1): ##loop across number of time steps
#     un = u.copy()       ##copy the existing values of u into un
#     row, col = u.shape
#     for j in range(1, row):
#         for i in range(1, col):
#             u[j, i] = (un[j, i] - (c * dt / dx * (un[j, i] - un[j, i - 1])) -
#                                   (c * dt / dy * (un[j, i] - un[j - 1, i])))
#             u[0, :] = 1
#             u[-1, :] = 1
#             u[:, 0] = 1
#             u[:, -1] = 1
#
# fig = plt.figure(figsize=(11, 7), dpi=100)
# ax = fig.gca(projection='3d')
# surf2 = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)
# plt.show()

# ================================Evaluate PDE (using np arrays)================

for n in range(nt + 1): # loop across number of time steps
    un = u.copy()
    u[1:, 1:] = (un[1:, 1:] - (c * dt / dx * (un[1:, 1:] - un[1:, :-1])) -
                              (c * dt / dy * (un[1:, 1:] - un[:-1, 1:])))
    u[0, :] = 1
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1

# ================================Plot Results==================================

fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
surf2 = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)
ax.set_xlim3d(0, 2)
ax.set_ylim3d(0, 2)
ax.set_zlim3d(0, 2)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.title('2D Linear Convection')
plt.show()