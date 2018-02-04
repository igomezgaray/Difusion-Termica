# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 14:50:28 2018

@author: ferchi
"""
import math as m
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from array import array
from scipy.special import erfc
import os

posicion_termocuplas=np.array([32.98,24.96,21.19,16.40,12.31,8.14,])

#pongo la variable "a" para cambiar que canal ajusto
a=0
x=tiempo[a,:]
y=datos[a,:]
#saco los puntos del inicio que no habia calentado el soldador
r=100
x=x[r:-1]
y=y[r:-1]
X=posicion_termocuplas[a]
x=x+10
ey=y*0.02
t=x[0]
print(np.exp(X**2/(4*k*t)))
#A=F0/K
#f=lambda t,A,k:2*A*((k*t/np.pi)**(1/2)*np.exp(X**2/(4*k*np.floor(t)))-X/2*erfc(X/2/(k*t)**(1/2)))
t0=-500
f=lambda t,A,k,T0:2*A*((k*(t-t0)/np.pi)**(1/2)*np.exp(X*X/(4*k*t))-X/2*erfc(X/2/(k*(t-t0))**(1/2)))+T0

iniciales=np.array([150,6,38])
xx=np.linspace(x[0],x[-1],100000) 
popt, pcov = curve_fit(f,x,y,p0=iniciales,sigma = ey,absolute_sigma=True) #calcula el fiteo y devuelve los sigmas y los valores de las variables que dan el fiteo, el sigma es el error del eje y. la parte del absolute_sigma es para que la matriz de error dependa del error de y, si es false depende de cuanto se dispersan del ajuste
plt.plot(xx,f(xx, popt[0], popt[1],popt[2]), 'g-', label = 'Ajuste '+'CH'+str(a))#los popt son los valores de las variables fiteadas que usara la funcion f                      
                   
#plt.plot(xx,f(xx,iniciales[0],iniciales[1],iniciales[2]),'g-', label = 'Ajuste')
plt.plot(x,y,'b-', label = 'CH'+str(a))
plt.grid(True) # Para que quede en hoja cuadriculada
plt.title('Temperatura en funcion del tiempo')
plt.xlabel('tiempo (s)')
plt.ylabel('Temnperatura (ºC)')
plt.legend(loc = 'best') 


