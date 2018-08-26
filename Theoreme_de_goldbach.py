n = int ( input ('''              Théorème de Syracuse  
Quel nombre veux-tu ?'''	) )
m = 1 
a = 1
while n != 1: 
	if n % 2 == 0:
		n = n / 2
		print (n)
		m = m + 1
		if n == 1:
			break
		if n > a:
			a = n
	if n % 2 == 1:
		n = 3 * n + 1
		print (n)
		m = m + 1
		if n > a:
			a = n

print ( "Le plus grand nombre est %s et il a %s nombres" %(a,m))
