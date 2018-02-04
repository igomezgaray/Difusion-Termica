# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 15:28:04 2017

@author: ferchi
"""

#paquetes:
import math as m
from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from array import array
import os


#config imagenes
plt.figure(num=None, figsize=(8, 4), dpi=80, facecolor='w', edgecolor='k')

#escribir algo
print('hola')

#crear una matriz de ceros de 1x2:
m=np.zeros((1,2))

#cargar txt:
d=np.loadtxt('d1.txt', delimiter = '\t')#\t es qeu los divide por tab los valores
#SI LOS DATOS VIENEN CON LOS DECIMALES SEPARADOS POR COMAS EN VEZ DE PUNTOS (si no es asi, ignorar):
a=0
while i<40: #en vez de 40 va la cantidad de txts   
    a1 = open('C:/Users/ferchi/.spyder-py3/labo/Mediciones/'+str(a)).read().replace(',','.')#cambio las comas por puntos y lo guardo como b
    a1=a1.split()#convierto v en una matriz separando todo por tabs y enters, por eso esta el ()
    #saco la parte que dice time, date, etc
    a1.remove(a1[0])
    a1.remove(a1[0])
    a1.remove(a1[0])
    a1.remove(a1[0])
    #separo el eje x del y
    x=a1[::2]#agarro las columnas pares
    y=a1[1::2]#agarro las columnas impares
    #lo convierto de texto a numeros
    for i in range(len(x)):
        x[i]=float(x[i])
        y[i]=float(y[i])
    a1=np.zeros((len(x),2))
    a1[:,0]=x
    a1[:,1]=y
    #lo reescribo
    np.savetxt(str(a)+'.txt',a1, fmt='%.18g', delimiter='\t', newline=os.linesep)        
    a=a+1

#seleccionar columnas enteras de la matriz d:
x=[row[0] for row in d] 
y=[row[1] for row in d] 


#cargar la media de varios txt en el vector y:
y=[]
ey=[]
a=0
while a<40:
    a1=np.loadtxt(str(a)+'.txt')
    x=np.array([row[0] for row in a1]) 
    a1=np.array([row[1] for row in a1]) 
    y.append(np.mean(a1))
    ey.append(np.std(a1))
    a=a+1

                       


#borrar elemento
del y[2]#si no es .np
x=np.delete(x,0)#si es .np


#definir vectores hechos por valores equiespaciados
x=np.linspace(0,1,100)#100 valores entre el 0 y el 1
y=np.linspace(0,2,100)


#seleccionar desde el elemento número a hasta el numero b del vector x
x=x[a:b]

#plotear (graficar)
plt.plot(x,y,'b*', label = 'Datos')#x e y deben ser vectores del mismo tamaño
plt.errorbar(x,y,ey,linestyle = 'None')
plt.grid(True) # Para que quede en hoja cuadriculada
plt.title('Grafico ejemplo')
plt.xlabel('Valores en x')
plt.ylabel('Valores en y')
plt.legend(loc = 'best') 

#escala logaritmica:
plt.semilogx()#escala logaritmica en x


#definir una funcion
f=lambda variable1,variable2,variable3,variable4: (variable1)^2-variable2+variable3*variable4

#fiteo con la funcion f 
iniciales=np.array([1,0.1,1.6,0.45]) #crea un vector con los valores iniciales del fiteo en el orden de las variables de la funcion
popt, pcov = curve_fit(f,x,y,p0=iniciales,sigma = ey,absolute_sigma=True) #calcula el fiteo y devuelve los sigmas y los valores de las variables que dan el fiteo, el sigma es el error del eje y. la parte del absolute_sigma es para que la matriz de error dependa del error de y, si es false depende de cuanto se dispersan del ajuste
#popt son los valores de los parametros que devuelve el ajuste, pcov es una matriz que en su diagonal tiene los errores al cuadrado de cada parametro                      
                      
#plotear el fiteo 
xx=np.linspace(x[0],x[-1],1000)                    
plt.plot(xx,f(xx, popt[0], popt[1],popt[2],popt[3]), 'g-', label = 'Ajuste')#los popt son los valores de las variables fiteadas que usara la funcion f                      

#R^2+Chi cuadrado
residuals = y- f(x, popt[0],popt[1])
ss_res = np.sum(residuals**2)
ss_tot = np.sum((y-np.mean(y))**2)
r_squared = 1 - (ss_res / ss_tot)
chi=np.sum(((residuals/(ey))**2)/len(y))
print(r_squared,chi)

mat=np.zeros((len(popt)+1,2))
for i in range(len(popt)):
    mat[i,0]=popt[i]
    mat[i,1]=np.sqrt(pcov[i,i])
    
mat[-1,0]=r_squared
mat[-1,1]=chi

np.savetxt('C:/Users/ferchi/.spyder-py3/ajustes/'+'campo'+'.txt',mat, fmt='%.18g', delimiter='\t', newline=os.linesep)