def EqSecondDegree(a,b,c):
    # %load solution/ex4
    """
    Calcul des racines de l'equation du second degré:
    a x^2 + b x + c = 0
    """
    from math import sqrt

    print("L'équation a resoudre est: {} x^2 + {} x + {}".format(a,b,c))

    delta = b**2 - 4*a*c  #Calcul du discriminant:

    #Resultats des racines suivant la valeur de delta:
    if delta > 0:
        x1 = (-b - sqrt(delta))/(2*a)
        x2 = (-b + sqrt(delta))/(2*a)
        # Affichage des solutions trouvées
        print("Les solutions sont réelles: ")
        print("La premiere racine est x1= ",x1)
        print("La seconde racines est x2= ",x2) 
        return x1, x2

    elif delta == 0:
        x0 = -b/(2*a)
        # Affichage de la solution trouvée
        print("Il y a une seule solution: ")
        print("La solution est", x0)
        return x0

    elif delta<0:
        z1 = (-b - 1j*sqrt(-delta))/(2*a)
        z2 = (-b + 1j*sqrt(-delta))/(2*a)
        # Affichage des solutions trouvées
        print("Les solutions sont complexes: ")
        print("La premiere racine est z1 = ", z1)
        print("La seconde racine est z2 = ", z2)
        return z1, z2
