## NOM DU PROGRAMME: DipRadiation3D.py
#% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
import matplotlib.colors as mcolors

def sph2cart(azimuth,elevation,r):
    """
    Convertisseur de Coordonnée Sphérique/Cartésienne
    """
    x = r * np.sin(elevation) * np.cos(azimuth)
    y = r * np.sin(elevation) * np.sin(azimuth)
    z = r * np.cos(elevation)
    return x, y, z
theta = np.linspace(0.001,np.pi,400)
phi = np.linspace(0.001,2*np.pi,400)
THETA, PHI = np.meshgrid(theta,phi)
RHO = np.sin(THETA)**2
X, Y, Z = sph2cart(PHI,THETA,RHO)
fig = plt.figure(figsize=(8,5))
cmap = plt.get_cmap('gnuplot')
ax2 = plt.subplot(111, projection='3d')
ax2._axis3don = False # hide x, y, z axis
norm = mcolors.Normalize(vmin=Z.min(), vmax=Z.max())
ax2.plot_surface(X, Y, Z, rstride=8, cstride=8,
                 facecolors=cmap(norm(Z)), antialiased=True, alpha=0.5)
fig.suptitle("Rayonnement d'un dipole (3D)")
plt.tight_layout()
plt.savefig("dipole1_3D.png"); plt.savefig("dipole1_3D.pdf")
plt.show()