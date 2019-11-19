def EqSecondDegree(a,b,c):
    # %load solution/ex4
    """
    Calcul des racines de l'equation du second degré:
    a x^2 + b x + c = 0
    """
    from math import sqrt

    delta = b**2 - 4*a*c  #Calcul du discriminant:

    #Resultats des racines suivant la valeur de delta:
    if delta > 0:
        x1 = (-b - sqrt(delta))/(2*a)
        x2 = (-b + sqrt(delta))/(2*a)
        return x1, x2

    elif delta == 0:
        x0 = -b/(2*a)
        return x0

    elif delta<0:
        z1 = (-b - 1j*sqrt(-delta))/(2*a)
        z2 = (-b + 1j*sqrt(-delta))/(2*a)
        return z1, z2
