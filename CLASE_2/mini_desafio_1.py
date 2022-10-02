"""
Mini desafío 1
Gráficar en el intervalo de [-1, 1] la función valor absoluto. 
Elegir una cantidad apropiada de puntos de acuerdo a su criterio.
Tip: Usar la funcion np.absolute de numpy.
Gráficar en el intervalo de [-5, 5] una función gaussiana definida como:
f(x)=e−x2/2 
Tip: Usar la funcion np.exp de numpy.
"""

# Parte 1: 
# Gráficar en el intervalo de [-1, 1] la función valor absoluto.
# Elegir una cantidad apropiada de puntos de acuerdo a su criterio.
# Tip: Usar la funcion np.absolute de numpy.

import matplotlib.pyplot as plt

import numpy as np

# Cantidad de puntos
n = 10

X = np.linspace(-1, 1, n)
print('X =\n', X,'\n')

# Se calcula la función sobre cada elemento por separado
Y = np.absolute(X)
print('Y =\n', Y,'\n')

plt.plot(X, Y)
plt.show()

# Parte 2:
# Gráficar en el intervalo de [-5, 5] una función gaussiana definida como:
# f(x)=e−x2/2
# Tip: Usar la funcion np.exp de numpy.

import matplotlib.pyplot as plt
import numpy as np

# Cantidad de puntos
n = 10

X = np.linspace(-5, 5, n)
print('X =\n', X,'\n')

# Se calcula la función sobre cada elemento por separado
Y = np.exp(-X**2/2)
print('Y =\n', Y,'\n')

plt.plot(X, Y)
plt.show()

###########################################################################



