# NOM DU FICHIER: OscillateurAmotiODE.py
#% IMPORTATION

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

w = 2*np.pi # fréquence propre
d = 0.25    # rapport d'amotissement
# SYSTÈME: OSCILLATEUR LIBRE AMORTIE
A = np.array([[0, 1], [-w**2, -2*d*w]])

dt = 0.01 # pas du temps
T = 10 # temps finale
nsteps = int(T/dt)
# CONDITION INITIAL: x = 2, v = 0
x0 = np.array([2,0])
#%% ITÉRATION: EULER FORWARD
TF = np.zeros(nsteps)
XF = np.zeros((2, nsteps))
TF[0] = 0.0
XF[:,0] = x0
for k in range(nsteps-1):
    TF[k+1] = TF[k] + dt
    XF[:,k+1] = np.dot((np.eye(2) + dt * A), XF[:,k])
# utiliser fonction reshape (changer la forme)
#xf = np.reshape(XF[:1], (nsteps))
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

#%% ITÉRATION: EULER BACKWARD
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
