import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pylab import *
from fractions import Fraction

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numer, denom):

    if denom == 0:
        return "Division by 0 - result undefined"
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    if reduced_den == 1:
        return reduced_num
    elif common_divisor == 1:
        return numer, denom
    else:
        return reduced_num, reduced_den

liste = [] 
couleur = ['b','g','r','c','m','y','k','w'] 
liste_abscisse = []
liste_ordonnee = []


typ = input("Des points ou des vecteurs ? (p/v) ")
if typ == "p":
  r = int(input("Nombre de points : (SI VOUS VOULEZ PLUSIEURS VECTEURS, VOUS DEVEZ ÉCRIRE D'ABORD LE POINT DE BASE PUIS CELUI D'ARRIVÉE ET SI VOUS AVEZ 2 FOIS LE MEME POINT DE DEPART, RÉECRIVEZ-LE  :  "))
  for x in range(r):
     coordonnees = list(map(int,input("X,Y : ").split(",")))
     liste.append(coordonnees)
  for x in range(len(liste)):
    liste_abscisse.append(liste[x][0])
    liste_ordonnee.append(liste[x][1])


diff = (abs(min(liste_abscisse)) + abs(max(liste_abscisse)))/3
if min(liste_abscisse)-diff >= 0:
  plt.xlim(-2,max(liste_abscisse)+diff)
else :
  plt.xlim(min(liste_abscisse)-diff,max(liste_abscisse)+diff)

diff2 = (abs(min(liste_ordonnee)) + abs(max(liste_ordonnee)))/3
if min(liste_ordonnee)-diff2 >= 0:
  plt.ylim(-2,max(liste_ordonnee)+diff2)
else:
  plt.ylim(min(liste_ordonnee)-diff2,max(liste_ordonnee)+diff2)
plt.grid(True)
plt.title("Représentation graphique d'une fonction")

ax = gca()
ax.yaxis.set_major_locator(MultipleLocator(2.0))
ax.yaxis.set_major_locator(MultipleLocator(1.0))
ax.xaxis.set_major_locator(MultipleLocator(1.0))
ax.xaxis.set_minor_locator(MultipleLocator(0.2))
ax.yaxis.set_minor_locator(MultipleLocator(0.2)) 


ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.subplots_adjust(left=0, bottom=0, right=1, top=1,wspace=None, hspace=None)

ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
# ax.set_xticklabels([])
# ax.set_yticklabels([])
for x in range(int(len(liste)/2)):
  abscisse = liste[1][0] - liste[0][0]
  ordonee = liste[1][1] - liste[0][1]

  try:
    ax.arrow(liste[0][0], liste[0][1], abscisse, ordonee, head_width=0.1, head_length=0.15, fc='k', ec=couleur[x])
  except :
    ax.arrow(liste[0][0], liste[0][1], abscisse, ordonee, head_width=0.1, head_length=0.15, fc='k', ec='k')
  liste.remove(liste[0])
  liste.remove(liste[0])
plt.show()

