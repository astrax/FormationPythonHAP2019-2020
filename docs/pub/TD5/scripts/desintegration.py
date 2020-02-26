## NOM DU PROGRAMME: desintegration.py
#%% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt
#%% SOLUTION EXACTE
def n_exact(t, noyaux0, tau):
    return noyaux0*np.exp(-t/tau)
#%% ENTRÉES
noyaux0 = int(input("nombre initial de noyaux: "))
tau = float(input('constante de temps de décroissance: '))
dt = float(input('pas de temps: '))
tmax = int(input('temps de fin de la simulation: '))
nsteps = int(tmax/dt)
noyaux = np.zeros(nsteps)
t = np.zeros(nsteps)
#%% VLEURS INITIALES
t[0] = 0.0
noyaux[0] =noyaux0
#%% BOUCLE PRINCIPALE: MÉTHODE D'EULER
for i in range(nsteps-1):
    t[i+1] = t[i] + dt
    noyaux[i+1] = noyaux[i] - noyaux[i]/tau*dt
#%% TRAÇAGE DU GRAPHIQUE
plt.figure(figsize=(8,5))
plt.plot(t, noyaux, '-r', label='Solution: Euler')
plt.plot(t, n_exact(t, noyaux0, tau), '--b', label='Solution exacte')
plt.xlabel('temps')
plt.ylabel('N(t)')
plt.title('Désintégration radioactive')
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig("desintegration.png")
plt.savefig("desintegration.pdf")
plt.show()