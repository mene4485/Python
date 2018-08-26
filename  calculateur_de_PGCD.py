print ('''      Bienvenue au calculateur de PGCD      ''')
print(' a > b ')
a = int ( input ( '''Quel est le premier nombre ?
''' ) ) 
b = int ( input ( '''Quel est le second nombre ?
''' ) ) 
r =  a % b
c = a
d = b

while r != 0:
	a = b
	b = r
	r = a % b
print ( "%s est le PGCD de %s et %s. " % (b, c, d))



