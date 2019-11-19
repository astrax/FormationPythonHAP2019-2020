# Nom Fichier: ContourPlot.py
# Importation
import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X,Y = np.meshgrid(x, y)

# Surface
S = plt.contourf(X, Y, f(X, Y), 8, cmap='plasma')
# Contour
C = plt.contour(X, Y, f(X, Y), 8, colors='black')
plt.clabel(C, inline=1, fontsize=10)

plt.colorbar(S) # afficher la barre de couleurs
plt.show()