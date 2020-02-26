## NOM DU PROGRAMME: projectile.py
#%% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt
#%% CONSTANTES
# accélération de la pesanteur(m/s^2)
g = 9.8
# angles de tire (deg)
angles = [30, 35, 40, 45, 50, 55]
# vitesse initiale (m/s())
v0 = 20.0 
N = 10000 # Nombre de pas de temps
# pas de temps (s)
dt =0.001
#%% VLEURS INITIALES
x = np.zeros(N)
y = np.zeros(N)
vx = np.zeros(N)
vy = np.zeros(N)
for theta in angles:
    vx[0] = v0 * np.cos(theta*np.pi/180.0)
    vy[0] = v0 * np.sin(theta*np.pi/180.0)
    x[0], y[0]=0, 1
    # MÉTHODE D'EULER
    for i in range(N-1):
        x[i+1] = x[i] + vx[i] * dt
        y[i+1] = y[i] + vy[i] * dt
        vx[i+1] = vx[i]
        vy[i+1] = vy[i] - g * dt
    plt.plot(x, y, lw =2, label=str(theta)+' deg')
#%% GRAPHIQUE: TRAJECTOIRES
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.suptitle("Trajectoire d'un projectile", weight='bold')
plt.title(r'Pas de temps: $\Delta_t$ = {:.3f} s'.format(dt))
plt.grid()
plt.legend()
plt.axis([0, 45, 0, 15])
# ENREGISTRER ET AFFICHER LA FIGURE
plt.savefig("projectile.png")
plt.savefig("projectile.pdf")
plt.show()