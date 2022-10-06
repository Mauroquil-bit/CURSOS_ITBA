# # Parte 1
import numpy as np
import matplotlib.pyplot as plt

# Cantidad de puntos
n = 101

X = np.linspace(-1, 1, n)
Y = np.absolute(X)
plt.plot(X,Y)
plt.show()

##########################################################

# Parte 2

#Parte 2
import matplotlib.pyplot as plt
import numpy as np
import math

# Cantidad de puntos
n = 100
x = np.linspace(-5,5,n)
gaussiana = np.exp(-x**2/2)  # Expresión vectorizada, calcula el resultado uno a uno

plt.plot(x, gaussiana)
plt.show()

##########################################################

