## NOM DU PROGRAMME: RK4Ex3.py
#% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt
def RK4(F,t,y,h):
    K0 = h*F(t,y)
    K1 = h*F(t + h/2.0, y + K0/2.0)
    K2 = h*F(t + h/2.0, y + K1/2.0)
    K3 = h*F(t + h, y + K2)
    return (K0 + 2.0*K1 + 2.0*K2 + K3)/6.0
def F(t,y):
    F = np.zeros(4)
    F[0] = y[1]
    F[1] = y[0]*(y[3]**2) - 3.9860e14/(y[0]**2)
    F[2] = y[3]
    F[3] = -2.0*y[1]*y[3]/y[0]
    return F
t = 0
tStop = 1200.0
h = 50.0
y = np.array([7.15014e6, 0.0, 0.0, 0.937045e-3])
T = []
Y = []
T.append(t)
Y.append(y)
while t < tStop:
    y = y + RK4(F,t,y,h)
    t = t + h
    T.append(t)
    Y.append(y)
    
T,Y = np.array(T),np.array(Y)
print("T      Y[0]       Y[1]      Y[2]       Y[3]")
for i in range(len(T)):
    print(T[i], "{:2.4e}".format(Y[i,0]), "{:2.4e}".format(Y[i,1]),
          "{:2.4e}".format(Y[i,2]), "{:2.4e}".format(Y[i,3]))
    
plt.figure(figsize=(8,5))
plt.plot(T, Y[:,0], '-o',lw = 2)
plt.xlabel("temps [s]")
plt.ylabel("r [m]")
plt.axhline(y=6.37814E6, color="k")
# plot point d'impact
plt.plot(1034.184,6.37814E6,'rX')
plt.savefig("Ex3RK4.png"); plt.savefig("Ex3RK4.pdf")
plt.show()
