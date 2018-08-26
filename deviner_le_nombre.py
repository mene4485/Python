import random 

print("Mode 1 - Contre l'ordi")
print("Mode 2 - Deux joueurs")
reponse = input("Choisissez un des deux modes : ")

if reponse == '1' : 
	print("Devinez le nombre compris entre 0 et 100")
	nombre = random.randint(0 , 100)
	while True:
		num = int(input("Entrez un nombre :"))
		if num > nombre :
			print("Plus Bas")
		elif num < nombre : 
			print("Plus haut")
		elif num == nombre:
			print("BRAVO !!")
			break 

if reponse == '2' : 
	nombre = int(input("Joueur 1 , entrez un nombre : "))
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	coups1 = 0
	while True:
		num = int(input("Entrez un nombre entre 1 et 100 :"))
		if num > nombre :
			print("Plus Bas")
			coups1 = coups1 + 1
		elif num < nombre : 
			print("Plus haut")
			coups1 = coups1 + 1
		elif num == nombre:
			print("BRAVO !!")
			coups1 = coups1 + 1
			break 
	print("\nMaintenant changez de place : Joueur 1 devient joueur 2 et vice versa")
	nombre = int(input("Joueur 1 , entrez un nombre : "))
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	coup2 =0
	while True:
		num = int(input("Entrez un nombre entre 1 et 100 :"))
		if num > nombre :
			print("Plus Bas")
			coup2 = coup2 + 1
		elif num < nombre : 
			print("Plus haut")
			coup2 = coup2 + 1
		elif num == nombre:
			print("BRAVO !!")
			coup2 = coup2 + 1
			break 

	if coups1 < coup2:
		print("Joueur 1 gagne avec %s coups" % coups1)
		print("Joueur 2 perd avec %s coups" % coup2)
	elif coup2 < coups1:
		print("Joueur 2 gagne avec %s coups" % coup2)
		print("Joueur 1 perd avec %s coups" % coups1)




