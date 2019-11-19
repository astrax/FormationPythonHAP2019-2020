# Nom Fichier: Plot3D.py
# Importation
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3 ) * np.exp(-x ** 2 - y ** 2)
n = 100
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)
Z = f(X,Y)
fig = plt.figure()
ax = Axes3D(fig)
S = ax.plot_surface(X, Y, Z, cmap="viridis")
ax.contourf(X, Y, Z, zdir='z', offset=-1, cmap="viridis")
ax.set_zlim(-1, 1)
plt.colorbar(S, shrink=0.5)
plt.show()