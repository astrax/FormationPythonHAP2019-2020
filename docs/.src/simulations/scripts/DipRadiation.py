## NOM DU PROGRAMME: DipRadiation.py
#% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0,2*np.pi,500)
rho = np.sin(theta)**2
plt.figure()
ax = plt.subplot(111, polar=True)
ax.plot(theta, rho,color='r')
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_rmax(1.0)
ax.set_title("Rayonnement d'un dipole", va='bottom')
theta = np.linspace(0.01,2*np.pi,500)
plt.tight_layout()
plt.savefig("dipole1.png"); plt.savefig("dipole1.pdf")
plt.show()