#!/usr/local/bin/python3

from tkinter import *
from tkinter import ttk 
import random 

def bonjour(): 
	print ("Bonjour les merdes")
tk = Tk()
canvas = Canvas(tk, width = 500, height = 500)
canvas.pack() 


def rectangle_aleatoire(largeur, hauteur, couleur):
	x1 = random.randrange(largeur)
	y1 = random.randrange(hauteur)
	x2 = x1 + x1
	y2 = y1 + y1
	canvas.create_rectangle(x1, y1, x2, y2, fill = couleur)

rectangle_aleatoire(400, 400, "red")
tk.mainloop()