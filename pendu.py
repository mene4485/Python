import random
from tkinter import *
import time
tk = Tk()
part = int(input("Combien de parties voulez vous faire? "))

def fa(coup):
	if coup == 7:
		canvas.create_line(50,245,300,245)
		canvas.create_line(125,245,125,50)
	if coup == 6:
		canvas.create_line(125,50,225,50)
		canvas.create_line(225,50,225,70)
	if coup == 5:
		canvas.create_oval(205 , 70 , 245, 110 , fill = 'pink')
	if coup == 4:
		canvas.create_line(225 , 110 , 225, 175)
	if coup == 3:
		canvas.create_line(225 , 120 , 175, 105)
	if coup == 2:
		canvas.create_line(225 , 120 , 275, 105)
	if coup == 1:
		canvas.create_line(225 , 175 , 190, 200)
	if coup == 0:
		canvas.create_line(225 , 175 , 260, 200)


score = 0
canvas = Canvas(tk, width = 400, height = 400)
canvas.pack()

for x in range(part):
	coup = 8
	lieu_al = random.randrange(0 , len(liste))
	mot = liste[lieu_al]
	mot_masque = []
	reussi = False
for x in mot:
	mot_masque.append("_")
	faux = []
	o = canvas.create_text(175 , 300 , text=mot_masque , 
	font=('Times', 24))
	q = canvas.create_text(10 , 100 , text=faux , 
	font=('Times', 24))
	print()
while coup > 0:
	lettre = input("Votre lettre est: ")
	while True:
		if len(lettre) > 1 or lettre==" " :
			lettre = input("Veuillez ressaisir votre lettre: ")
		elif lettre in mot_masque or lettre in faux:
			lettre = input("Vous avez déjà ecrit cette lettre. Veuillez ressaisir votre lettre: ")
		elif lettre.isalpha() == False:
			lettre = input("Vous devez écrire une lettre. Veuillez ressaisir votre lettre: ")
		else:
			break
		re = None
		for x in range(len(mot)):
		if lettre == mot[x]:
		mot_masque[x] = lettre
		re = True
		if re == None:
		faux.append(lettre)
		canvas.delete(q)
		q = canvas.create_text(175 , 350 , text=faux , font=('Lobster', 24))
		coup -= 1
		fa(coup)

canvas.delete(o)
o = canvas.create_text(175 , 300 , text=mot_masque , font=('Times', 24))

if "".join(mot_masque) == mot:
	canvas.create_text(200 , 20 , text="Bravo!" , font=('Nunito', 40))
	canvas.delete(o)
	o = canvas.create_text(175 , 300 , text=mot , font=('Times', 24))
	time.sleep(2)
	canvas.delete(o)
	time.sleep(2)
	canvas.delete(q)
	canvas.delete("all")
break
if coup == 0:
	canvas.create_line(225 , 175 , 260, 200)