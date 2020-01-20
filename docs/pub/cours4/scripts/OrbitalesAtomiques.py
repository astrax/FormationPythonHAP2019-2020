## NOM DU PROGRAMME: OrbitalesAtomiques.py
#% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt
from midpoint_integral import midpoint
# a) 
def densite_radiale(r, a0 = 0.529):
    return 4 * (r**2/a0**3) * np.exp(-2*(r/a0))
# b)
r = np.linspace(0,2.6, 100)

plt.figure(figsize=(7,5))
plt.plot(r, densite_radiale(r), label = "densité radiale pour une OA 1s")
plt.xlabel("r "+r"$[\AA]$")
plt.ylabel("densité radiale")
plt.legend()
plt.show()

# c) probabilité de présence de l’électron entre 0 et a0
a0 = 0.529
Pa0 = midpoint(densite_radiale, 0, a0, 100)
print("La probabilité de présence de l’électron entre 0 et a0 est: ", Pa0)

# d) rayon moyen de l'OA 1s

for n in range(21):
    Prn = midpoint(densite_radiale, 0, n*a0, 100)
    if Prn >= 0.90:
        print("n = %d, Pr%d = %.4f"%(n,n,Prn))
    
'''
r90 = 3*a0. On dit donc que la rayon moyen de l'OA 1s de l'atome d'hydrogène 
est une sphère de rayon 3*a0, soit à peu près 1.6 Å.
'''

# e)
Pr = midpoint(densite_radiale, 0.9*a0, 1.1*a0, 100)
print("La probabilité de présence de l’électron entre 0.9*a0 et 1.1*a0 est: ", Pr)

# La probabilité de présence de l’électron entre 0.9*a0 et 1.1*a0 est:  0.10790737203009312

# f) Conclusion

'''
* La densité radiale de probabilité de présence est maximale 
pour r = a0 (rayon de Bohr) On dit que c'est le rayon le plus probable.

* Ce résultat est trompeur, car entre 0.9*a0  et 1.1*a0, la probabilité de présence
de l'électron n'est que de 11%.

* l'atome d'hydrogène est une sphère de rayon 3*a0, soit à peu près 1.6 Å.

* La probabilité de présence de l’électron 1s est plus élevée à l’extérieur 
de l’orbite de Bohr. 
'''
