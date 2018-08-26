
#organiser une liste par ordre croissant

liste = []  #création d'une liste 
while True: 
	try:
		x = input("Enter a number : ") #l'utilisateur rempli la liste par lui-même
		if x == "done": #si il met "done" ça veut dire que sa liste est finie
			break
		liste.append(int(x))  
	except:
		print("Invalid Syntax")

liste2 = sorted(liste) #organise les nombres par ordre croissant
print("Voici votre liste par ordre croissant : ", liste2)
	

