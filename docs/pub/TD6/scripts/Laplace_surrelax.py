## NOM DU PROGRAMME: Laplace_surrelax.py
#% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
eps = 1e-5 # erreur fractionnaire autorisée
L = 1.0 # longueur de chaque côté
N = int(input('nombre de points de grille sur un côté -> '))
dy = dx = L/(N-1.0)
x = np.array(range(N))*dx
y = np.array(range(N))*dy
(x, y) = np.meshgrid(x, y)
u = np.zeros((N, N))
# conditions aux limites
for j in range(N):
    u[j,N-1] = 1.0
# calculer le paramètre de sur-relaxation
omega = 2.0/(1.0+np.sin(np.pi*dx/L))
# pixels blancs et noirs: les blancs ont j+k pairs; les noirs ont j+k impairs
blanc = [(j, k) for j in range(1, N-1) for k in range(1, N-1) if (j+k)%2 == 0]
noir = [(j, k) for j in range(1, N-1) for k in range(1, N-1) if (j+k)%2 == 1]
# préparer l'animation
image = plt.imshow(u.T, origin='lower', extent=(0.0, L, 0.0, L))
n = 0 # nombre d'itérations
err = 1.0 # erreur moyenne par site
while err > eps:
    # mettre à jour le tracé animé
    image.set_data(u.T)
    plt.title('itération %d'%n)
    plt.tight_layout()
    plt.show()
    plt.pause(0.001)
    # prochaine itération en raffinement
    n = n+1
    err = 0.0
    for (j, k) in blanc+noir: # boucle sur pixels blancs puis pixels noirs
        du = (u[j-1,k]+u[j+1,k]+u[j,k-1]+u[j,k+1])/4.0-u[j,k]
        u[j,k] += omega*du
        err += abs(du)
    err /= N**2
# tracé de surface de la solution finale
fig = plt.figure()
axis = fig.gca(projection='3d', azim=-60, elev=20)
surf = axis.plot_surface(x, y, u.T, rstride=1, cstride=1, cmap='viridis')
wire = axis.plot_wireframe(x, y, u.T, rstride=1+N//50, cstride=1+N//50,
                           color = "r", linewidth=0.5, alpha = 0.5)
axis.contour(x, y, u.T, 10, zdir='z', offset=-1.0)
axis.set_xlabel('x')
axis.set_ylabel('y')
axis.set_zlabel('u')
axis.set_zlim(-1.0, 1.0)
fig.colorbar(surf)
plt.tight_layout()
plt.savefig("Laplace_surrelax.png"); plt.savefig("Laplace_surrelax.pdf")
plt.show()


    
    
    





