from math import *
a = int(input('''Quel est le nombre a ?
'''))
b = int(input('''Quel est le nombre b ?
'''))
c = int(input('''Quel est le nombre c ?
'''))
D = b*b - 4*a*c

if D < 0:
	print("Il n'y pas de solutions") 
elif D == 0:
	e = (-b)/(2*a)
	print("La solution est %s" % e)
elif D > 0:
	e = (-b - sqrt(D) )/ 2*a
	f = (-b + sqrt(D) )/ 2*a
	print("Les solutions sont %s et %s" % (e,f))


