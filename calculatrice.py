# calculatrice

from tkinter import*
nb1 = ""

def ajout(nb): 
	global nb1
	nb1 = nb1 + nb
	label["text"] = nb1 

def num1():
	ajout("1")

def num2():
	ajout("2")

def num3():
	ajout("3")

def num4():
	ajout("4")

def num5():
	ajout("5")

def num6():
	ajout("6")

def num7():
	ajout("7")

def num8():
	ajout("8")

def num9():
	ajout("9")

def zero():
	ajout("0")

def point():
	ajout(".")


def clear():
	global nb1
	nb1 = ""
	label["text"] = nb1
	
def add():
	global nb1, op, nb2
	nb2 = float(nb1)
	nb1 = ""
	op = 1
	label["text"] = "+"

def minus():
	global nb1, op, nb2
	nb2 = float(nb1)
	nb1 = ""
	op = 2
	label["text"] = "-"

def times():
	global nb1, op, nb2
	nb2 = float(nb1)
	nb1 = ""
	op = 3
	label["text"] = "x"

def equal():
	global nb1
	nb1 = float(nb1)
	if op == 1:
		result = round(nb2 + nb1,4) 
	if op == 2:
		result = round(nb2 - nb1,4)
	if op == 3: 
		result = round(nb2 * nb1,4)

	label["text"] = result
	nb1 = str(result)


tk = Tk() 
tk.title("Calculatrice")

label = Label(tk, text = "0", font = ("Times" , 30))
label.place(x = 10, y = 10)
label.pack(side = TOP) 

canvas = Canvas(tk, width = 280, height = 250)
canvas.pack() 

button = Button(tk, text = "   1   ", font = ("Times" , 30), command = num1).place(x = 10,y = 200)
button = Button(tk, text = "   2   ", font = ("Times" , 30), command = num2).place(x = 80,y = 200)
button = Button(tk, text = "   3   ", font = ("Times" , 30), command = num3).place(x = 150,y = 200)
button = Button(tk, text = "   4   ", font = ("Times" , 30), command = num4).place(x = 10,y = 150)
button = Button(tk, text = "   5   ", font = ("Times" , 30), command = num5).place(x = 80,y = 150)
button = Button(tk, text = "   6   ", font = ("Times" , 30), command = num6).place(x = 150,y = 150)
button = Button(tk, text = "   7   ", font = ("Times" , 30), command = num7).place(x = 10,y = 100)
button = Button(tk, text = "   8   ", font = ("Times" , 30), command = num8).place(x = 80,y = 100)
button = Button(tk, text = "   9   ", font = ("Times" , 30), command = num9).place(x = 150,y = 100)
button = Button(tk, text = "   0   ", font = ("Times" , 30), command = zero).place(x = 10,y = 250)
button = Button(tk, text = "   .   ", font = ("Times" , 30), command = point).place(x = 80,y = 250)

button = Button(tk, text = "   C  ", font = ("Times" , 30), command = clear).place(x = 150,y = 250)
button = Button(tk, text = "  +  ", font = ("Times" , 30), command = add).place(x = 220,y = 100)
button = Button(tk, text = "  -  ", font = ("Times" , 35), command = minus).place(x = 220,y = 150)
button = Button(tk, text = "  x  ", font = ("Times" , 30), command = times).place(x = 220,y = 200)
button = Button(tk, text = "  =  ", font = ("Times" , 30), command = equal).place(x = 220,y = 250)


tk.mainloop() 