## NOM DU PROGRAMME: compare_integration_methods.py
#% IMPORTATION
from trapeze_integral import trapeze
from midpoint_integral import midpoint
from math import exp

g = lambda y: exp(-y**2)
a = 0
b = 2
print("      n      point milieu     trapèze")
for i in range(1, 21):
    n = 2**i
    m = midpoint(g, a, b, n)
    t = trapeze(g, a, b, n)
    print('%7d %.16f %.16f'%(n, m, t))