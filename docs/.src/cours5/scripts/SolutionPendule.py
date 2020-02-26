import numpy as np
import matplotlib.pyplot as plt
# SYSTÈME: PENDULE SIMPLE
g = 9.8 # accélération de pesanteur [m/s^2]
l = 1 # longeur du pendule [m]
dt = 0.01 # pas du temps [s]
Tf = 10 # temps finale de la simulation [s]
theta0 = 0.2 # angle initiale [rad]
omega0 = np.sqrt(g/l) 
# SOLUTION EXACTE
def pendule_exacte(t):
    return theta0 * np.cos(omega0 * t)
t = np.arange(0, Tf, dt)

plt.plot(t, pendule_exacte(t), linewidth=2, label="sol exacte")
plt.legend()
plt.ylabel("Amplitude d'oscillation [rad]")
plt.xlabel("Temps [s]")
plt.title("Oscillateur Harmonique")
plt.show()

#%% EULER EXPLICITE
A = np.array([[0, 1], [- omega0**2, 0]])
nsteps = int(Tf/dt)
# CONDITIONS INITIALES: à t = 0; theta = theta0, omega = 0
u0 = np.array([theta0, 0])

Texp = np.zeros(nsteps)
Uexp = np.zeros((2, nsteps))
Texp[0] = 0.0
Uexp[:,0] = u0
# ITÉRATION
for k in range(nsteps-1):
    Texp[k+1] = Texp[k] + dt
    Uexp[:,k+1] = np.dot((np.eye(2) + dt * A), Uexp[:,k])
    
plt.figure(figsize=(10,5))
# PLOT POSITION vs TEMPS
plt.subplot(1,2,1)
plt.plot(Texp,Uexp[0,:], linewidth=2)
plt.xlabel("Temps [s]")
plt.ylabel("Amplitude d'oscillation [rad]")
plt.title("Oscillateur Harmonique (Euler explicite)")
# DIAGRAMME DE PHASE 2D
plt.subplot(1,2,2)
plt.plot(Uexp[0,:],Uexp[1,:], linewidth=2)
plt.xlabel("Amplitude d'oscillation [rad]")
plt.ylabel("Vitesse angulaire [rad/s]")
plt.title("Espace des phases (Euler explicite)")
plt.savefig("Pendule_EulerExp1D.png"); plt.savefig("Pendule_EulerExp1D.pdf")
# DIAGRAMME DE PHASE 3D
from mpl_toolkits.mplot3d.axes3d import Axes3D
plt.figure()
ax = plt.axes(projection="3d")
ax.plot(Texp, Uexp[0,:],Uexp[1,:], linewidth=2)
ax.set_xlabel("Temps [s]")
ax.set_ylabel("Amplitude d'oscillation [rad]")
ax.set_zlabel("Vitesse angulaire [rad/s]")
ax.set_title("Espace des phases (Euler explicite)")
plt.show()

#%% EULER IMPLICITE
from numpy.linalg import inv
Timp = np.zeros(nsteps)
Uimp = np.zeros((2, nsteps))
Timp[0] = 0.0
Uimp[:,0] = u0
# ITÉRATION
for k in range(nsteps-1):
    Timp[k+1] = Timp[k] + dt
    Uimp[:,k+1] = np.dot(inv(np.eye(2) - dt * A), Uimp[:,k])
    
plt.figure(figsize=(10,5))
# PLOT POSITION vs TEMPS
plt.subplot(1,2,1)
plt.plot(Timp,Uimp[0,:], linewidth=2)
plt.xlabel("Temps [s]")
plt.ylabel("Amplitude d'oscillation [rad]")
plt.title("Oscillateur Harmonique (Euler implicite)")
# DIAGRAMME DE PHASE
plt.subplot(1,2,2)
plt.plot(Uimp[0,:],Uimp[1,:], linewidth=2)
plt.xlabel("Amplitude d'oscillation [rad]")
plt.ylabel("Vitesse angulaire [rad/s]")
plt.title("Espace des phases (Euler implicite)")
plt.savefig("Pendule_Eulerimp1D.png"); plt.savefig("Pendule_Eulerimp1D.pdf")
plt.show()
# DIAGRAMME DE PHASE 3D
plt.figure()
ax = plt.axes(projection="3d")
ax.plot(Timp, Uimp[0,:],Uimp[1,:], linewidth=2)
ax.set_xlabel("Temps [s]")
ax.set_ylabel("Amplitude d'oscillation [rad]")
ax.set_zlabel("Vitesse angulaire [rad/s]")
ax.set_title("Espace des phases (Euler implicite)")
plt.savefig("Pendule_Eulerimp3D.png"); plt.savefig("Pendule_Eulerimp3D.pdf")
plt.show()

#%% ILLUSTRATION
plt.figure()
plt.plot(t, pendule_exacte(t), linewidth=2, label="sol exact")
plt.plot(t, Uexp[0,:], linewidth=2, linestyle='--', label="Euler explicite")
plt.plot(t, Uimp[0,:], linewidth=2, linestyle='--', label="Euler implicite")
plt.legend()
plt.xlabel("Temps [s]")
plt.ylabel("Amplitude d'oscillation [rad]")
plt.title("Oscillateur Harmonique avec "+ r"$\Delta t =$"+str(dt))
plt.savefig("Pendule_illustration.png"); plt.savefig("Pendule_illustration.pdf")
plt.show()
#END Program