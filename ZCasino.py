from random import randrange
from math import ceil
print()
print('''                Bienvenue dans le ZCasino !!!
Vous avez 1000$. Je vous explique les règles. Vous devez miser 
un nombre entre 0 et 49. Puis vous donnez une somme d\'argent. Le 
croupier lance une bille. Si elle atterit sur ton nombre tu gagnes trois
fois la mise. Les cases paires sont noires et les impaires sont rouges.
Si ton nombre est de la meme couleur que le nombre ou la bille est tombée
tu gagnes 50% de ta mise. Sinon tu perds ta mise. ''')
print()
argent = 1000
nombre_miser = -1
somme = -1

while True:
	nombre_miser = -1
	somme = -1
	while nombre_miser < 0 or nombre_miser > 49:
		try: 
			nombre_miser = int ( input ( "Quel nombre entier compris entre 0 et 49 mises-tu? "))
		except ValueError:
			print("Ton nombre comporte des virgules")
			nombre_miser = -1
		
		if nombre_miser < 0 or 49 < nombre_miser: 
			print("Votre nombre n'est pas compris entre 0 et 49")
			nombre_miser = -1

		if 0 < nombre_miser < 49 :
			break

	while somme <= argent or somme > 0:
		try:
			somme = int ( input ( " Quelle somme entier mises-tu? "))
		except ValueError:
			print("La somme doit être entier")
		
		if somme > argent:
			print("Tu n'as pas assez d'argent.")
		
		if somme < 0:
			print("La somme ne peut pas etre négative.")

		if 0 < somme <= argent :
			break

	roulette = randrange(50)
	print("La bille est sur le nombre %s ." % roulette )
	if roulette == nombre_miser:
		print ("Bravo! Tu gagnes %s $." % somme*3)
		argent += somme * 3
	
	if roulette % 2 == nombre_miser % 2:
		e = ceil(somme/2)
		print ("Tu gagnes %s $." % e)
		argent += e
	
	else:
		print ("Dommage! Tu perds %s $." % somme)
		argent -= somme
	print("Tu as %s $" % argent)
	print()
	if argent <= 0:
		print("Vous n'avez plus d'argent.")
		break















