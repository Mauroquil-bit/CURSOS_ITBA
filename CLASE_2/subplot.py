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

