#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from math import*
abscisse = [ k/10 for k in range(100)]
y = [] 
y2 = []


def f(t):
    return sin(t) 

def g(t):
    return cos(t) 

for x in abscisse: 
     y.append(f(x))  
     y2.append(g(x)) 
    
    
plt.plot(abscisse, y)
plt.plot(abscisse, y2)
plt.show() 