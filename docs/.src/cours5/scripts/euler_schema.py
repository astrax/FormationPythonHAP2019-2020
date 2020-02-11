## NOM DU PROGRAMME: euler_schema.py
#% IMPORTATION
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('Solarize_Light2')
with plt.xkcd():
    noyaux0 = 100
    tau = 1
    dt = 0.3
    tmax = 2
    nsteps = int(tmax/dt)
    noyaux = np.zeros(nsteps)
    t = np.zeros(nsteps)
    #%% VLEURS INITIALES
    t[0] = 0.0
    noyaux[0] =noyaux0
    #%% BOUCLE PRINCIPALE: MÉTHODE D'EULER
    for i in range(nsteps-1):
        t[i+1] = t[i] + dt
        noyaux[i+1] = noyaux[i] - noyaux[i]/tau*dt
    #%% TRAÇAGE DU GRAPHIQUE
    plt.figure(figsize=(8,5))
    plt.plot(t[:-3], noyaux[:-3],color='b')
    plt.plot(t[:-2], noyaux[:-2],ls="", marker ='o', ms=14, markerfacecolor="red")
    plt.plot(t[-4:], noyaux[-4:],color='r')
    plt.plot(t,noyaux0*np.exp(-(t/tau)), ls ='--', ms=14, color='b')
    plt.annotate("NOUS CONNAISSONS ICI LA PENTE: \nu' = f(u)",
            xy=(t[-4:-3], noyaux[-4:-3]), xycoords='data',
            xytext=(0.8, 60), textcoords='offset points', size=10,
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )
    plt.annotate("SOLUTION EXACTE",
            xy=(t[-2],noyaux0*np.exp(-(t[-2]/tau))), xycoords='data',
            xytext=(0.8, 70), textcoords='offset points', size=10,
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )
    plt.annotate("NOUVEAU POINT PRÉDIT",
            xy=(t[-3:-2], noyaux[-3:-2]), xycoords='data',
            xytext=(-40, -40), textcoords='offset points', size=10,
            arrowprops=dict(arrowstyle="->",
                            connectionstyle="arc3"),
            )
    plt.tight_layout()
    plt.savefig("euler_schema.png")
    plt.savefig("euler_schema.pdf")
        