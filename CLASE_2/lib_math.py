"""
Incluso podríamos definir una función de Python para ayudarnos a graficar una función matemática genérica, 
volviendo sencillo escribir nuevas expresiones. 
En el siguiente ejemplo graficamos la función  y=sin(2πx)  haciendo uso de la librería math.
¿En este caso cuántos puntos consideran necesarios para que el gráfico parezca una curva perfecta?
Tip: Prueben cambiar la cantidad de puntos a 5, 10, 20, 50, 100, etc. 
para ver qué sucede.
"""

import matplotlib.pyplot as plt
import math

def f(x):
  return math.sin( 2 * math.pi * x )

n = 10  # Cantidad de puntos

X = [ x/(n-1) for x in range(n) ] 
Y = [ f(x) for x in X ]

plt.plot(X, Y)    # plt.plot recibe 2 listas de igual longitud, la primera para el eje X, la segunda para el eje Y
plt.show()        # Luego de generar el gráfico, lo mostramos

###########################################################################

