import time
import matplotlib.pyplot as plt 
n = int (input ('''Jusqu'à quel nombre n veux-tu savoir de nombres premiers ? ''' ))
nombre = 0
liste_premier=[]
p = 1
if n != 0:
	liste_premier.append(1)
	nombre = nombre + 1

for x in range ( 2 , n):
	foutu = 0
	a=2
	while (a < x):
		if x % a == 0:
			foutu = 1
		a=a+1    
			
	if (foutu==0):
		liste_premier.append(x)
		nombre = nombre + 1
print (liste_premier)



absc=[k for k in range(1,n)]
ordo=[nombre/absc for k in range(0,1)]

plt.plot(absc, ordo)
plt.show()

