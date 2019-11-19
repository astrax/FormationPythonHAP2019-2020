# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 14:31:51 2015

@author: Ahmed
"""
from __future__ import division
from numpy import pi, arange,meshgrid
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy.special as ss
from mpl_toolkits.mplot3d import axes3d

lamda=500*1.E-9
k=(2.*pi)/lamda  #wavelength of light in vaccuum

a=1e-6;  # radius of diffracting circular aperture
I0=400  #relative intensity
R=1.E-3 # distance of screen from aperture
Y=arange(-0.25*1.E-2,0.251*1.E-2,1.E-5); Z=Y # coordinates of screen


YY, ZZ =meshgrid(Y, Z)
q=(YY**2+ZZ**2)**0.5
beta=k*a*q/R
I=I0*((ss.jv(1,beta)/beta)**2)

plt.imshow(I, cmap=cm.copper, interpolation='bilinear',
          origin='lower',vmin=0, vmax=1)

plt.xticks([]); plt.yticks([])
#plt.colorbar()
#plt.xlabel(r'$X.10^3$',fontsize=10)
#plt.ylabel(r'$Y.10^3$',fontsize=10)
plt.title('Fraunhofer Diffraction of circular aperture',fontsize=16)
plt.savefig('diff_circle.pdf')

#fig 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface( YY, ZZ,I, rstride=6, cstride=6, cmap=cm.copper, alpha=0.4)
ax.set_xlim3d(-0.002, 0.002)
ax.set_ylim3d(-0.002, 0.002)
ax.set_zlim3d(0, 100)

ax.set_xticks([]); ax.set_yticks([])
plt.title('Fraunhofer Diffraction of circular aperture',fontsize=16)
plt.savefig('diff_circle.pdf')
plt.show()
