# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 17:28:27 2021

@author: bunya
"""

"""
Spyder 
Bunyamin matplotlib
"""
import os 
os.getcwd()
os.chdir("C:\\Users\\bunya\\python")
import pandas as pd

# we import the Matplotlib library
import matplotlib as mlp
import matplotlib.pyplot as plt
plt.plot([5,7,2,4])
plt.plot([5,7,2,4], [4,6,9,2], 'ro')
# 'ro' stands for round object
# we create two objects
x = [ 50, 70, 90, 65]
y = [129, 192, 163, 172]
plt.plot(x, y, linewidth = 4.0)
plt.plot(x, y, linewidth = 2.0, linestyle = '--')
plt.plot(x, y, linewidth = 1.0, ls = '-', marker = "o", markersize = 10)
plt.plot(x, y, linewidth = 1.0, ls = '-', marker = "o", markersize = 10, markerfacecolor = 'white')
plt.plot(x, y)
plt.title("TITLE")
plt.xlabel("Axis X")
plt.ylabel("Axis Y")

#grid and other parameter introduce
plt.plot(x, y)
plt.title("TITLE", color = "blue")
plt.xlabel("Axis X", color = "purple")
plt.ylabel("Axis Y", color = "green")
plt.grid(True)
plt.legend(['Legend1'])  

plt.plot(x, y)
plt.title("TITLE", color = "blue")
plt.xlabel("Axis X", color = "purple")
plt.ylabel("Axis Y", color = "green")
plt.grid(True)
plt.legend(['Legend2'], loc = 2)

#can also change the shapes used in a plot
plt.plot([1,2,3,4],[1,4,8,15],'b*')
plt.plot([1,3,5,7],[1,4,8,12],'g^')
plt.plot([1,2,3,5],[2,5,4,12],'ro')
plt.legend(['First','Second','Third'],loc=0)

plt.scatter(x, y)
plt.bar(x, y)
plt.barh(x, y)



      