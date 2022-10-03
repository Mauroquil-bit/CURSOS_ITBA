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

