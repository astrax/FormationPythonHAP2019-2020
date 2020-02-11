#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 22:01:03 2019

@author: ahmed
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
from mpl_toolkits.mplot3d.axes3d import Axes3D

w = 2*np.pi # fréquence propre
d = 0.25    # rapport d'amotissement
# SYSTÈME: OSCILLATEUR LIBRE AMORTIE
A = np.array([[0, 1], [-w**2, -2*d*w]])

dt = 0.01 # pas de temps
T = 10 # temps finale
nsteps = int(T/dt)
# CONDITION INITIAL: x = 2, v = 0
x0 = np.array([2,0])
#%% ITÉRATION: EULER Progressive
TF = np.zeros(nsteps)
XF = np.zeros((2, nsteps))
TF[0] = 0.0
XF[:,0] = x0
for k in range(nsteps-1):
    TF[k+1] = TF[k] + dt
    XF[:,k+1] = np.dot((np.eye(2) + dt * A), XF[:,k])

plt.figure()
plt.plot(TF,XF[0,:])
plt.xlabel("Temps")
plt.ylabel("Position")
plt.grid()
plt.tight_layout()
plt.show()

plt.figure()
plt.plot(XF[0,:],XF[1,:])
plt.xlabel("Position")
plt.ylabel("Vitesse")
plt.title("Diagramme de phase")
plt.grid()
plt.tight_layout()
plt.show()
# FIGURE 3D
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot(TF, XF[0,:],XF[1,:], '-b')
plt.show()
#%% ITÉRATION: EULER REGRESSIVE
TFb = np.zeros(nsteps)
XFb = np.zeros((2, nsteps))
TFb[0] = 0.0
XFb[:,0] = x0
for k in range(nsteps-1):
    TFb[k+1] = TFb[k] + dt
    XFb[:,k+1] = np.dot(inv(np.eye(2) - dt * A), XFb[:,k])

plt.figure()
plt.plot(TFb,XFb[0,:])
plt.xlabel("Temps")
plt.ylabel("Position")
plt.grid()
plt.tight_layout()
plt.show()

plt.figure()
plt.plot(XFb[0,:],XFb[1,:])
plt.xlabel("Position")
plt.ylabel("Vitesse")
plt.title("Diagramme de phase")
plt.grid()
plt.tight_layout()
plt.show()
