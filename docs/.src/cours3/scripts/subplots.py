# Nom Fichier: subplots.py
# Importation
import matplotlib.pyplot as plt
fig1=plt.figure(figsize=(5, 5))   # Figure
ax1=plt.subplot(211) # premier subplot dans la figure
ax1.plot([1, 2, 3], "-go")
ax1.set_xlabel("x1")
ax1.set_ylabel("y1")
ax1.set_title('subplot 211') # titre du subplot 211
ax2=plt.subplot(212) # deuxième subplot dans la figure
ax2.plot([4, 2, 5], "--k*")
ax2.set_xlabel("x2")
ax2.set_ylabel("y2")
ax2.set_title('subplot 212') # titre du subplot 212

plt.tight_layout() # Ajuster la figure
plt.show()