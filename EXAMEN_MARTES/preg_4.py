# ¿Qué subplot se está seleccionando mediante el uso de la instrucción plt.subplot(2, 3, 4) ?


# ¿Cuántos parámetros tiene el método plt.subplot() ?
# ¿Qué hace plt.subplot(2, 3, 4) ?
# plt.subplot(2, 3, 4)
# selecciona el subplot de la fila 2 y columna 3.
#
# ¿Qué hace plt.subplot(2, 3, 4) ?
# plt.subplot(2, 3, 4)
# selecciona el subplot de la fila 2 y columna 3.
#
# ¿Qué hace plt.subplot(2, 3, 4) ?
# plt.subplot(2, 3, 4)
# selecciona el subplot de la fila 2 y columna 3.
#
# ¿Qué hace la instrucción plt.subplot(2, 3, 4) ?
# plt.subplot(2, 3, 4)
# selecciona el subplot de la fila 2 y columna 3.
#
# ¿Qué hace plt.subplot(3, 2, 4) ?
# plt.subplot(3, 2, 4)
# selecciona el subplot de la fila 3 y columna 2.
#
# ¿Qué hace plt.subplot(4, 2, 3) ?
# plt.subplot(4, 2, 3)
# selecciona el subplot de la fila 4 y columna 2.
# Ejemplo:
# import numpy as np
# import matplotlib.pyplot as plt
#
# x = np.arange(0, 2*3.14 , 0.25)
# plt.subplot(2, 3, 4)
# plt.plot(x,np.sin(x),'m*',label='Seno')       # Magenta con estrellas
# plt.plot(x,np.cos(x),'r--',label='Coseno')    # Rojo linea discontinua
# plt.legend()
# plt.show()
#

# ¿Qué hace plt.subplot(2, 3, 4) ?
# plt.subplot(2, 3, 4)
# selecciona el subplot de la fila 2 y columna 3.

import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 3)
fig.set_size_inches(8, 6)

# ¿Qué hace plt.subplots(2, 3) ?
# plt.subplots(2, 3)
# genera una figura con 2 filas y 3 columnas de subplots.

# ¿Qué hace fig, ax = plt.subplots(2, 3) ?
# fig, ax = plt.subplots(2, 3)
# genera una figura con 2 filas y 3 columnas de subplots.

# ¿Qué hace plt.subplots(2, 3, 4) ?
# plt.subplots(2, 3, 4)
# genera una figura con 2 filas y 3 columnas de subplots.
# ¿Que significa el tercer parámetro?







