import numpy as np
import matplotlib.pyplot as plt
# Charger les données du fichier 'cosinus.dat'
X, C = np.loadtxt('cosinus.dat', comments='#', unpack=True)
# Tracer C en fonction de X
plt.plot(X,C)
plt.title("cos(x)")
plt.xlabel("X")
plt.ylabel("C")
plt.show()