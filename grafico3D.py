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
fig = plt.figure()
ax = fig.gca(projection='3d')

plt.figure(num=None, figsize=(12, 10), dpi=80, facecolor='w', edgecolor='k')

posicion_termocuplas=np.array([32.98,24.96,21.19,16.40,12.31,8.14,])

#separo las matrices de tiempo y datos
#primero creo los vectores vacios

y=np.zeros(len(datos[0,:])*6)
z=np.zeros(len(datos[0,:])*6)
x=np.zeros(len(datos[0,:])*6)

a0=tiempo[0,:]
a1=tiempo[1,:]
a2=tiempo[2,:]
a3=tiempo[3,:]
a4=tiempo[4,:]
a5=tiempo[5,:]

b0=datos[0,:]
b1=datos[1,:]
b2=datos[2,:]
b3=datos[3,:]
b4=datos[4,:]
b5=datos[5,:]

#ahora les meto cada fila de los valores
for j in range(6):
    for i in range(len(datos[0,:])):
        y[j*len(datos[0,:])+i]=tiempo[j,i]
        z[j*len(datos[0,:])+i]=datos[j,i]
for j in range(len(datos[0,:])):
    for i in range(6):
        x[j*6+i]=posicion_termocuplas[i]
    
y=np.array(y)
z=np.array(z)

ax.plot(y, x, z, label='parametric curve')
ax.legend()

plt.show()
