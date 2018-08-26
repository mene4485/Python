joueur = {}
j1 = input("Inséré le nom du joueur 1: ")
j2 = input("Inséré le nom du joueur 2: ")
joueur[j1] = 0
joueur[j2] = 0
taille = int(input("Quel est la taille de la grille ? "))

gagnant = False
a = 0
nba = None
utiliser = []
while gagnant == False:
	for x in range(1 , taille**2 + 1):
		if x not in utiliser:
			print(x , end=" "* (3-len(str(x))))
		else:
			print("X" , end=" "* (3-len(str(x))))
		if x % taille == 0:
			print()

	if a % 2 == 0:
		nb = int(input("{} , inséré votre nombre: ".format(j1)))
	if a % 2 == 1:
		nb = int(input("{} , inséré votre nombre: ".format(j2)))
	
	if 0 > nb > x:
		nb = int(input("Votre nombre n'est pas dans la grille. Veuillez réesayer:"))

	if nba != None:
		if nb % nba == 0 or nba % nb == 0:
			if nb not in utiliser:
				utiliser.append(nb)
			else:
				print("Perdu, ce nombre a deja ete utiliser")
				gagnant = True
		else:
			print("Perdu, ce nombre n'est pas un multiple / diviseur de {}".format(nba))
			gagnant = True
	else:
		utiliser.append(nb)
	print()
	nba = nb
	a += 1
if a % 2 == 0:
	print("{} a gagné !!!".format(j1))
if a % 2 == 1:
	print("{} a gagné !!!".format(j2))