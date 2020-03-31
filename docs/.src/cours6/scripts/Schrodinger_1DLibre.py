## NOM DU PROGRAMME: Schrodinger_1DLibre.py
#% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt
'''
Définition des constantes
-------------------------
Les constantes physiques standards sont tirées 
du package scipy.constants
'''
from scipy.constants import h, hbar, e, m_e

DeuxPi = 2.0*np.pi
L = 5.0e-9   # dimension de la boite quantique (USI)  

#%% Définition du domaine spatial et temporel
Nx = 1000    # nombre de pas d'intégration sur le domaine spatial
xmin = 0.0
xmax = L
dx = (xmax-xmin)/Nx
x = np.arange(0.0,L,dx)
Nt = 30000   # nombre de pas d'intégration sur le domaine temporel 
a2 = 0.1
dt = a2*2*m_e*dx**2/hbar
a3 = e*dt/hbar

#%% Définition des paramètres du paquet d'onde inital
x0 = x[int(Nx/2)]  # position initiale du paquet
sigma = 2.0e-10    # largeur du paquet en m
Lambda = 1.5e-10   # longeur d'onde de de Broglie l'électron (en m)
Ec = (h/Lambda)**2/(2*m_e*e) # énergie cinétique théorique de l'électron (en eV)

#%% Définition du potentiel
U = np.zeros(Nx)  # électron libre dans le puit

#%% Initialisation des buffers de calcul aux conditions initiales
Psi_Real = np.zeros(Nx)
Psi_Imag = np.zeros(Nx)
Psi_Prob = np.zeros(Nx)

#%% calcul et affichage de la fonction d'onde initiale
Psi_Real = np.exp(-0.5*((x-x0)/sigma)**2)*np.cos(DeuxPi*(x-x0)/Lambda)
Psi_Imag = np.exp(-0.5*((x-x0)/sigma)**2)*np.sin(DeuxPi*(x-x0)/Lambda)
# Normalisation du paquet d'onde
Psi_Prob = Psi_Real**2 + Psi_Imag**2
## FIGURE ---> Test
#plt.figure()
#pl1, pl2, pl3 = plt.plot(x, Psi_Real, x, Psi_Imag, x, Psi_Prob)
#plt.legend((pl1, pl2,pl3), ("PSI R", "PSI Imag", "Psi Prob"))
#plt.show()

#%% Boucle de calcul et d'affichage de l'évolution
for t in range(Nt):
    plt.clf()
    Psi_Real[1:-1] = Psi_Real[1:-1] - a2*(Psi_Imag[2:] - 2*Psi_Imag[1:-1] + Psi_Imag[:-2]) \
                     + a3*U[1:-1]*Psi_Imag[1:-1]
    Psi_Imag[1:-1] = Psi_Imag[1:-1] + a2*(Psi_Real[2:] - 2*Psi_Real[1:-1] + Psi_Real[:-2]) \
                     - a3*U[1:-1]*Psi_Real[1:-1]
    Psi_Prob[1:-1] = Psi_Real[1:-1]**2 + Psi_Imag[1:-1]**2
    if t % 1000 == 0:
        
        plt.figure(1)
        plt.plot(x*1.e9,Psi_Real,'blue')
        plt.plot(x*1.e9,Psi_Imag,'red')
        plt.plot(x*1.e9,Psi_Prob,'green')
        plt.axis([0,L*1.e9,-1,1])
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("anim2/"+str(int(t%Nt/1000)).rjust(2, '0')+".png")
        plt.savefig("anim2/myimage.pdf")
        plt.show()
        plt.pause(0.001)
