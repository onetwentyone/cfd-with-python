# -*- coding: utf-8 -*-
"""
cfd-with-python

non-linear convection
~inviscid Burgers equation~
du/dt + u*du/dx = 0

"""

import numpy as np
import matplotlib.pyplot as plt


nx = 81    # try changing this number from 41 to 81 and Run All ... what happens?
dx = 2 / (nx-1)
nt = 25    #nt is the number of timesteps we want to calculate
dt = .025  #dt is the amount of time each timestep covers (delta t)s
# if at time dt, the wave is travelling a distance which is greater than dx there will be numerical instability
# introduce the Courant number to insure stability. sigma = u*dt/dx <= sigmaMax
sigma = .5 #sigma = the Courant number
dt = sigma * dx

u = np.ones(nx)      #np function ones()
u[int(.5 / dx):int(1 / dx + 1)] = 2  #setting u = 2 between 0.5 and 1 as per our I.C.s
# print(u)
x=np.linspace(0,2,nx)

plt.plot( x, u,label='t=0')


un = np.ones(nx)  # initialize a temporary array
for n in range(nt):  # loop for values of n from 0 to nt, so it will run nt times
    un = u.copy()  ##copy the existing values of u into un
    for i in range(1, nx):  ## you can try commenting this line and...
        u[i] = un[i] - u[i] * dt / dx * (un[i] - un[i - 1])

x=np.linspace(0,2,nx)
plt.plot( x, u,label='t='+str(nt*dt))

plt.xlabel('x',fontsize = 20)
plt.ylabel('u',fontsize = 20)
plt.legend()
plt.title('Wave with c=u[i]')
plt.show()
