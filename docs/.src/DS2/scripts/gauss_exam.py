#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:17:21 2019
GAUSSIENNE
@author: ahmed
"""

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 1/np.sqrt(2*np.pi) * np.exp(-0.5 *x*x)

n = 40
a, b = -4, 4
h = (b - a) / n
xList, fList=[], []

for i in range(n+1):
    xi  = a + i * h
    fi = f(xi)
    xList.append(xi)
    fList.append(fi)

#print(fList)

x = np.linspace(-4, 4, 41)
print(f(x))

plt.plot(x, f(x), 'ko-',lw=2)
plt.title("Fonction gaussienne", fontweight='bold')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.tight_layout()
plt.savefig("gauss.png"); plt.savefig("gauss.pdf")
