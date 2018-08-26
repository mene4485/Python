
#savoir les n premiers nombres premiers 


n = int(input("Nombre n premier nombre premier : ")) #je demande les n premiers nombres premiers qu'il souhaite
nombre = 5  # déclaration de variable pour plus tard
x = 2   #pareil
m = 0	#pareil

if n < 0:		#juste pour l'amusement
	print("Ok t'es con...") 
if n == 1: 		#premier nombre premier
	print("2")
	n = 0
if n == 2: 		#deux premiers nombres premiers
	print("2\n3")
	n = 0
if n > 2: 		#si l'utilisateur demande plus de deux premiers nombres premiers  
	print("2\n3")
	n = n - 2


while n > 0:
	while x < nombre :  #écrit les calculs sur un papier tu comprendras mieux 
		if nombre % x == 0:
			m = 1
			break
		else:
			x = x + 1

	if m == 0:
		print(nombre)
		n = n - 1

	nombre = nombre + 1
	x = 2
	m = 0

