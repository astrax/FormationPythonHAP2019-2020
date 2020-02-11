## NOM DU PROGRAMME: OsillateurGneral.py
#% IMPORTATION
import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

def oscillateur_EulerExp(a= 0.25, u0= np.array([2,0]), dt=0.01, Tf = 5):
    # SYSTÈME: OSCILLATEUR LIBRE AMORTI
    w = 2*np.pi # fréquence propre
    A = np.array([[0, 1], [-w**2, -2*a*w]])
    nsteps = int(Tf/dt)
    #%% ITÉRATION: EULER ExPLICITE
    Texp = np.zeros(nsteps)
    Uexp = np.zeros((2, nsteps))
    Texp[0] = 0.0
    Uexp[:,0] = u0
    for k in range(nsteps-1):
        Texp[k+1] = Texp[k] + dt
        Uexp[:,k+1] = np.dot((np.eye(2) + dt * A), Uexp[:,k])
    return Texp, Uexp

Texp1, Uexp1 = oscillateur_EulerExp(a= 0, u0= np.array([2,0]), dt=0.01, Tf = 5)
Texp2, Uexp2 = oscillateur_EulerExp(a= 0.25, u0= np.array([2,0]), dt=0.01, Tf = 5)
Texp3, Uexp3 = oscillateur_EulerExp(a= 1, u0= np.array([2,0]), dt=0.01, Tf = 5)
plt.figure(figsize=(10,5))
# PLOT POSITION vs TEMPS
#plt.suptitle("Simulation d'un oscillateur libre amorti avec un pas d'intégration "+ r"$ \Delta t= %.2f$"%dt,
#             fontweight = "bold")
plt.subplot(1,2,1)
plt.plot(Texp1,Uexp1[0,:], linewidth=2, label=r"$\zeta =0.00$")
plt.plot(Texp2,Uexp2[0,:], linewidth=2, label=r"$\zeta =0.25$")
plt.plot(Texp3,Uexp3[0,:], linewidth=2, label=r"$\zeta =1.00$")
plt.xlabel("Temps")
plt.ylabel("Position")
plt.legend()
plt.title("Trajectoire de la mass M (Euler explicite)")
# DIAGRAMME DE PHASE 2D
plt.subplot(1,2,2)
plt.plot(Uexp1[0,:],Uexp1[1,:], linewidth=2, label=r"$\zeta =0.00$")
plt.plot(Uexp2[0,:],Uexp2[1,:], linewidth=2, label=r"$\zeta =0.25$")
plt.plot(Uexp3[0,:],Uexp3[1,:], linewidth=2, label=r"$\zeta =1.00$")
plt.xlabel("Position")
plt.ylabel("Vitesse")
plt.title("Trajectoire dans l'espace de phase (Euler explicite)")
plt.legend()
plt.show()
plt.savefig("EulerExpGen.png"); plt.savefig("EulerExpGen.pdf")
# DIAGRAMME DE PHASE 3D
plt.figure()
ax = plt.axes(projection="3d")
ax.plot(Texp1,Uexp1[0,:],Uexp1[1,:], linewidth=2, label=r"$\zeta =0.00$")
ax.plot(Texp2,Uexp2[0,:],Uexp1[1,:], linewidth=2, label=r"$\zeta =0.25$")
ax.plot(Texp3,Uexp3[0,:],Uexp1[1,:], linewidth=2, label=r"$\zeta =1.00$")
ax.set_xlabel("Temps")
ax.set_ylabel("Position")
ax.set_zlabel("Vitesse")
ax.set_title("Trajectoire de phase (Euler explicite)")
#plt.savefig("EulerExp3D.png"); plt.savefig("EulerExp3D.pdf")
plt.show()

def oscillateur_EulerImp(a= 0.25, u0= np.array([2,0]), dt=0.01, Tf = 5):
    # SYSTÈME: OSCILLATEUR LIBRE AMORTI
    w = 2*np.pi # fréquence propre
    A = np.array([[0, 1], [-w**2, -2*a*w]])
    nsteps = int(Tf/dt)
    #%% ITÉRATION: EULER ExPLICITE
    Timp = np.zeros(nsteps)
    Uimp = np.zeros((2, nsteps))
    Timp[0] = 0.0
    Uimp[:,0] = u0
    for k in range(nsteps-1):
        Timp[k+1] = Timp[k] + dt
        Uimp[:,k+1] = np.dot(inv(np.eye(2) - dt * A), Uimp[:,k])
    return Timp, Uimp

Timp1, Uimp1 = oscillateur_EulerImp(a= 0, u0= np.array([2,0]), dt=0.01, Tf = 5)
Timp2, Uimp2 = oscillateur_EulerImp(a= 0.25, u0= np.array([2,0]), dt=0.01, Tf = 5)
Timp3, Uimp3 = oscillateur_EulerImp(a= 1, u0= np.array([2,0]), dt=0.01, Tf = 5)
plt.figure(figsize=(10,5))
# PLOT POSITION vs TEMPS
#plt.suptitle("Simulation d'un oscillateur libre amorti avec un pas d'intégration "+ r"$ \Delta t= %.2f$"%dt,
#             fontweight = "bold")
plt.subplot(1,2,1)
plt.plot(Timp1,Uimp1[0,:], linewidth=2, label=r"$\zeta =0.00$")
plt.plot(Timp2,Uimp2[0,:], linewidth=2, label=r"$\zeta =0.25$")
plt.plot(Timp3,Uimp3[0,:], linewidth=2, label=r"$\zeta =1.00$")
plt.xlabel("Temps")
plt.ylabel("Position")
plt.legend()
plt.title("Trajectoire de la mass M (Euler implicite)")
# DIAGRAMME DE PHASE 2D
plt.subplot(1,2,2)
plt.plot(Uimp1[0,:],Uimp1[1,:], linewidth=2, label=r"$\zeta =0.00$")
plt.plot(Uimp2[0,:],Uimp2[1,:], linewidth=2, label=r"$\zeta =0.25$")
plt.plot(Uimp3[0,:],Uimp3[1,:], linewidth=2, label=r"$\zeta =1.00$")
plt.xlabel("Position")
plt.ylabel("Vitesse")
plt.title("Trajectoire dans l'espace de phase (Euler implicite)")
plt.show()
plt.savefig("EulerExpGen2.png"); plt.savefig("EulerExpGen2.pdf")
# DIAGRAMME DE PHASE 3D
plt.figure()
ax = plt.axes(projection="3d")
ax.plot(Timp1,Uimp1[0,:],Uimp1[1,:], linewidth=2, label=r"$\zeta =0.00$")
ax.plot(Timp2,Uimp2[0,:],Uimp1[1,:], linewidth=2, label=r"$\zeta =0.25$")
ax.plot(Timp3,Uimp3[0,:],Uimp1[1,:], linewidth=2, label=r"$\zeta =1.00$")
ax.set_xlabel("Temps")
ax.set_ylabel("Position")
ax.set_zlabel("Vitesse")
ax.set_title("Trajectoire de phase (Euler implicite)")
#plt.savefig("Eulerimp3D.png"); plt.savefig("Eulerimp3D.pdf")
plt.show()