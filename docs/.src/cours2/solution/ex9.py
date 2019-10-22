from math import sin, cos, pi

def deriv2(x):
    return cos(2*x), -2*sin(2*x), -4*cos(2*x)

f, df, d2f = deriv2(x=pi)

print("f(pi) = {}; f'(pi) = {}; f''(pi) = {} ".format(f, df, d2f))