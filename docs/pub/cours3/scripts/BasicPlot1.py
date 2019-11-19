# Nom Fichier: BasicPlot1.py
# importaion
import matplotlib.pyplot as plt
# definir x
x = [1, 3, 5, 6, 8, 10, 15]
# definir y
y=x
# créer un nouveau graphique
plt.figure()
# Écrire un titre
plt.title("Figure: f(x) = x")
#plot f(x)= x avec: ligne solide ( - ) et marqueurs ( o ) rouges ( r )
plt.plot(x, y, '-ro')
# Écrire un texte (label) sur l'axe des x
plt.xlabel("X-Axis")
# Écrire un texte (label) sur l'axe des y
plt.ylabel("Y-Axis")
#les graphiques ne seront affichés que lorsque vous appelez plt.show ()
plt.show()

