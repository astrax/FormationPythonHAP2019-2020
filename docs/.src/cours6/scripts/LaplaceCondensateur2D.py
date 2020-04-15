## NOM DU PROGRAMME: LaplaceCondensateur2D.py
#% IMPORTATION
# -*- coding: utf-8 -*-
# Programme de calcul de potentiel crÃ©Ã© par un condensateur plan
# dans ubne boite reliÃ©e Ã  la terre.
# MÃ©thode de Gauss-Seidel
# Dominique Lefebvre pour TangenteX.com
# 2 mars 2016
#

# importation des librairies
from numpy import max,abs,empty,linspace,meshgrid
import time
import matplotlib
import matplotlib.pyplot as plt

# dÃ©finition des paramÃ¨tres physiques de l'expÃ©rience
V0 = 0.0             # les cotÃ©s de la boite sont au potentiel nul
Vp = 400.0           # potentiel de plaque 
  
# dÃ©finition de la grille de calcul
N = 100                  # nombre de pas sur la grile (identique en Ox et Oy)
V = empty([N+1,N+1])     # crÃ©ation de la grille, en float par dÃ©faut

# critÃ¨re de prÃ©cision du calcul
EPS = 1e-3        # prÃ©cision souhaitÃ©e pour le critÃ¨re de convergence

# initialisation des compteurs
ecart = 1.0       
iteration = 0

# dÃ©finition des conditions aux limites
V[0,:]  = V0  # bord supÃ©rieur
V[:,0]  = V0  # bord gauche
V[:,-1] = V0  # bord droit
V[-1,:] = V0  # bord infÃ©rieur

# initialisation de l'intÃ©rieur de la grille
V[1:N,1:N] = 0.0

# dÃ©finition de la gÃ©omÃ©trie du condensateur
V[25:75,40]  = -Vp  # bord plaque gauche potentiel nÃ©gatif
V[25:75,60]  = Vp   # bord plaque droit potentiel positif

# dÃ©but du calcul - enregistrement de la durÃ©e
tdebut = time.time()

# boucle de calcul - mÃ©thode de Gauss-Seidel
while ecart > EPS:    
    iteration += 1
    # sauvegarde de la grille courante pour calculer l'Ã©cart
    Vprec = V.copy()
    # calcul de la nouvelle valeur du potentiel sur la grille
    V[1:-1,1:-1]= 0.25*(Vprec[0:-2,1:-1] +V[2:,1:-1] + Vprec[1:-1,0:-2] + V[1:-1,2:])
    # je rÃ©affecte les valeurs constantes sur les plaques
    V[25:75,40]  = -Vp  
    V[25:75,60]  = Vp   
    # critÃ¨re de convergence
    ecart = max(abs(V-Vprec))
   
# fin du calcul - affichage de la durÃ©e
print('Nombre iterations : ',iteration) 
print('Temps de calcul (s) : ',time.time() - tdebut)
 
# Affichage des rÃ©sultats
fig = plt.figure(figsize=(6,5))
ax = fig.add_subplot(1,1,1) 

# dessin des deux plaques
plt.plot([40,40],[25,75],'b-', lw = 4)  # plaque gauche
plt.plot([60,60],[25,75],'r-', lw = 4)  # plaque droite

# dessin de la grille de calcul
plt.grid()

# tracÃ© des Ã©quipotentielles
x = linspace(0,N+1,N+1)
y = linspace(0,N+1,N+1)
X,Y = meshgrid(x,y)
equ = plt.contour(X,Y,V,20,colors='w', alpha = .5)
#matplotlib.rcParams['contour.negative_linestyle'] = 'solid'
plt.clabel(equ, fontsize=10, inline=1,fmt='%1.0f')

# tracÃ© de la grille
plt.imshow(V, cmap='viridis')
plt.colorbar()

plt.show()

