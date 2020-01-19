## NOM DU PROGRAMME: midpoint_integral.py
def midpoint(f, a, b, n):
    h = float(b-a)/n
    result = 0
    for i in range(n):
        xi = (a + h/2.0) + i*h
        result += f(xi)
    result *= h
    return result

def application():
    from math import exp
    v = lambda t: 3*(t**2)*exp(t**3)
    n = int(input('n: '))
    numerical = midpoint(v, 0, 1, n)

    # Comparer avec le résultat exact
    V = lambda t: exp(t**3) - 1
    exact = V(1) - V(0)
    error = exact - numerical
    print('n=%d: %.16f, erreur: %g' % (n, numerical, error))

if __name__ == '__main__':
    application()