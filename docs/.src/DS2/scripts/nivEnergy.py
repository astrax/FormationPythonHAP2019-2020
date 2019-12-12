## NOM DU PROGRAMME: -----
#% IMPORTATION
# Constantes
me = 9.1094e-31
e = 1.6022e-19
eps0 = 8.8542e-12
h = 6.6261e-34
def E(n):
    Ejoule = - (me * e**4)/(8*eps0**2 * h**2)* (1/n**2)
    return Ejoule/e
# niveau d'énergie fondamentale
print("E(n = 1) = ", E(n = 1), " eV")
print("E(n = 100) = ", E(n = 100), " eV")

# affichage de différents niveaux d'énergie
for n in range(1, 21):
    print("E{} = {} eV".format(n, E(n)))
# énergie libéré par l'électron
from numpy import array
DEn = [[E(ni) - E(nf) for ni in range(1, 6)] for nf in range(1,6)]
print(array(DEn))
#==> DEn = 
#[[  0.          10.20461453  12.09435796  12.75576816  13.06190659]
# [-10.20461453   0.           1.88974343   2.55115363   2.85729207]
# [-12.09435796  -1.88974343   0.           0.6614102    0.96754864]
# [-12.75576816  -2.55115363  -0.6614102    0.           0.30613844]
# [-13.06190659  -2.85729207  -0.96754864  -0.30613844   0.        ]]
