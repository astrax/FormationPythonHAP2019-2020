## NOM DU PROGRAMME: projectile.py
#%% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt
#%% CONSTANTS
# constante de pesenteur (m/s^2)
g = 9.8
v0 = 20.0
xtarget = 8.0 
N = 10000 # Nombre de pas de temps
# pas de temps
dt =0.001
# how close we must get (m)
eps = 0.01 
theta1 = 0.0 # bracketing angle (degrees) that falls too short
theta2 = 45.0 # bracketing angle (degrees) that falls too far
dx = 2*eps # some initial value > eps
#%% VLEURS INITIALES
x = np.zeros(N)
y = np.zeros(N)
vx = np.zeros(N)
vy = np.zeros(N)
# 
# guess at the value of theta

while abs(dx) > eps:
    theta = (theta1+theta2)/2.0
    vx[0] = v0 * np.cos(theta*np.pi/180.0)
    vy[0] = v0 * np.sin(theta*np.pi/180.0)
    x[0], y[0]=0, 1
    # MÉTHODE D'EULER
    for i in range(N-1):
        x[i+1] = x[i] + vx[i] * dt
        y[i+1] = y[i] + vy[i] * dt
        vx[i+1] = vx[i]
        vy[i+1] = vy[i] - g * dt
    # we hit the ground somewhere between step i-1 and i interpolate to find
    # this location
        if y[i+1]>=0:
            xground = x[i+1]
    # update the bounds bracketing the root
    dx = xground - xtarget
    if dx < 0.0: # too short: update smaller angle
        theta1 = theta
    else: # too far: update larger angle
        theta2 = theta
    print(theta)
            
plt.plot(x, y, lw =2, label=str(theta)+' deg')
#%% GRAPHIQUE
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.suptitle("Trajectoire d'un projectile", weight='bold')
plt.title(r'Pas de temps: $\Delta_t$ = {:.3f} s'.format(dt))
plt.grid()
plt.legend()
plt.axis([0, 45, 0, 15])
# ENREGISTRER ET AFFICHER LA FIGURE
plt.show()