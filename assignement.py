

fname = input("Enter file name: ")
fh = open(fname, "r")
lst = list()
liste = [] 

for x in fh:
    line = x.split() 
    lst.append(line) 
    
for x in range(len(lst)):
	liste = lst[x] + liste

liste2 = [] 

for x in range(len(liste)):
	if liste[x] not in liste2:
		liste2.append(liste[x]) 
	elif liste[x] in liste2 :
		pass 



liste2.sort() 
print(liste2)  

