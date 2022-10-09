# Those three sides

# Escribir una función que dibuje un triángulo equilatero, 
# debe recibir 3 parametros:

# X,Y: coordenadas del centro
# L: Largo de los lados

import numpy as np
import matplotlib.pyplot as plt

def plotTriangle(x, y, L):
  height = np.sqrt(3)*L/2
  apothem = height/3
  #Busco los tres puntos de un triangulo equilatero en base al centro geometrico 
  #https://en.wikipedia.org/wiki/Equilateral_triangle
  point1 = [x-L/2, y-apothem]
  point2 = [x+L/2, y-apothem]
  point3 = [x/2, y+height-apothem]
  # Guardo los puntos en forma x,y, y repito el primer punto para que se cierre el triangulo
  xCoord = [point1[0], point2[0], point3[0], point1[0]]
  yCoord = [point1[1], point2[1], point3[1], point1[1]]
  plt.plot(xCoord, yCoord)
  plt.show()
  return

plotTriangle(0, 0, 100)


##################################################################

# ¿Qué hace import numpy as np?
# Importa la libreria numpy y la renombra como np

# ¿Qué hace import matplotlib.pyplot as plt?
# Importa la libreria matplotlib.pyplot y la renombra como plt

# ¿Qué hace def plotTriangle(x, y, L):?
# Define la funcion plotTriangle que recibe 3 parametros

# ¿Qué hace height = np.sqrt(3)*L/2?
# Calcula la altura del triangulo equilatero

# ¿Qué hace apothem = height/3?
# Calcula el apotema del triangulo equilatero

# ¿Qué hace point1 = [x-L/2, y-apothem]?
# Calcula el primer punto del triangulo equilatero

# ¿Qué hace point2 = [x+L/2, y-apothem]?
# Calcula el segundo punto del triangulo equilatero

# ¿Qué hace point3 = [x/2, y+height-apothem]?
# Calcula el tercer punto del triangulo equilatero

# ¿Qué hace xCoord = [point1[0], point2[0], point3[0], point1[0]]?
# Guarda las coordenadas x de los puntos del triangulo equilatero

# ¿Qué hace yCoord = [point1[1], point2[1], point3[1], point1[1]]?
# Guarda las coordenadas y de los puntos del triangulo equilatero

# ¿Qué hace plt.plot(xCoord, yCoord)?
# Dibuja el triangulo equilatero

# ¿Qué hace plt.show()?
# Muestra el triangulo equilatero

# ¿Qué hace return?
# Retorna el triangulo equilatero

# ¿Qué hace plotTriangle(0, 0, 100)?
# Llama a la funcion plotTriangle con los parametros 0, 0, 100




