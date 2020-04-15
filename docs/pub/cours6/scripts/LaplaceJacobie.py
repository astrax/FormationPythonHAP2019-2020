# -*- coding: utf-8 -*-
# Programme de rÃ©solution de l'Ã©quation de Laplace
# par la mÃ©thode de Jacobi
# Dominique Lefebvre pour TangenteX.com
# 25 fÃ©vrier 2016
#

# importation des librairies
import numpy as np
import time
import matplotlib.pyplot as plt

# dÃ©finition des paramÃ¨tres physiques de l'expÃ©rience
Vi = 100.0           # le couvercle est Ã  100 V
V0 = 0.0             # les cotÃ©s sont au potentiel nul
  
# dÃ©finition de la grille de calcul
N = 100                     # nombre de pas sur la grile (identique en Ox et Oy)
V = np.empty([N+1,N+1])     # grille de calcul courante
Vnew = np.empty([N+1,N+1])  # grille de stockage des calculs nouveaux

# critÃ¨re de prÃ©cision du calcul
EPS = 1e-3
# initialisation des compteurs        
ecart = 1.0
iteration = 0

# dÃ©finition des conditions aux limites
V[0,:]  = Vi  # bord supÃ©rieur
V[:,0]  = V0  # bord gauche
V[:,-1] = V0  # bord droit
V[-1,:] = V0  # bord infÃ©rieur

# initialisation de l'intÃ©rieur de la grille
V[1:N,1:N] = 0.0

# dÃ©but du calcul - enregistrement de la durÃ©e
tdebut = time.time()

# boucle de calcul - mÃ©thode de Jacobi en utilisant la vectorisation des boucles
Vnew = V.copy()
while ecart > EPS: 
    iteration += 1   
    # boucle de calcul Numpy
    Vnew[1:-1,1:-1]= 0.25*(V[0:-2,1:-1] +V[2:,1:-1] + V[1:-1,0:-2] + V[1:-1,2:])
    # critÃ¨re de convergence
    ecart = np.max(np.abs(Vnew - V))
    # sauvegarde dans la grille V de la grille calculÃ©e    
    V = Vnew.copy()
   
# fin du calcul - affichage de la durÃ©e
print('Nombre iterations : ',iteration)
print('Temps de calcul (s) : ',time.time() - tdebut)
    
# Affichage des rÃ©sultats
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111)    
im = plt.imshow(V,cmap='viridis')

plt.colorbar(im)
plt.show()


