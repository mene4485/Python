from tkinter import*
import random 
import time
tk = Tk() 

tk.title("Rebondir")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 0)
canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.pack() 
tk.update() 


class Balle:
	def __init__(self, canvas, couleur):
		self.canvas = canvas
		self.id = canvas.create_oval(10, 10, 25, 25, fill = couleur)
		self.canvas.move(self.id, 245, 100)

	def dessiner(self):
		pass


tk.mainloop() 