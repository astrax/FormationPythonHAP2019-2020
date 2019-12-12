#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 16:59:56 2019
viscosité de l’eau
@author: ahmed
"""
import matplotlib.pyplot as plt
import numpy as np

def mu(T, A, B, C):
    return A*10**(B/(T-C))

# 0 deg C = 273 deg K
T = np.linspace(0, 100, 20)

plt.plot(T, mu(T+273, A = 2.414e-5, B = 247.8, C = 140), 'k^--')
plt.title("Évolution de la viscosité de l'eau avec la température",
          fontweight='bold')
plt.xlabel("Température (degrés Celsius)")
plt.ylabel("Viscosité (Pa s)")
plt.grid()
plt.savefig("viscosity.png"); plt.savefig("viscosity.pdf")
