## NOM DU PROGRAMME: tire.py
#%% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt
#%% CONSTANTES
# accélération de la pesanteur (m/s^2)
g = 9.8
# vitesse initiale (m/s)
v0 = 10.0 
# plage cible (m)
xcible = 8.0 
# comment nous devons nous rapprocher (m)
eps = 0.01 
# pas de temps (s)
dt = 0.001 
# angle (degrés) que le projectile tombe trop court
theta1 = 0.0 
# angle (degrés) que le projectile tombe trop loin
theta2 = 45.0
# une valeur initiale> eps
dx = 2*eps 
#%% BOUCLE PRINCIPALE: MÉTHODE DE TIRE
while abs(dx) > eps:
    # devinez à la valeur de thêta
    theta = (theta1+theta2)/2.0
    x = [0.0]
    y = [0.0]
    vx = [v0*np.cos(theta*np.pi/180.0)]
    vy = [v0*np.sin(theta*np.pi/180.0)]
    # MÉTHODE D'EULER
    i = 0
    while y[i] >= 0.0:
        # appliquer une différence finie approximative 
        # aux équations du mouvement
        x += [x[i]+vx[i]*dt]
        y += [y[i]+vy[i]*dt]
        vx += [vx[i]]
        vy += [vy[i] - g*dt]
        i = i+1
    # nous avons touché le sol quelque part entre l'étape i-1 et i 
    # interpoler pour trouver cet emplacement
    xsol = x[i - 1]+y[i - 1]*(x[i] - x[i - 1])/(y[i] - y[i - 1])
    # mettre à jour les limites encadrant la racine
    dx = xsol - xcible
    if dx < 0.0: # trop court: mettre à jour l'angle plus petit
        theta1 = theta
    else: # trop loin: mettre à jour un angle plus grand
        theta2 = theta
#%% GRAPHIQUE: TRAJECTOIRES
plt.plot(x, y, lw =2)
plt.plot([xcible], [0.0], 'o', ms=12)
plt.annotate('Cible', xy=(xcible, 0), xycoords='data', xytext=(5,5),
             textcoords='offset points')
plt.title(r"trajectoire d'un projectile avec $\theta$ = %.2f deg"% theta)
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.ylim(ymin=0.0)
plt.grid()
# ENREGISTRER ET AFFICHER LA FIGURE
plt.savefig("tire.png")
plt.savefig("tire.pdf")
plt.show()