# Nom Fichier: Imshow.py
# Importation
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3 ) * np.exp(-x ** 2 - y ** 2)

n = 30
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
# Image
im = plt.imshow(Z, interpolation='nearest', cmap='gray', origin='lower')

plt.colorbar(im)
plt.show()