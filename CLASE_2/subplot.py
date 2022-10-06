# Se pueden configurar muchísimos más parámetros, 
# por lo cual les mostrarmos únicamente los que se suelen usar más regularmente. 
# Si necesitan funcionalidades más específicas, 
# puedan encontrarlas en la documentación de matplotlib.pyplot.


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2*3.14, 0.3)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(12, 4))  # Configuramos el tamaño del gráfico (en pulgadas)

plt.subplot(1, 2, 1)
plt.title("Gráfico azul")
plt.plot(x, y1, 'bo')        # Graficamos la función y1
plt.xlabel('Tiempo')
plt.ylabel('Corriente')

plt.subplot(1, 2, 2)
plt.title("Gráfico rojo")
plt.plot(x, y2, 'r-.')       # Graficamos la función y2
plt.xlabel('Tiempo')
plt.axis([0, 3, -1, 1])      # Elegimos los límites de los ejes
plt.grid(True)               # Activamos la grilla

plt.show()


######################################################

# ¿Qué hace plt.xlabel('Tiempo')?
# plt.xlabel('Tiempo')
# agrega un label al eje x.

# ¿Qué hace plt.ylabel('Corriente')?
# plt.ylabel('Corriente')
# agrega un label al eje y.

# ¿Qué hace plt.axis([0, 3, -1, 1])?
# plt.axis([0, 3, -1, 1])
# configura los límites de los ejes.

# ¿Qué hace plt.grid(True)?
# plt.grid(True)
# activa la grilla.

# ¿Qué hace plt.title("Gráfico azul")?
# plt.title("Gráfico azul")
# agrega un título al gráfico.

# ¿Qué hace plt.subplot(1, 2, 1)?
# plt.subplot(1, 2, 1)
# divide la ventana en 1 fila y 2 columnas,
# y selecciona el primer gráfico.

# ¿Qué hace plt.subplot(1, 2, 2)?
# plt.subplot(1, 2, 2)
# divide la ventana en 1 fila y 2 columnas,
# y selecciona el segundo gráfico.

# ¿Qué hace plt.figure(figsize=(12, 4))?
# plt.figure(figsize=(12, 4))
# configura el tamaño de la ventana (en pulgadas).

# ¿Qué hace plt.plot(x, y1, 'bo')?
# plt.plot(x, y1, 'bo')
# grafica la función y1 con color azul y puntos.

# ¿Qué hace plt.plot(x, y2, 'r-.')?
# plt.plot(x, y2, 'r-.')
# grafica la función y2 con color rojo y línea punteada.

# ¿Qué hace plt.show()?
# plt.show()
# muestra el gráfico.

# ¿Qué hace plt.legend()?
# plt.legend()
# muestra la leyenda.

