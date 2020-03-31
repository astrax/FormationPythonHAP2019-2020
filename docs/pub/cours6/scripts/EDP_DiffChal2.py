## NOM DU PROGRAMME: EDP_DiffChalAnim.py
#% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt
# DONNÉES NUMÉRIQUES
L = 1 # Longueur de la barre [m]
Nx = 100 # Nombre de tronçons
tau = 1 # Durée totale de l'évolution [s]
Nt = 10000 # Nombre d'intervalles de temps
dx = L/Nx # Longueur du tronçon
dt = tau/Nt # Intervalle élémentaire de temps
D = 0.5 # Coefficient de diffusion thermique
Tb = 100 # Température initiale de la barre
Textr = 0 # Température des extrémités
# Construction de axe des abscisses (variable espace x)
x = np.linspace(0, L, Nx)
# Construction CI ,CL (2 exemples pour la CI)
T = [Textr] + (Nx - 2)*[Tb] + [Textr] # Echelon de temperature
#T=Textr + (Tb-Textr ) * np.sin(np.pi*x/L) # Arche sinusoidale temperature
# Construction du tableau vierge des accroissements de temperature
accroissT = np.zeros(Nx)
T[0] = 0

# Corps de la résolution
for n in range(Nt): # Boucle d'évolution de temps pas à pas
    plt.clf()
    for m in range(1, Nx-1): #boucle de calcul de accroissement de temperature pour chaque abscisse
        accroissT[m] = ((dt*D)/(dx**2))*(T[m-1]-2*T[m]+T[m+1])
    for m in range(1, Nx-1): # Boucle de calcul de T instant  suivant
        T[m] += accroissT[m]  
    if (n%100 == 0):    
        plt.figure(1)
        plotlabel ="t=%1.2f s"%(n*dt)
        plt.plot(x, T, lw = 4, label=plotlabel, color = plt.get_cmap('jet')(1-n/Nt))
            
        plt.grid()
        plt.xlabel("x [m]", fontsize=14)
        plt.ylabel("T [C]", fontsize=14)
        plt.title("Évolution de la température après le choc thermique", weight ="bold")
        plt.legend(loc=1)
        plt.axis([0,L,0,100])
        
        plt.savefig("anim/chaleur"+str(int((n%Nt)/100)).zfill(2) +".jpg")
        plt.tight_layout()
        plt.show()

        plt.pause(0.001)
        
        