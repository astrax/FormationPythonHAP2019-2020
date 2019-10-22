from math import pi

my_pi = 1.  # intialisation
p = 100000
for i in range(1, p):
    my_pi *= 4 * i ** 2 / (4 * i ** 2 - 1.)  # implémentation de la formule de Wallis

my_pi *= 2       # multiplication par 2 de la valeur trouvée

print("La valeur de pi de la bibliothèque 'math': ", pi)
print("La valeur de pi calculer par la formule de Wallis: ", my_pi)

print("La différence entre les deux valeurs:", abs(pi - my_pi)) 
# la fonction abs() donne la valeur absolue