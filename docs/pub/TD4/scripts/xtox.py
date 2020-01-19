## NOM DU PROGRAMME: xtox.py
#% IMPORTATION
from integration_adaptive import integration_adaptative

def f(x):
    return x**x

eps = 1E-4
a = 0.0;  b = 2.0

# Choisir la méthode milieu
n = integration_adaptative(f, a, b, eps, 'midpoint')
if n > 0:
    print('n suffisant est: %d'%(n))
else:
    # Le n négatif est renvoyé pour signaler que la limite supérieure de n 
    # a été dépassée
    print("Aucun n n'a été trouvé dans %d iterations"  % (abs(n)))