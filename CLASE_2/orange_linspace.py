"""
Con np.arange() debemos indicar el salto entre un elemento y otro, 
mientras que con np.linspace() tenemos que indicar la cantidad total de elementos. 
Además np.arange() no incluye el valor de stop en el vector mientras que np.linspace() sí.
Vamos a recrear el gráfico anterior usando np.linspace(), 
np.sin() y np.pi:
"""

import matplotlib.pyplot as plt
import numpy as np

# Cantidad de puntos
n = 10

X = np.linspace(0, 1, n)
print('X =\n', X,'\n')

# Se calcula la función sobre cada elemento por separado
Y = np.sin( 2 * np.pi * X )
print('Y =\n', Y,'\n')

plt.plot(X, Y)
plt.show()


"""
Podemos ver que 2*np.pi es una constante, 
por lo que al multiplicarlo por X se realiza la multiplicación elemento a elemento. 
Cada elemento del vector X se multiplica por la misma constante: 2*np.pi. 
Luego np.sin() calcula el seno, nuevamente, elemento a elemento.
"""
###########################################################################

