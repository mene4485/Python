from random import randrange
nb = randrange(1 , 100)
coup = 0
a = -1
while a != nb:
	a = int(input("Insere ton nombre: "))
	coup += 1
	if a > nb:
		print("Plus bas")
	elif a < nb:
		print("Plus haut")
	if a == nb:
		break
print("Tu l'as fais en {} coups.".format(coup))