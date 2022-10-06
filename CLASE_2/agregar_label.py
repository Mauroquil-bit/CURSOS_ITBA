# También se le puede colocar un label a los gráficos, 
# usando el parámetro label='Mi label'.
# Para que todos los labels se muestren juntos, 
# debemos ejecutar plt.legend() después de todos los gráficos, 
# una sóla vez justo antes de plt.show().

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 2*3.14 , 0.25)
plt.plot(x,np.sin(x),'m*',label='Seno')       # Magenta con estrellas
plt.plot(x,np.cos(x),'r--',label='Coseno')    # Rojo linea discontinua
plt.legend()
plt.show()


##########################################################################

# ¿Qué hace plt.legend()?
# plt.legend()
# muestra todos los labels de los gráficos en una sola leyenda.

# ¿Qué hace plt.show()?
# plt.show()
# muestra todos los gráficos en una sola ventana.

# ¿Qué hace plt.plot(x,np.sin(x),'m*',label='Seno')?
# plt.plot(x,np.sin(x),'m*',label='Seno')
# genera un gráfico de la función seno con color magenta y estrellas.

# ¿Qué hace plt.plot(x,np.cos(x),'r--',label='Coseno')?
# plt.plot(x,np.cos(x),'r--',label='Coseno')
# genera un gráfico de la función coseno con color rojo y linea discontinua.

# ¿Qué hace x = np.arange(0, 2*3.14 , 0.25)?
# x = np.arange(0, 2*3.14 , 0.25)
# genera una lista de números que van desde 0 hasta 2*3.14 con un paso de 0.25.

