#!/usr/local/bin/python3

from tkinter import *
import tkinter.messagebox 
import time 
tk = Tk()
reponse = tkinter.messagebox.askquestion("Question 1", "Did the World War 2 started in 1939 ?")
my_image = PhotoImage(file = '/Users/meneliknouvellon/Downloads/diappointed.gif')
my_real_image = my_image.zoom(2,2)  
my_image2 = PhotoImage(file = "/Users/meneliknouvellon/Downloads/goodjob.gif") 



if reponse == "yes": 
	canvas = Canvas(tk, width = 500, height = 500)
	canvas.pack() 
	canvas.create_text(150, 100, text = "Good Job", fill = "green", font = ("Zapfino", 40))
	canvas.create_image(50, 150, anchor = NW, image = my_image2)  

if reponse == "no": 
	canvas = Canvas(tk, width = 500, height = 500)
	canvas.pack() 
	canvas.create_text(250, 100, text = "You have to check out your history classes...", fill = "red", font = ("Herculanum", 20))
	canvas.create_image(50, 150, anchor = NW, image = my_real_image) 
 
 
tk.mainloop() 

