# -*- coding: utf-8 -*-
"""
cfd-with-python

2D Convection
dv/dt + u*dv/dx + v*dv/dy = 0

Discretize forward in time, backward in space
u_(i,j)^(n+1) - u_(i,j)^n               u_(i,j)^n - u_((i-1,j))^n               u_(i,j)^n - u_((i,j-1))^n
------------------------- + u_(i,j)^n * ------------------------- + v_(i,j)^n * -------------------------  =  0
            dt                                      dx                                      dy

solve for: u_i^(n+1)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import time, sys

# =====================Variable Declarations==============================

nx = 101
ny = 101
dx = 2 / (nx - 1)
dy = 2 / (ny - 1)
nt = 80
dt = 0.005
c = 1
# if at time dt, the wave is travelling a distance which is greater than dx there will be numerical instability
# introduce the Courant number to insure stability. sigma = u*dt/dx + v*dt/dy <= sigmaMax
uMax = 2            # Max velocity
sigma = uMax*dt/dx + 0*dt/dy
print(sigma)        # keep Courant number under 1.0 for stability in current sim

x = np.linspace(0, 2, nx)
y = np.linspace(0, 2, ny)
u = np.ones((ny, nx))
v = np.ones((ny, nx))

# ====================Assign Initial Conditions===========================
##set hat function I.C. : u(.5<=x<=1 && .5<=y<=1 ) is 2
u[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2
##set hat function I.C. : v(.5<=x<=1 && .5<=y<=1 ) is 2
v[int(.5 / dy):int(1 / dy + 1), int(.5 / dx):int(1 / dx + 1)] = 2

###Plot Initial Condition
fig = plt.figure(figsize=(11, 7), dpi=100)
ax = fig.gca(projection='3d')
X, Y = np.meshgrid(x, y)
ax.plot_surface(X, Y, u, cmap=cm.viridis, rstride=2, cstride=2)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
# plt.show()

# ================================Evaluate PDE==================================

p = plt.imshow(u)  ###for slide show of each iteration
fig = plt.gcf()
for n in range(nt + 1):  ##loop across number of time steps
    un = u.copy()
    vn = v.copy()
    u[1:, 1:] = (un[1:, 1:] -
                 (un[1:, 1:] * c * dt / dx * (un[1:, 1:] - un[1:, :-1])) -
                 vn[1:, 1:] * c * dt / dy * (un[1:, 1:] - un[:-1, 1:]))
    v[1:, 1:] = (vn[1:, 1:] -
                 (un[1:, 1:] * c * dt / dx * (vn[1:, 1:] - vn[1:, :-1])) -
                 vn[1:, 1:] * c * dt / dy * (vn[1:, 1:] - vn[:-1, 1:]))
    # Apply boundary condition of u=1 & v=1 at{x=0,2 & y=0,2}
    u[ 0, :] = 1
    u[-1, :] = 1
    u[ :, 0] = 1
    u[ :,-1] = 1

    v[ 0, :] = 1
    v[-1, :] = 1
    v[ :, 0] = 1
    v[ :,-1] = 1

    p.set_data(u)
    plt.pause(0.1)

# ================================Plot Results==================================

# fig = plt.figure(figsize=(11, 7), dpi=100)
# ax = fig.gca(projection='3d')
# X, Y = np.meshgrid(x, y)
# ax.plot_surface(X, Y, u, cmap=cm.viridis, rstride=2, cstride=2)
# ax.set_xlabel('$x$')
# ax.set_ylabel('$y$');
# X, Y = np.meshgrid(x, y)
# plt.contour(X,Y,u)
# plt.title('2D Convection')
# plt.show()
