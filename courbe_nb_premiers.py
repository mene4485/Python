


n = int(input("Nombres premiers jusqu'à n : ")) #je demande les n premiers nombres premiers qu'il souhaite
x = n
nombre = 0
module = 2
m = 0

while n <= x : 
	if nombre % module == 0:
		m = 1
		nombre = nombre + 1
		print(nombre)
	else:
		n = n - 1
		module = module + 1

	
