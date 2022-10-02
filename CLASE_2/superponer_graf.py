# Es posible ejecutar varias veces plt.plot() para superponer diferentes gráficos, 
# pero plt.show() se ejecuta una sola vez al final del código.
#Adicionalmente, podemos personalizar cada gráfico con un tercer parámetro de la función plt.plot(), 
# el cual es un string. El contenido del string indicará el tipo de linea y el color. 
# Mostramos un ejemplo donde le cambiamos el tipo de linea agregando los parámetros m*, r--:

import numpy as np
import matplotlib.pyplot as plt 

x = np.arange(0, 2*3.14 , 0.25)
plt.plot(x,np.sin(x),'m*')       # Magenta con estrellas
plt.plot(x,np.cos(x),'r--')      # Rojo linea discontinua
plt.show()

# Resultado:



##########################################################################

# ¿Qué hace np.arange(0, 2*3.14 , 0.25)?
# np.arange(0, 2*3.14 , 0.25)
# genera una lista de números que van desde 0 hasta 2*3.14 con un paso de 0.25.
# ¿Un ejemplo?
# import numpy as np
# x = np.arange(0, 2*3.14 , 0.25)
# print(x)

# [ 0.    0.25  0.5   0.75  1.    1.25  1.5   1.75  2.    2.25  2.5   2.75
#   3.    3.25  3.5   3.75  4.    4.25  4.5   4.75  5.    5.25  5.5   5.75
#   6.    6.25  6.5   6.75  7.    7.25  7.5   7.75  8.    8.25  8.5   8.75
#   9.    9.25  9.5   9.75 10.   10.25 10.5  10.75 11.   11.25 11.5  11.75
#  12.   12.25 12.5  12.75 13.   13.25 13.5  13.75 14.   14.25 14.5  14.75
#  15.   15.25 15.5  15.75 16.   16.25 16.5  16.75 17.   17.25 17.5  17.75

# ¿Qué hace np.sin(x)?
# np.sin(x)
# genera una lista de números que son el resultado de aplicar la función
# seno a cada elemento de la lista x.
# ¿Un ejemplo?
# import numpy as np
# x = np.arange(0, 2*3.14 , 0.25)
# y = np.sin(x)
# print(y)




