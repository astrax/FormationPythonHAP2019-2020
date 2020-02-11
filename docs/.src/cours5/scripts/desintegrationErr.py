## NOM DU PROGRAMME: desintegrationErr.py
#IMPORTATION
import numpy as np
import matplotlib.pyplot as plt
# ENTRÉES
noyaux0 = int(input("nombre initial de noyaux: "))
tau = float(input('constante de temps de décroissance: '))
dtbas = float(input('pas de temps de résolution le plus bas: '))
nres = int(input('nombre de raffinements de résolution: '))
tmax = int(input('temps de fin de la simulation: '))
# BOUCLE PRINCIPALE: CALCUL D'ERREURS
for n in range(nres):
    raffine = 10**n
    dt = dtbas/raffine
    nsteps = int(tmax/dt)
    noyaux = noyaux0
    err = np.zeros(nsteps)
    t = np.zeros(nsteps)
    # BOUCLE SECONDAIRE: MÉTHODE D'EULER
    for i in range(nsteps-1):
        t[i+1] = t[i] + dt
        noyaux = noyaux - noyaux/tau*dt
        exact = noyaux0 * np.exp(- t[i+1]/tau)
        err[i+1] = abs((noyaux - exact)/exact)
    # tracer l'erreur à cette résolution
    plt.loglog(t[raffine::raffine], err[raffine::raffine],
               '.-', label='dt = '+str(dt))
    
plt.legend(loc=4)
plt.xlabel('temps')
plt.ylabel('erreur fractionnaire')
plt.title("Erreur d'intégration de la désintégration radioactive")
plt.grid(linestyle='-', which='major')
plt.grid(which='minor')
plt.savefig("desintegrationErr.png")
plt.savefig("desintegrationErr.pdf")
plt.show()