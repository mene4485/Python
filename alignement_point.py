
coor_a = input("Coordonnées du point A séparés par un point virgule : ").split(";") 
coor_b = input("Coordonnées du point B séparés par un point virgule : ").split(";") 
coor_c = input("Coordonnées du point C séparés par un point virgule : ").split(";") 

for x in range(len(coor_a)):
	coor_a[x] = int(coor_a[x])

for x in range(len(coor_b)):
	coor_b[x] = int(coor_b[x]) 

for x in range(len(coor_c)):
	coor_c[x] = int(coor_c[x]) 

vecteur_AB_x = coor_b[0] - coor_a[0] 
vecteur_AB_y = coor_b[1] - coor_a[1] 

vecteur_AC_x = coor_c[0] - coor_a[0] 
vecteur_AC_y = coor_c[1] - coor_a[1] 

a = vecteur_AB_y * vecteur_AC_x
b = vecteur_AB_x * vecteur_AC_y

if a == b:
	print("Les points sont alignés")
else :
	print("les points ne sont pas alignés")