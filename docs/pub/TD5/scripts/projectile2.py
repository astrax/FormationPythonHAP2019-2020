#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 17:11:10 2019
projectile2.py
source: http://visual.icse.us.edu.pl/szkola/ProjectileMotion.html
see also: http://gappyfacets.com/2016/03/28/python-projectile-motion-classical-physics-test/

@author: ahmed
"""

# Import various functions meant for numerical science
import numpy as np
from math import cos,sin,pi
import matplotlib.pyplot as plt

t_0 = 0 # Start time, s
t_end = 10 # End time, s
N = 1000 # Number of time steps

# Create a uniformly spaced time-array
t = np.linspace(t_0, t_end, N+1)

# Calculate the size of a time step
dt = t[1] - t[0]

# Create empty acceleration, velocity and position arrays
a = np.zeros((N+1,2))
v = np.zeros((N+1,2))
r = np.zeros((N+1,2))

# Set initial conditions
v[0] = (100*cos(pi/6), 100*sin(pi/6)) # inital velocity, m/s
r[0] = (0,1)  # initial position, m

m = 5.5 # mass, kg
g = 9.81 # acceleration of gravity, m/s^2
rho = 1.3 # air density, kg/m^3
C_D = 0.45 # drag coefficient
d = 0.11 # diameter of cannonball, m
A = pi*d**2 # cross-sectional area, m^2

def F(r, v, t):
    return (0, -m*g) - 0.5*rho*C_D*A*abs(v)*v

# Solving equations of motion iteratively
for i in range(N):
    a[i] = F(r[i], v[i], t[i])/m
    v[i+1] = v[i] + a[i]*dt
    r[i+1] = r[i] + v[i]*dt

# Extract x and y coordinates
x = r[:,0]
y = r[:,1]

# Plot figure
plt.plot(x,y)

# Prettify the plot
plt.xlabel('Horizontal distance, [m]')
plt.ylabel('Vertical distance, [m]')
plt.title('Trajectory of a fired cannonball')
plt.grid()
#plt.axis([0, 900, 0, 250])

# Makes the plot appear on the screen
plt.show()
