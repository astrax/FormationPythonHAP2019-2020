# NOM DU FICHIER: ex2deuxfonctions.py
# Importer tout de matplotlib et numpy
from pylab import *
def g(y):
    return exp(-y)*sin(4*y)
def h(y):
    return exp(-(3./2)*y)*sin(4*y)

y = np.linspace(0, 4, 501)
plt.figure()
plt.plot(y, g(y), 'r-', y, h(y), 'k--')
plt.xlabel('y'); plt.ylabel('g(y)')
plt.title('Onde sinusoïdale atténuée')
plt.legend(['g', 'h'])
plt.savefig("fig_ex2.png"); plt.savefig("fig_ex2.pdf")
plt.show()