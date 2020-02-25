## NOM DU PROGRAMME: DipRadiationGeneral.py
#% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d

def rho(theta, rapport = 0.5):
    u = rapport* np.pi
    F = (np.cos(u*np.cos(theta)) - np.cos(u))/(np.sin(theta))
    G = F * F
    return G/G.max() 

plt.figure()
ax = plt.subplot(111, polar=True)
plt.title("Rayonnement d'une antenne dipolaire de longueur L")
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_rmax(1.0)
theta = np.linspace(0.01,2*np.pi,500)

for rapport in [0.5,1.0,1.5, 2]:
    ax.plot(theta,rho(theta, rapport), lw = 2,
            label=r"$L/\lambda=%.1f$"%rapport, alpha=0.75)
plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig("dipole.png"); plt.savefig("dipole.pdf")
plt.show()

#% Dipôle 3D
Theta = np.linspace(0.001,np.pi,400)
Phi = np.linspace(0.001,2*np.pi,400)
THETA, PHI = np.meshgrid(Theta,Phi)
# 
def sph2cart(azimuth,elevation,r):
    """
    Convertisseur de Coordonnée Sphérique/Cartésienne
    """
    x = r * np.sin(elevation) * np.cos(azimuth)
    y = r * np.sin(elevation) * np.sin(azimuth)
    z = r * np.cos(elevation)
    return x, y, z

import matplotlib.colors as mcolors
fig = plt.figure(figsize=(8,5))
cmap = plt.get_cmap('gnuplot')
rapport = 1.4
X, Y, Z = sph2cart(PHI,THETA,rho(THETA,rapport))
#ax1 = plt.subplot(121, polar=True)
#ax1.plot(theta,rho(theta, rapport), lw = 2)
#ax1.set_theta_zero_location('N')
#ax1.set_theta_direction(-1)
ax2 = plt.subplot(111, projection='3d')
ax2._axis3don = False # hide x, y, z axis
norm = mcolors.Normalize(vmin=Z.min(), vmax=Z.max())
ax2.plot_surface(X, Y, Z, rstride=8, cstride=8,
                 facecolors=cmap(norm(Z)), antialiased=True, alpha=0.5)
fig.suptitle("Diagramme de rayonnement: "+r"$L/\lambda=%.1f$"%rapport)
plt.tight_layout()
plt.savefig("dipole3D_w14.png"); plt.savefig("dipole3D_w14.pdf")