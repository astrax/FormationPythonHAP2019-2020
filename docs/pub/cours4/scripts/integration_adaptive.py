## NOM DU PROGRAMME: integration_adaptive.py
#% IMPORTATION
from numpy import linspace, zeros, sqrt
from trapeze_integral import trapeze
from midpoint_integral import midpoint

def integration_adaptative(f, a, b, eps, method='midpoint'):
    '''
    Question a)
    '''
    n_limit = 1000000  # Juste un choix (utilisé pour éviter la boucle inf)
    n = 2
    if method == 'trapeze':
        integral_n  = trapeze(f, a, b, n)
        integral_2n = trapeze(f, a, b, 2*n)
        diff = abs(integral_2n - integral_n)
        while (diff > eps) and (n < n_limit):
            integral_n  = trapeze(f, a, b, n)
            integral_2n = trapeze(f, a, b, 2*n)
            diff = abs(integral_2n - integral_n)
            n *= 2
    elif method == 'midpoint':
        integral_n  = midpoint(f, a, b, n)
        integral_2n = midpoint(f, a, b, 2*n)
        diff = abs(integral_2n - integral_n)
        while (diff > eps) and (n < n_limit):
            integral_n  = midpoint(f, a, b, n)
            integral_2n = midpoint(f, a, b, 2*n)
            diff = abs(integral_2n - integral_n)
            n *= 2
    else:
        print('Erreur - intégration adaptative appelée avec un paramètre inconnu')
    # Maintenant, nous vérifions si un n acceptable a été trouvé ou non
    if diff <= eps:   # Succès
        print("L'intégrale calcule: ", integral_2n)
        return n
    else:
        return -n   # Renvoie n négatif pour dire "non trouvé"

def application():
    """Questions b) and c)"""

    g = lambda x: sqrt(x)

#    eps = 1E-1 # Il suffit de basculer entre ces deux valeurs eps
    eps = 1E-10
    a = 0.0 + 0.01  # Si nous ajustons a, sqrt (x) est géré facilement
    b = 2.0
    n = integration_adaptative(g, a, b, eps, 'midpoint')
    if n > 0:
        print('n suffisant est: %d'%(n))
    else:
        print("Aucun n n'a été trouvé dans %d iterations" % (n_limit))
   
    # c) faire un tracé pour le point milieu et les trapèzes
    eps = linspace(1E-1,10E-10,10)
    n_m = zeros(len(eps))
    n_t = zeros(len(eps))
    for i in range(len(n_m)):
        n_m[i] = integration_adaptative(g, a, b, eps[i], 'midpoint')
        n_t[i] = integration_adaptative(g, a, b, eps[i], 'trapeze')

    import matplotlib.pyplot as plt
    plt.figure(figsize=(7,5))
    plt.plot(eps,n_m,'b-', label = "méthode du point milieu")
    plt.plot(eps,n_t,'r-',  label = "méthode des trapèzes")
    plt.xlabel(r'$\epsilon$')
    plt.ylabel('n')
    plt.xscale("log")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    application()