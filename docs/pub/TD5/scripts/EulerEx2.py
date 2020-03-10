## NOM DU PROGRAMME: EulerEx2.py
#% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt
#Question-a)
def sol_exacte(t, mu, z0):
    return mu - (mu-z0)* np.exp(-t/mu)

mu = 1
z0 = [0, 1, 2]
dt = 0.05
t = np.arange(0, 2, dt)
plt.figure()
for zi in z0:
    plt.plot(t, sol_exacte(t, mu, zi),lw = 2, label= "z0 = " + str(zi))
plt.title("Solution exacte pour mu = 1")
plt.xlabel("Temps [s]")
plt.ylabel("z(t)")
plt.legend()
plt.grid()
plt.savefig("Ex2_solexactemu1.png");plt.savefig("Ex2_solexactemu1.pdf")
plt.show()
#Question-b)
mu = 0.05
plt.figure()
for zi in z0:
    plt.plot(t, sol_exacte(t, mu, zi), lw = 2, label= "z0 = " + str(zi))
plt.title("Solution exacte pour mu = 0.05")
plt.xlabel("Temps [s]")
plt.ylabel("z(t)")
plt.legend()
plt.grid()
plt.savefig("Ex2_solexactemu005.png");plt.savefig("Ex2_solexactemu005.pdf")
plt.show()
#Question-c) - EULER EXPLICITE
z0 = 2
N = len(t)
zexp =np.zeros(N)
zexp[0] = z0
for n in range(N-1):
    zexp[n+1] = zexp[n] + dt*(1- zexp[n]/mu)

#Question-d) - EULER IMPLICITE
zimp =np.zeros(N)
zimp[0] = z0
for n in range(N-1):
    zimp[n+1] = (zimp[n] + dt)/(1+ dt/mu)
#Question-e) - COMPARAISON
plt.figure()
plt.plot(t, sol_exacte(t, mu, z0), lw = 2, label= "solution exacte")
plt.plot(t, zexp, lw = 2, label= "Euler explicite")
plt.plot(t, zimp, lw = 2, label= "Euler implicite")
plt.xlabel("Temps [s]")
plt.ylabel("z(t)")
plt.legend()
plt.grid()
plt.show()
