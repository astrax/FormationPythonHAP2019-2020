# Nom Fichier: BasicText.py
# Importation
import matplotlib.pyplot as plt

fig = plt.figure()
fig.suptitle('Sous-titre de la figure en gras', fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_title('titre des axes')

ax.set_xlabel('xlabel')
ax.set_ylabel('ylabel')

ax.text(3, 8, 'texte en italique encadré par les données', style='italic',
        bbox={'facecolor':'blue', 'alpha':0.5, 'pad':10})

ax.text(2, 6, r'Une équation: $E=mc^2$', fontsize=15)


ax.text(0.95, 0.01, "texte en couleur sur l'axe des x",
        verticalalignment='bottom', horizontalalignment='right',
        transform=ax.transAxes,
        color='red', fontsize=14)

ax.plot([2], [1], 'o')

ax.annotate('annotation: point M(2,1)', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.axis([0, 10, 0, 10])
plt.grid()
plt.show()