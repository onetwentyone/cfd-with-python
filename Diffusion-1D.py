# -*- coding: utf-8 -*-
"""
cfd-with-python

1-D Diffusion
~heat equation (if u = temperature)~
du/dt = v * d^2u/dx^2

"""

import numpy as np
import matplotlib.pyplot as plt

nx = 41
dx = 2 / (nx - 1)
nt = 20  # the number of timesteps we want to calculate
nu = 0.3  # the value of viscosity
sigma = .2  # sigma is a parameter, we'll learn more about it later
dt = sigma * dx ** 2 / nu  # dt is defined using sigma ... more later!

u = np.ones(nx)  # a numpy array with nx elements all equal to 1.
u[int(.5 / dx):int(1 / dx + 1)] = 2  # setting u = 2 between 0.5 and 1 as per our I.C.s

un = np.ones(nx)  # our placeholder array, un, to advance the solution in time

for n in range(nt):  # iterate through time
    un = u.copy()  ##copy the existing values of u into un
    for i in range(1, nx - 1):
        u[i] = un[i] + nu * dt / dx ** 2 * (un[i + 1] - 2 * un[i] + un[i - 1])

x = np.linspace(0, 2, nx)
plt.plot( x, u,label='t='+str(nt*dt))

plt.xlabel('x',fontsize = 20)
plt.ylabel('u',fontsize = 20)
plt.legend()
plt.title('1-D Diffus')
plt.show()
