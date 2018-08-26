import sys
import time

def theoreme_de_pythagore():
	print("Ce logiciel résoud automatiquement le théorème de pythagore")
	time.sleep(3)
	print("Vous avez juste à rentrer les valeurs correspondantes à ton triangle rectangle")
	time.sleep(3)
	print("Vous avez 2 modes : ")
	time.sleep(2)
	print(" - Si vous connaissez le CÔTÉ 1 et le CÔTÉ 2 et vous voulez savoir l'hypothénuse CLIQUEZ SUR 1") 
	time.sleep(5)
	print(" - Si vous connaissez le CÔTÉ 1 et L'HYPOYHÉNUSE et vous voulez savoir le CÔTÉ 2, CLIQUEZ SUR 2")
	nombre_choisi = int(sys.stdin.readline()) 
	if nombre_choisi == 1:
		print("Quel est le coté 1 ? ")
		cote_1= float(sys.stdin.readline())
		print("Quel est le coté 2 ? ")
		cote_2= float(sys.stdin.readline())
		print("L'hypothénuse de ce triangle est égale à ")
		hypothénuse= float(pow(pow(cote_1,2)+pow(cote_2,2),0.5))
		print(hypothénuse)
	if nombre_choisi == 2:
		print("Quel est le coté 1 ? ")
		cote_1= float(sys.stdin.readline())
		print("Quel est l'hypothénuse ? ")
		hypothénuse= float(sys.stdin.readline()) 
		print("Le côté 2 de ce triangle est égale à ")
		cote_2= float(pow(pow(hypothénuse,2)-pow(cote_1,2),0.5))
		print(cote_2)
	if nombre_choisi > 2 or nombre_choisi < 0:
		print("Mettez un chiffre VALIDE")

theoreme_de_pythagore() 