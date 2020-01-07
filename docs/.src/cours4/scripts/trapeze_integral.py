## NOM DU PROGRAMME: trapeze_integral.py
def trapeze(f, a, b, n):
    h = (b-a)/n
    result = 0.5*f(a) + 0.5*f(b)
    for i in range(1, n):
        xi = a + i*h
        result += f(xi)
    result *= h
    return result

def application():
    from math import exp
    v = lambda t: 3*(t**2)*exp(t**3)
    n = int(input('n: '))
    numerical = trapeze(v, 0, 1, n)

    # Comparer avec le résultat exact
    V = lambda t: exp(t**3) - 1
    exact = V(1) - V(0)
    print(exact)
    error = exact - numerical
    print('n=%d: %.16f, erreur: %g' % (n, numerical, error))

if __name__ == '__main__':
    application()