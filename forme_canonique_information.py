#ce programme cherche la variable manquante dans une équation de forme canonique

import sys
print("(écrivez le numéro qui vous correspond)")
print("Quelle inconnue chercher vous: a(1), x(2), alpha(3) , beta(4) ou le résultat(5)?")
demande = int(input()) 

def information():
	if a < 0:
		print("La fonction est tournée vers le bas et son maximum a pour coordonnée (%s ; %s)"  % (alpha,beta))
	if a > 0:
		print("La fonction est tournée vers le haut et son minimum a pour coordonnée (%s ; %s)"  % (alpha,beta))


if demande == 1:
	print("Cependant vous devez me donner les autres variables")
	print("Nombre X ?")
	x = int(input()) 
	print("Alpha ?")
	alpha = int(input()) 
	print("Beta ?")
	beta = int(input()) 
	print("Résultat ?")
	resultat = int(input()) 
	a = round((resultat-beta)/((x-alpha)**2),2) 
	print("A = %s" % a)
	information() 
	


if demande == 2:
	print("Cependant vous devez me donner les autres variables")
	print("Nombre A ?")
	a = int(input()) 
	print("Alpha ?")
	alpha = int(input()) 
	print("Beta ?")
	beta = int(input()) 
	print("Résultat ?")
	resultat = int(input()) 
	x = round((((resultat-beta)/a)**0.5+alpha),2) 
	print ("X = %s" % x)
	information() 


if demande == 3:
	print("Cependant vous devez me donner les autres variables")
	print("Nombre A ?")
	a = int(input()) 
	print("Nombre X ?")
	x = int(input()) 
	print("Beta ?")
	beta = int(input()) 
	print("Résultat ?")
	resultat = int(input()) 
	alpha = round((x - ((resultat-beta)/a)**0.5),2)
	print("Alpha = %s" % alpha)
	information() 

if demande == 4:
	print("Cependant vous devez me donner les autres variables")
	print("Nombre A ?")
	a = int(input()) 
	print("Nombre X ?")
	x = int(input()) 
	print("Alpha ?")
	alpha = int(input()) 
	print("Résultat ?")
	resultat = int(input())
	beta = round((-a*((x-alpha))**2+resultat),2)
	print("Beta = %s" % beta)
	information() 

if demande == 5:
	print("Cependant vous devez me donner les autres variables")
	print("Nombre A ?")
	a = int(input()) 
	print("Nombre X ?")
	x = int(input()) 
	print("Alpha ?")
	alpha = int(input()) 
	print("Beta ?")
	beta = int(input()) 
	resultat = round((a*((x-alpha)**2)+ beta),2)
	print("Resultat = %s" % resultat)
	information() 
	
	