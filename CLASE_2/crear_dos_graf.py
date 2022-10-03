# En caso de que no queramos mostrar las curvas superpuestas, 
# podemos crear diferentes gráficos en la pantalla utilizando plt.subplot(nrows, ncols, index).
# nrows: Número de filas
# ncols: Número de columnas
# index: Número entre 1 y nrows*ncols.
# Nota: Usando plt.tight_layout() justo antes de plt.show() se ajusta automáticamente el espaciado entre los subplots. 
# Pueden probar comentando la instrucción en los próximos ejemplos para ver cómo cambia levemente el espaciado.

import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 2*3.14, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.subplot(2, 1, 1)   # 2 filas, 1 columna, posición 1
plt.plot(x, y1, 'b-')  # graficamos función y1

plt.subplot(2, 1, 2)   # 2 filas, 1 columna, posición 2
plt.plot(x, y2, 'r-.') # graficamos función y2

plt.tight_layout()     # Ajustar espaciado entre subplots

print('Ejemplo 1:\n')
plt.show()


# Una vez que usamos plt.show() el gráfico se muestra y podemos crear uno nuevo:


plt.subplot(1, 2, 1)   # 1 fila, 2 columnas, posición 1
plt.plot(x, y1, 'b-')  # graficamos función y1

plt.subplot(1, 2, 2)   # 1 fila, 2 columnas, posición 2
plt.plot(x, y2, 'r-.') # graficamos función y2

plt.tight_layout()     # Ajustar espaciado entre subplots

print('\nEjemplo 2:\n')
plt.show()

########################################################

# ¿Qué hace y1 = np.sin(x)?
# y1 = np.sin(x)
# genera una lista de números que van desde 0 hasta 2*3.14 con un paso de 0.1.

# ¿Qué hace y2 = np.cos(x)?
# y2 = np.cos(x)
# genera una lista de números que van desde 0 hasta 2*3.14 con un paso de 0.1.

# ¿Qué hace plt.subplot(2, 1, 1)?
# plt.subplot(2, 1, 1)
# crea un gráfico de 2 filas, 1 columna y lo ubica en la posición 1.

