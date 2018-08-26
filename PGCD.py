import sys
from math import * 
print("CALCUL DE PGCD")
print("A quoi correspond a ? ")
a = int(sys.stdin.readline())  
print("ERROR, you have to write a number")
print("A quoi correspond b ? ")
b = int(sys.stdin.readline()) 
print("ERROR, you have to write a number")


if a > b :  
	reste = a % b 
	if reste != 0 : 
		while True : 
			a = b
			b = reste
			reste = a % b 
			if reste == 0 : 
				break
		print ("Le PGCD est %s" % b)
	else :
		print("Le PGCD est %s" % b )	

	
if b > a :
	reste = b % a  
	if reste != 0:
		while True:
			b = a 
			a = reste 
			reste = b % a 
			if reste == 0:
				break 
		print("Le PGCD est %s" % a)		
	else :
		print("Le PGCD est %s" % a)
	 