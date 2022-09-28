"""
Usando plt.plot(x, y) podemos generar el gráfico de la función.
Es posible incluír muchas curvas superpuestas sobre el mismo gráfico, 
por lo cual matplotlib espera a que se termine de generar cada gráfico 
y al final de todo debemos llamar a plt.show() para mostrar todas las curvas generadas. 
La idea es en el futuro poder realizar distintos gráficos y 
recién al final de todo llamar una sóla vez a plt.show() para mostrar todo junto.
"""

import matplotlib.pyplot as plt

x = [0.0, 0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9,  1.0]
y = [0.0, 0.01, 0.04, 0.09, 0.16, 0.25, 0.36, 0.49, 0.64, 0.81, 1.0]

plt.plot(x, y)  # plt.plot recibe 2 listas de igual longitud, la primera para el eje X, la segunda para el eje Y
plt.show()      # Luego de generar el gráfico, lo mostramos





