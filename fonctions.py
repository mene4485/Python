import os
from donnees import *
from random import randrange

def nom_hasard():
	global mot
	hasard = randrange(0,21)
	mot = liste[hasard]

bytearray(mot_masque) = ""
for x in range(len(mot)):
	mot_masque += "*" 

def mot_masque():
	while chance != 0 or reussi == True:
		lettre = input("Tapez une lettre: ").lower()
		if lettre in mot:
			pos = mot.find(lettre)
			print("Bravo")
			mot_masque[pos] = lettre
			fois += 1
			if fois == len(mot):
				reussi = True
		else:
			("Dommage")
			chance -= 1
		return mot_masque   	


