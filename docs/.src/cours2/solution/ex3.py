devise = input("Devise : ")
montant = int(input ("Montant : "))
# 1 EUR = 3.30 TND
facteur_euro_dinar = 3.30
if devise == 'EUR' :
    print ("{} TND".format(montant * facteur_euro_dinar))
    
elif devise == 'TND' :
    print ("{} Euros".format(montant / facteur_euro_dinar))
    
else :
    print ("Je n'ai rien compris") # affichage d'un message d'erreur