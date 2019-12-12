## NOM DU PROGRAMME: -----
#% IMPORTATION
n =20
a, b = -2, 3
h = (b - a) / n
xList = []
for i in range(n+1):
    xi  = a + i * h
    xList.append(xi)
print(xList)
xList = [a + i * h for i in range(n+1)]
print(xList)
from numpy import array
xVect = array(xList)
print(xVect)