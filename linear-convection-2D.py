# -*- coding: utf-8 -*-
"""
cfd-with-python

linear convection
du/dt + c*du/dx = 0

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import time, sys  

# =====================Variable Declarations==============================
nx = 81
ny = 81
nt = 100    #nt is the number of timesteps we want to calculate
c = 1       #assume wavespeed of c = 1
dx = 2 / (nx-1)
dy = 2 / (ny-1)
# if at time dt, the wave is travelling a distance which is greater than dx there will be numerical instability
# introduce the Courant number to insure stability. sigma = u*dt/dx <= sigmaMax
sigma = .2 #sigma = the Courant number
dt = sigma * dx  #dt is the amount of time each timestep covers (delta t)

x=np.linspace(0,2,nx)
y=np.linspace(0,2,ny)

u = np.ones((ny,nx))     ##create a (1 x n) vector of 1's
un = np.ones((ny,nx))    ## initialize a temporary array

# ====================Assign Initial Conditions===========================
##set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
u[ int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2


###Plot Initial Condition
##the figsize parameter can be used to produce different sized images
fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = np.meshgrid(x, y)
surf = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)
plt.show()

# ========================Evaluate PDE==========================
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

# ========================Evaluate PDE(using arrays)==============
u = np.ones((ny, nx))
u[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2

for n in range(nt + 1): ##loop across number of time steps
    un = u.copy()
    u[1:, 1:] = (un[1:, 1:] - (c * dt / dx * (un[1:, 1:] - un[1:, :-1])) -
                              (c * dt / dy * (un[1:, 1:] - un[:-1, 1:])))
    u[0, :] = 1
    u[-1, :] = 1
    u[:, 0] = 1
    u[:, -1] = 1

fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
surf2 = ax.plot_surface(X, Y, u[:], cmap=cm.viridis)
plt.show()