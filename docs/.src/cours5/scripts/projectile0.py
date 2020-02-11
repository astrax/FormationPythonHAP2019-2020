## NOM DU PROGRAMME: projectile.py
#%% IMPORTATION
import numpy as np
import matplotlib.pyplot as plt
#%% ENTRÉES
# constante de pesenteur (m/s^2)
g = 9.8 
# angles de lancement (degrés)
angles = np.arange(30, 55, 5)
# pas de temps
dt = 0.01
#%% VLEURS INITIALES
v0 = 10.0 
N = 1000
x = np.zeros(N)
y = np.zeros(N)
vx = np.zeros(N)
vy = np.zeros(N)

for theta in angles:
    vx[0] = v0 * np.cos(theta*np.pi/180.0)
    vy[0] = v0 * np.sin(theta*np.pi/180.0)
#    print(vx[0])
#    i=0
#    while y[i] >= 0:
##        print(y[i])
##        print(x)
#        x[i+1] = x[i] + vx[i] * dt
#        y[i+1] = y[i] + vy[i] * dt
#        vx[i+1] = vx[i]
#        vy[i+1] = vy[i] - g * dt
#        i = i+1
    x[0], y[0]=0, 1
    for i in range(N-1):
        
        x[i+1] = x[i] + vx[i] * dt
        y[i+1] = y[i] + vy[i] * dt
        vx[i+1] = vx[i]
        vy[i+1] = vy[i] - g * dt
        
    plt.plot(x, y,'-', label=str(theta)+' degrees')
        
# Prettify the plot
plt.xlabel('Horizontal distance, [m]')
plt.ylabel('Vertical distance, [m]')
plt.title('Trajectory of a fired cannonball')
plt.grid()
plt.legend()
plt.axis([0, 13, 0, 6])

# Makes the plot appear on the screen
plt.show()
    

#for k in range(len(angles)):
#    plt.plot(x, y, label=str(angles[k])+' degrees')
#        
#    
    
#for theta in angles:
#    x = [0.0]
#    y = [0.0]
#    vx = [v0*np.cos(theta*np.pi/180.0)]
#    vy = [v0*np.sin(theta*np.pi/180.0)]
##    print(vx)
#    # use Euler’s method to integrate projectile equations of motion
#    i = 0
#    while y[i] >= 0.0:
#        # extend the lists by appending another point
#        x += [0.0]
#        y += [0.0]
#        vx += [0.0]
#        vy += [0.0]
#        # apply finite difference approx to equations of motion
#        x[i+1] = x[i]+vx[i]*dt
#        y[i+1] = y[i]+vy[i]*dt
#        vx[i+1] = vx[i]
#        vy[i+1] = vy[i] - g*dt
#        i = i+1
#        
#    # plot the trajectory
#    plt.plot(x, y, label=str(theta)+' degrees')