fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname , "r")
count = {} 
liste = []
liste_des_heures = []

for line in fh:
    if line.startswith("From "):
        words = line.split()
        liste.append(words[5])

for x in range(len(liste)):
    hour = liste[x].split(":")
    liste_des_heures.append(hour[0]) 

for x in liste_des_heures:
	count[x] = count.get(x , 0) + 1


lst = sorted(count.items())

for k,v in lst:
	print(k,v)




