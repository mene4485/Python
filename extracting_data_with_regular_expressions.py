import re

lol = input() 
fh = open(lol,"r")
liste = []

for line in fh:
	y = re.findall("[0-9]+", line)
	if len(y) <= 0: continue
	for x in range(len(y)):
		num = int(y[x])
		liste.append(num)

print(sum(liste)) 
