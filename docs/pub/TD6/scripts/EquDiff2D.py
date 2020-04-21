## NOM DU PROGRAMME: EquDiff2D.py
#% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt
# taille de la plaque, en [mm]
L = 10.
# intervalles dans les directions x, y, en [mm]
dx = dy = 0.1
# Coefficient de diffusion thermique de l'acier, en [mm2.s-1]
D = 4.
Tfroid, Tchaud = 300, 1000
# Nombre de pas de temps
nsteps = 250
nx, ny = int(L/dx), int(L/dy)
dx2, dy2 = dx*dx, dy*dy
# pas de temps maximum, dans question b)
dt = dx2 * dy2 / (2 * D * (dx2 + dy2))
u = Tfroid * np.ones((nx, ny))
# Conditions initiales - disque de rayon r, centrée sur (cx, cy), en [mm]
r, cx, cy = 2, 5, 5
r2 = r**2
for i in range(nx):
    for j in range(ny):
        p2 = (i*dx-cx)**2 + (j*dy-cy)**2
        if p2 < r2:
            u[i,j] = Tchaud
# Sortie de 4 graphiques à quatre instants dans l'intervalle de temps
mfig = [0, 50, 100, 200]
fignum = 0 # initialisation
fig = plt.figure()
# implémentation du schéma FTCS
for m in range(nsteps):
    for i in range(1, nx-1):
        for j in range(1, ny-1):
            uxx = (u[i+1,j] - 2*u[i,j] + u[i-1,j]) / dx2
            uyy = (u[i,j+1] - 2*u[i,j] + u[i,j-1]) / dy2
            u[i,j] += dt * D * (uxx + uyy)
    if m in mfig:
        fignum += 1
        print(m, fignum)
        ax = fig.add_subplot(220 + fignum)
        im = ax.imshow(u, cmap=plt.get_cmap('hot'), vmin=Tfroid,vmax=Tchaud)
        ax.set_axis_off()
        ax.set_title('{:.1f} ms'.format(m*dt*1000))
fig.subplots_adjust(right=0.85)
cbar_ax = fig.add_axes([0.9, 0.15, 0.03, 0.7])
cbar_ax.set_xlabel('T [K]', labelpad=20)
fig.colorbar(im, cax=cbar_ax)
plt.savefig("EquDiff2D.png"); plt.savefig("EquDiff2D.pdf")
plt.show()
    
