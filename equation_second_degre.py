#ce programme résout une éqution du second degré

# import sys
# import matplotlib.pyplot as plt  

# def g(x):
#     '''la fonction qu'on veut représenter'''
#     return(a*x*x-b*x+c)
 
# def graphe(f,a,b,N):
#     '''trace le graphe de la fonction f entre a et b avec N segments'''
#     lx = [a+i*(b-a)/N for i in range(N+1)]
#     ly = [f(x) for x in lx]
#     plt.plot(lx,ly)
#     plt.show() 

# print("Nombre A ?") 
# a = int(sys.stdin.readline())
# print("Nombre B ?") 
# b = int(sys.stdin.readline()) 
# print("Nombre C ?") 
# c = int(sys.stdin.readline())
# delta = b*b-4*a*c
# print("Delta = %s" % delta)

# if delta < 0 :
# 	print("Il n'y a pas de solution pour cette équation")
# if delta == 0:
# 	solution = round(-b/(2*a),2)
# 	print("La seule solution de cette équation est %s" % solution)
# if delta > 0:
# 	solution1 = round((-b-(delta**0.5))/(2*a),2)
# 	solution2 = round((-b+(delta**0.5))/(2*a),2)
# 	print("Les solutions de cette équation sont %s et %s" % (solution1,solution2))

 
# # programme principal
# graphe(g,-10,0,100)

import turtle
from tkinter import*
from math import*
 
#controle des parametres donnés par l'utilisateur
def controle(a,b,c):
    delta = b**2 - 4*a*c
    if a ==0:
        suite=0
        fen2=Tk()
        tex2=Label(fen2,text='cette fonction nest pas une fonction polynome du second dergres, A doit etre different de 0',fg='red')
        tex2.pack(side=TOP)
        bouton=Button(fen2,text='OK',command=fen2.destroy)
        bouton.pack()
        fen2.mainloop()
    else:
        suite=1
        extremum = -delta/(4*a)
        if extremum<-20 or extremum>20:
            suite=0
            fen2=Tk()
            tex2=Label(fen2,text='Extremum doit être compris entre -20 et 20.',fg='red')
            tex2.pack(side=TOP)
            bouton=Button(fen2,text='OK',command=fen2.destroy)
            bouton.pack()
            fen2.mainloop()
        else:
            suite=1
        return(suite)
 
# trace d'une droite avec les coordonnees de débuts et de fin --> axes
def drawLine (ttl, x1, y1, x2, y2):
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()
 
  # affichage des points sur le graphiques--> dessine les absices et ordonnées
def labelPoint (ttl, x, y, label):
  ttl.penup()
  ttl.goto (x, y)
  ttl.pendown()
  ttl.write (label)
  ttl.penup()
   
#trace des droites du repère
def drawGridMark (ttl, x, y, isVertical):
  if isVertical :
    drawLine (ttl, x, y + 5, x, y - 5)
  else:
    drawLine (ttl, x - 5, y, x + 5, y)
     
#place les points sur les axes
def labelGridPoint (ttl, x, y, isVertical, text):
  if isVertical:
    labelPoint (ttl, x - 20, y - 20, text)
  else:
    labelPoint (ttl, x + 20, y, text)
 
def drawGridScaled (ttl):
  # dessines les axes
  drawLine (ttl, -400, 0, 400, 0)
  drawLine (ttl, 0, 400, 0, -400)
 
  # ecrire les points sur l'axe x
  for x in [-400,-300,-200, -100, 100, 200, 300, 400]:
    drawGridMark (ttl, x, 0, True)
    #placement en fonction de l'echelle
    labelGridPoint (ttl, x, 0, True, (x/echelle(), 0))
 
  # ecrire les points sur l'axe y
  for y in [-400,-300,-200, -100,100 , 200,300,400]:
    drawGridMark (ttl, 0, y, False)
    #placement en fonction de l'echelle
    labelGridPoint (ttl,0, y, False, (0, y/echelle()))
 
#calcul de l'echelle en fonction de l'extremum pour centrer la courbe
def echelle ():
  a=float(saisie_A.get())
  b=float(saisie_B.get())
  c=float(saisie_C.get())
  extremum=(fonction_polynome(-b/(2*a)))
  if -2<extremum<2:
      return(100)
  else:
      return(10)
 
# fonction polynome (formule)
def fonction_polynome (x):
  a=float(saisie_A.get())
  b=float(saisie_B.get())
  c=float(saisie_C.get())
  return (a*(x ** 2) + b*x + c)
 
#trace de la courbe en fonction des (x,y,debut,fin,le pas)
def drawFnScaled (ttl, fn, lower, upper, step):
  ttl.penup()
  x = lower
  y = fn (x)
  scaledX = x * echelle()
  scaledY = y * echelle()
  ttl.goto (scaledX, scaledY)
  ttl.pendown()
  while x < upper:
      x = x + step
      y = fn( x )
      scaledX, scaledY = x * echelle(), y * echelle()
      ttl.goto (scaledX, scaledY)
  ttl.penup()
 
 
#fonction principale lance apres la prise des valeurs
def  trace_fonction():
  suite=0
  a=float(saisie_A.get())
  b=float(saisie_B.get())
  c=float(saisie_C.get())
  #appel de la fonction controle cree au dessus
  if controle(a,b,c)==1:
    # Titre de la page
    turtle.title ('Fonctions polynomes')
    # taille de la page
    turtle.setup (800, 800, 0, 0)
    # créer un objet turtle
    ttl = turtle.Turtle()
    # trace du repere
    drawGridScaled (ttl)
    # dessine la fonction
    ttl.pencolor ('purple')
    #drawFnScaled (ttl,  fonction_polynome , -math.pi, math.pi, 0.01)
    #pour 400 points: 200/echelle avec l'echelle evoluant de 10 a 100
    drawFnScaled (ttl,  fonction_polynome , - (200/ echelle()), 200 / echelle(), 10/echelle())
    # afficher sur le canvas
    turtle.done()
     
 
def delta():
    a=float(saisie_A.get())
    b=float(saisie_B.get())
    c=float(saisie_C.get())
    return(b**2-4*(a)*(c))
 
 
def extremum():
    a=float(saisie_A.get())
    b=float(saisie_B.get())
    c=float(saisie_C.get())
    return((b**2-4*(a)*(c))/(-4*a))
     
     
def solution1():
    a=float(saisie_A.get())
    b=float(saisie_B.get())
    c=float(saisie_C.get())
    return(((-b-sqrt(delta()))/2*a))
   
     
def solution2():
    a=float(saisie_A.get())
    b=float(saisie_B.get())
    c=float(saisie_C.get())
    return(((-b+sqrt(delta()))/2*a))
 
def solution3():
    a=float(saisie_A.get())
    b=float(saisie_B.get())
    c=float(saisie_C.get())
    return(-b/2*a)
 
def alpha():
    a=float(saisie_A.get())
    b=float(saisie_B.get())
    c=float(saisie_C.get())
    return(-b/2*a)
 
def beta():
    a=float(saisie_A.get())
    b=float(saisie_B.get())
    c=float(saisie_C.get())
    return((-b**2-(4*a*c))/a**2)
     
def donner_valeurs():
    a=float(saisie_A.get())
    b=float(saisie_B.get())
    c=float(saisie_C.get())
     
    if a != 0 and controle(a,b,c)==1:
        fen2=Tk()
        fen2.title ('Valeurs :')
        tex2=Label(fen2,text='Delta: '+str(delta()),fg='red')
        tex2.pack()
         
        tex3=Label(fen2,text='Extremum: '+str(extremum()),fg='red')
        tex3.pack()
 
        if delta()>0:
            tex4=Label(fen2,text='X1: '+str(solution1()),fg='red')
            tex4.pack()
             
            tex5=Label(fen2,text='X2: '+str(solution2()),fg='red')
            tex5.pack()
             
            tex9=Label(fen2,text="Forme factorisé: "+str(a) +"(x-(" +str(solution1()) +"))*(x-(" +str(solution2()) +"))",fg='red')
            tex9.pack()
             
             
        elif delta()==0:
            tex6=Label(fen2,text='X0:'+str(solution3()),fg='red')
            tex6.pack()
            tex9=Label(fen2,text="Forme factorisé: " +str(a) +"(x-" +str(solution1()) +")^2",fg='red')
            tex9.pack()
             
        else :
            tex6=Label(fen2,text="Il n'y a pas de solution possible.",fg='red')
            tex6.pack()
 
        tex7=Label(fen2,text='Alpha: '+str(alpha()),fg='red')
        tex7.pack()
        tex8=Label(fen2,text='Beta (ß): '+str(beta()),fg='red')
        tex8.pack()
         
        tex10=Label(fen2,text='Forme canonique: ' +str(a) +'(x+(' +str(alpha()) +"))^2+(" +str(beta()) +')',fg='red')
        tex10.pack()
   
        bouton=Button(fen2,text='OK',command=fen2.destroy)
        bouton.pack()
        fen2.mainloop()
 
     
#fenetre de prise de valeur du debut
fen1=Tk()
fen1.title ('Valeurs de a,b et c :')
 
CaseA=Label(fen1,text='A:', fg='red')
CaseB=Label(fen1,text='B:', fg='red')
CaseC=Label(fen1,text='C:', fg='red')
saisie_A = Entry(fen1,bg='white')
saisie_B = Entry(fen1,bg='white')
saisie_C = Entry(fen1,bg='white')
CaseA.grid(row=0)
CaseB.grid(row=1)
CaseC.grid(row=2)
saisie_A.grid(row=0,column=1)
saisie_B.grid(row=1,column=1)
saisie_C.grid(row=2,column=1)
bou1=Button(fen1,text='Tracer la fonction',command=trace_fonction)
bou1.grid(row =3)
bou2=Button(fen1,text='Donner les valeurs',command=donner_valeurs)
bou2.grid(row=3,column=1)
fen1.mainloop()