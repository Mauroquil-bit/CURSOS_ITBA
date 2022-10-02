# Parte 2 del minidesafío 1:

# Parte 2:
# Gráficar en el intervalo de [-5, 5] una función gaussiana definida como:
# f(x)=e−x2/2
# Tip: Usar la funcion np.exp de numpy.

import matplotlib.pyplot as plt
import numpy as np

# Gráficar en el intervalo de [-5, 5] una función gaussiana definida como:
# f(x)=e−x2/2

n = 101

X = np.linspace(-5, 5, n)
Y = np.exp(-X**2/2)

plt.plot(X, Y)
plt.show()

###########################################################################





###########################################################################

# ¿Qué hace np.linspace(-5, 5, n)?
# np.linspace(-5, 5, n) 
# genera una lista de n números equiespaciados entre -5 y 5.
# ¿Un ejemplo?



# [ -5.  -4.  -3.  -2.  -1.   0.   1.   2.   3.   4.   5.]

# ¿Qué hace np.exp(-X**2/2)?
# np.exp(-X**2/2)
# genera una lista de n números que son el resultado de aplicar la función
# exponencial a cada elemento de la lista X.
# ¿Un ejemplo?

# import numpy as np

# n = 11

# X = np.linspace(-5, 5, n)
# Y = np.exp(-X**2/2)
# print(Y)

# [  1.38879439e-06   1.83156389e-05   1.35335283e-04   6.06530660e-04
#    1.92874985e-03   3.67879441e-03   5.39909665e-03   5.39909665e-03
#    3.67879441e-03   1.92874985e-03   6.06530660e-04]

# ¿Qué hace np.exp(-X**2/2)?
# np.exp(-X**2/2)
# genera una lista de n números que son el resultado de aplicar la función
# exponencial a cada elemento de la lista X.

