# -*- coding: utf-8 -*-
"""
cfd-with-python

1-D Non-Linear Convection
~inviscid Burgers equation~
du/dt + u*du/dx = 0

Discretize forward in time, backward in space
u_i^(n+1) - u_i^n             u_i^n - u_(i-1)^n
-----------------  +  u_i^n * -----------------  =  0
       dt                             dx

solve for: u_i^(n+1)
"""

import numpy as np
import matplotlib.pyplot as plt

# ===========================Variable Declarations==============================

nx = 41            # number of grid points in x domain of  0 to 2
dx = 2 / (nx-1)     # distance between grid points in x domain
nt = 25             # nt is the number of timesteps to calculate
dt = .01          # dt is the amount of time each timestep covers (delta t)
c=1
# if at time dt, the wave is travelling a distance which is greater than dx there will be numerical instability
# introduce the Courant number to insure stability. sigma = u*dt/dx <= sigmaMax
sigma = .999          #sigma = the Courant number
dt = sigma*dx/2        # dt is the amount of time each timestep covers (delta t)
print(dt)
x=np.linspace(0,2,nx)   # create array of x domain
u = np.ones(nx)         # create a (1 x n) vector of 1's

# ==========================Assign Initial Conditions===========================

# set hat function I.C. : u(.5<=x<=1) is 2
u[int(.5 / dx):int(1 / dx + 1)] = 2  
# plt.plot( x, u,label='t=0')

# ================================Evaluate PDE==================================
plt.axis([0, 2.1, 0.8, 2.1])
plt.ion()
hl, = plt.plot(x, u)

for n in range(nt): # loop for values of n from 0 to nt, so it will run nt times
    un = u.copy()   # copy the existing values of u into un
    for i in range(1, nx): 
        u[i] = un[i] - un[i] * dt / dx * (un[i] - un[i - 1])

    hl.set_ydata(u)
    plt.pause(0.1)

# ================================Plot Results==================================
#
# x=np.linspace(0,2,nx)
# plt.plot( x, u,label='t=%0.3f' %(nt*dt))
#
# plt.xlim(0,3)
# plt.ylim(0,3)
# plt.xlabel('Distance X')
# plt.ylabel('Velocity U')
# #plt.legend()
# plt.title('1D Convection')
# plt.show()