# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 13:31:42 2018

@author: ferchi
"""

import math as m
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from array import array
from scipy.special import erfc
import os
from mpl_toolkits.mplot3d import Axes3D
plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')

posicion_termocuplas=np.array([32.98,24.96,21.19,16.40,12.31,8.14,])
x=posicion_termocuplas

f=lambda X,A,k,T0,t0:2*A*((k*(t-t0)/np.pi)**(1/2)*np.exp(X*X/(4*k*(t-t0)))-X/2*erfc(X/2/(k*(t-t0))**(1/2)))+T0
iniciales=np.array([2,6,21,160])
xx=np.linspace(x[0],x[-1],100000) 
i=0
while i<len(tiempo[0,:]):
    t=tiempo[0,i]
    y=datos[:,i]
    ey=y*0.02 
    plt.plot(x,y,'b-')   
    #popt, pcov = curve_fit(f,x,y,p0=iniciales,sigma = ey,absolute_sigma=True) #calcula el fiteo y devuelve los sigmas y los valores de las variables que dan el fiteo, el sigma es el error del eje y. la parte del absolute_sigma es para que la matriz de error dependa del error de y, si es false depende de cuanto se dispersan del ajuste
    #plt.plot(xx,f(xx, popt[0], popt[1],popt[2],popt[3]), 'g-', label = 'Ajuste '+'CH'+str(6-a))#los popt son los valores de las variables fiteadas que usara la funcion f                      
    i=i+40
ey=y*0.02    
plt.grid(True) # Para que quede en hoja cuadriculada
plt.title('Temperatura en funcion de la distancia para distintos tiempos')
plt.xlabel('Distancia')
plt.ylabel('Temperatura (ºC)')
plt.legend(loc = 'best') 

