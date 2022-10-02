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

# Graficar en el intervalo de [-1, 1] la función valor absoluto.
# Elegir una cantidad apropiada de puntos de acuerdo a su criterio.
# Tip: Usar la funcion np.absolute de numpy.

n = 101

X = np.linspace(-1, 1, n)
Y = np.absolute(X)

plt.plot(X, Y)
plt.show()


###########################################################################



