# Ejemplo 2:

import numpy as np
import matplotlib.pyplot as plt

x1 = [1.5, 1.7, 1.95, 2.63, 2.8, 3.9, 4.76]
y1 = [4.02, 4.61, 4.52, 6.35, 6.55, 9.21, 10.5]

x2 = np.arange(0, 8, 1)
y2 = 2*x2 +1

plt.plot(x1, y1, 'bo', label='Valores Medidos')
plt.plot(x2, y2, 'r-.', label='Estimación')
plt.legend()
plt.show()


########################################################

