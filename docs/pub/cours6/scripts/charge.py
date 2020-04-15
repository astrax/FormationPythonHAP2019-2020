## NOM DU PROGRAMME: charge.py
#% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
eps = 1e-5 # erreur fractionnaire autorisée
L = 1.0 # longueur de chaque côté
N = int(input('nombre de points de grille sur un côté -> '))
dz = dy = dx = 2.0*L/(N-1.0)
x = -L + np.array(range(N))*dx
y = -L + np.array(range(N))*dy
z = -L + np.array(range(N))*dz
u = np.zeros((N, N, N))
rho = np.zeros((N, N, N))
# source
q = 1.0
rho[(N-1)//2,(N-1)//2,(N-1)//2] = q/(dx*dy*dz)
# préparer l'animation
s = u[:,:,(N-1)//2]
image = plt.imshow(s.T, origin='lower', extent=(-L, L, -L, L), vmax=1.0)
# calculer le paramètre de sur-relaxation
omega = 2.0/(1.0+np.sin(np.pi*dx/L))
# pixels blancs et noirs: les blancs ont i+j+k pairs; les noirs ont i+j+k impairs
blanc = [(i, j, k) for i in range(1, N-1) for j in range(1, N-1) \
         for k in range(1, N-1) if (i+j+k)%2 == 0]
noir = [(i, j, k) for i in range(1, N-1) for j in range(1, N-1) \
         for k in range(1, N-1) if (i+j+k)%2 == 1]
n = 0 # nombre d'itérations
err = 1.0 # erreur moyenne par site
while err > eps:
    image.set_data(s.T)
    plt.title('itération %d'%n)
    plt.tight_layout()
    plt.show()
    plt.pause(0.001)
    # prochaine itération en raffinement
    n = n+1
    err = 0.0
    # lboucle sur pixels blancs puis pixels noirs
    for (i, j, k) in blanc+noir:
        du = (u[i-1,j,k] + u[i+1,j,k] + u[i,j-1,k] + u[i,j+1,k] + u[i,j,k-1] \
              + u[i,j,k+1] + dx**2*rho[i,j,k])/6.0 - u[i,j,k]
        u[i,j,k] += omega*du
        err += abs(du)
    err /= N**3
# tracé de surface de la solution finale
(x, y) = np.meshgrid(x, y)
s = s.clip(eps, 1.0)
levels = [10**(l/2.0) for l in range(-5, 0)]
fig = plt.figure()
axis = fig.gca(projection='3d', azim=-60, elev=20)
surf = axis.plot_surface(x, y, s.T, rstride=1, cstride=1, cmap='viridis')
wire = axis.plot_wireframe(x, y, s.T, rstride=1+N//50, cstride=1+N//50,
                           color = "r", linewidth=0.5, alpha = 0.5)
axis.contour(x, y, s.T, levels, zdir='z', offset=-1.0)
axis.contourf(x, y, s.T, 4, zdir='x', offset=-L)
axis.contourf(x, y, s.T, 4, zdir='y', offset=L)
axis.set_zlim(-1.0, 1.0)
axis.set_xlabel('x')
axis.set_ylabel('y')
axis.set_zlabel('u')
fig.colorbar(surf)
plt.tight_layout()
plt.savefig("charge.png"); plt.savefig("charge.pdf")
plt.show()