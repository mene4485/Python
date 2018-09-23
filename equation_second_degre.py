import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from fractions import Fraction


a = Fraction(input("Nombre A : "))
b = Fraction(input("Nombre B : "))
c = Fraction(input("Nombre C : "))

delta = b*b-4*a*c 

def f(x):
   return a*(x**2) + b*x + c

# ces deux fonctions servent juste à simplifier une fraction si necessaire 
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


alpha = (-b)/(2*a)
beta = f(alpha)

x = np.arange(-1000,1000,0.05)
y=f(x)

print()

# print alpha et beta
if alpha.denominator == 1:
  print("Alpha = " + str(alpha.numerator))
else: 
  print("Alpha = " + str(alpha)+" ou sinon " + str(float(alpha)))
if beta.denominator == 1:
  print("Beta = " + str(beta.numerator))
else: 
	print("Beta = " + str(beta)+" ou sinon " + str(float(beta))) 


#print delta
if delta.denominator == 1:
  print("Delta = " + str(int(delta)))
else :
  print("Delta = " + str(delta)+" ou sinon " +str(float(delta)))  

#print les solutions de l'équation + le tableau de signes
if delta < 0 :
  print("Il n'y a pas de solution pour cette équation")
  plt.xlim(alpha-5.1,alpha+5.1)
  if beta >= 0:
    plt.ylim(-2.1,beta+5.1)
  else:
    plt.ylim(beta-2.1,float((-1)*beta))   
  if a > 0:
    print()
    print("Tableau de signe de f(x) : ")
    print("          x     | -infini          +infini |")
    print("          f(x)  |             +            |")
    print()
  elif a < 0:
    print()
    print("Tableau de signe de f(x) : ")
    print("          x     | -infini          +infini |")
    print("          f(x)  |             -            |")
    print()
elif delta == 0:
    solution = (-b)/(2*a)
    print("La seule solution de cette équation est %s" % solution)
    plt.xlim(solution - 5.1,solution + 5.1)
    plt.ylim(-8.0,8.0)
    if a > 0:
      print()
      print("Tableau de signe de f(x) : ")
      print("          x     | -infini     %s     +infini |" % solution)
      print("          f(x)  |      +        " + "0" + "      +      " + (len(str(solution))-6)*" " + "|")
      print()
    elif a < 0:
      print()
      print("Tableau de signe de f(x) : ")
      print("          x     | -infini     %s     +infini |" % solution)
      print("          f(x)  |      -        " + "0" + "      -      " + (len(str(solution))-6)*" " + "|")
      print()
elif delta > 0:
     solution2 = round((-b-(delta**0.5))/(2*a),2)
     solution1 = round((-b+(delta**0.5))/(2*a),2)
     wesh = (solution2 + solution1)/2
     if a > 0:
      print()
      print("Tableau de signe de f(x) : ")
      print("          x     | -infini     %s          %s     +infini |" % (solution2,solution1))
      print("          f(x)  |       +       " + "0" + "     -     " + " 0" + "       +     " + (len(str(solution2))-1)*" " + "|")
      print()
      if solution2 < 0:
        plt.xlim(solution2 - abs(wesh) ,solution1 + abs(wesh))
      else :
        plt.xlim(solution2 - abs(wesh) ,solution1 + abs(wesh)) 
     elif a < 0:
      print()
      print("Tableau de signe de f(x) : ")
      print("          x     | -infini     %s          %s     +infini |" % (solution1,solution2))
      print("          f(x)  |       -       " + "0" + "      +     " + " 0" + "       -     " + (len(str(solution1))-1)*" " + "|")
      print()
      if solution2 < 0:
        plt.xlim(solution2 - wesh ,solution1 + wesh)
      else :
        plt.xlim(solution2 + wesh ,solution1 - wesh)
     plt.plot((-b-(delta**0.5))/(2*a),0,'ro')
     plt.plot((-b+(delta**0.5))/(2*a),0,'ro')
     plt.text(solution2,-0.4, str(solution2), fontsize=12)
     plt.text(solution1,-0.4, str(solution1), fontsize=12)
     if solution1 == int(solution1):
       if solution2 == int(solution2):
         print("Les solutions de cette équation sont %s et %s" % (int(solution2),int(solution1)))
       else :
         mene = simplify_fraction(-b-(delta**0.5),2*a)
         print("Les solutions de cette équation sont %s et %s/%s qui équivaut à environ %s" % (int(solution1),int(mene[0]),int(mene[1]),str(solution2)))
     elif solution2 == int(solution2):
       if solution1 == int(solution1):
         print("Les solutions de cette équation sont %s et %s" % (int(solution1),int(solution2)))
       else :
         mene = simplify_fraction(-b+(delta**0.5),2*a)
         print("Les solutions de cette équation sont %s et %s/%s qui équivaut à environ %s" % (int(solution2),int(mene[0]),int(mene[1]),str(solution1)))
     else :
         mene2 = simplify_fraction(-b+(delta**0.5),2*a)
         mene = simplify_fraction(-b-(delta**0.5),2*a)
         print("Les solutions de cette équation sont %s/%s qui équivaut à environ %s et %s/%s qui équivaut à environ %s" % (int(mene[0]),int(mene[1]),str(solution2),int(mene2[0]),int(mene2[1]),str(solution1)))

     
     

     if beta >= 0:
        plt.ylim(-2.1,beta+2.1)
     else:
        plt.ylim(beta-2.1,float((-1)*beta))  



courbe = input("Voulez-vous une Représentation de votre fonction ?(y/n) ")
if courbe == "y":
  plt.grid(True)
  plt.title("Représentation graphique d'une fonction")
  plt.plot(x,y)
  plt.plot(alpha,beta,'ro')
  r = "S(%s;%s)" % ( alpha, beta)
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
  if abs(int(beta)) >= 10:
  	ax.yaxis.set_major_locator(MultipleLocator(2.0))
  else:
  	ax.yaxis.set_major_locator(MultipleLocator(1.0))
  ax.xaxis.set_major_locator(MultipleLocator(1.0))
  ax.xaxis.set_minor_locator(MultipleLocator(0.2))
  ax.yaxis.set_minor_locator(MultipleLocator(0.2))
  ax.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
  ax.grid(which='minor', axis='x', linewidth=0.25, linestyle='-', color='0.75')
  ax.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')
  ax.grid(which='minor', axis='y', linewidth=0.25, linestyle='-', color='0.75')
  # ax.set_xticklabels([])
  # ax.set_yticklabels([])
  plt.show()
  plt.savefig('ok_mec.png')
