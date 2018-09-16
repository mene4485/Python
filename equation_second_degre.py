import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import sys

print("Nombre A ?") 
a = float(sys.stdin.readline())
print("Nombre B ?") 
b = float(sys.stdin.readline()) 
print("Nombre C ?") 
c = float(sys.stdin.readline())
delta = b*b-4*a*c 

def f(x):
   return a*(x**2) + b*x + c

alpha = (-b)/(2*a)
beta = f(alpha)

x = np.arange(-1000,1000,0.001)
y=f(x)


if delta < 0 :
   print("Il n'y a pas de solution pour cette équation")
   plt.xlim(alpha-5.1,alpha+5.1)
   if beta >= 0:
        plt.ylim(-2.1,beta+5.1)
   else:
        plt.ylim(beta-2.1,(-1)*beta) 
elif delta == 0:
     solution = round(-b/(2*a),2)
     print("La seule solution de cette équation est %s" % solution)
     plt.xlim(solution - 5.1,solution + 5.1)
     plt.ylim(-8.0,8.0)
elif delta > 0:
     solution2 = round((-b-(delta**0.5))/(2*a),2)
     solution1 = round((-b+(delta**0.5))/(2*a),2)
     plt.plot((-b-(delta**0.5))/(2*a),0,'ro')
     plt.plot((-b+(delta**0.5))/(2*a),0,'ro')
     plt.text(solution2,-0.4, str(solution2), fontsize=12)
     plt.text(solution1,-0.4, str(solution1), fontsize=12)
     print("Les solutions de cette équation sont %s et %s" % (solution1,solution2))
     wesh = (solution2 + solution1)/8
     plt.xlim(solution2 - wesh ,solution1 + wesh)
     if beta >= 0:
        plt.ylim(-2.1,beta+2.1)
     else:
        plt.ylim(beta-2.1,(-1)*beta) 

print("Delta : " + str(delta)) 

courbe = input("Voulez-vous une Représentation de votre fonction ?(y/n)")
if courbe == "y":
  plt.grid(True)
  plt.title("Représentation graphique d'une fonction")
  plt.plot(x,y)
  plt.plot(alpha,beta,'ro')
  r = "S(%s;%s)" % ( round(alpha,4), round(beta,4))
  if beta >= 0:
     plt.text(alpha, beta+0.2, r, fontsize=12)
  else:
     plt.text(alpha, beta-0.2, r, fontsize=12)

  ax = gca()
  ax.spines['right'].set_color('none')
  ax.spines['top'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.spines['bottom'].set_position(('data',0))
  ax.yaxis.set_ticks_position('left')
  ax.spines['left'].set_position(('data',0))
  plt.subplots_adjust(left=0, bottom=0, right=1, top=1,wspace=None, hspace=None)
  figManager = plt.get_current_fig_manager() 
  figManager.full_screen_toggle() 
  plt.show()

