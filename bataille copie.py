nbPetitPois = int(input())
boite = []

a = 1
b = 0
c = []

while b < nbPetitPois:
	for x in range(a):
		b += x
	c.append( [b , a] )
	b = 0
	a += 1

print( c[ len(c)-2 ]) 


