# Solución 1: utilizando propiedades de matplotlib

import matplotlib.pyplot as plt
import numpy as np

vendidos = []
ganancias = []

MAX_CAPACIDAD = 222
PASAJES_VENDIDOS = 250
Q_SIMULACIONES = 1000
GANANCIA_NETA_PASAJE = 400
COMPENSACION = 600
PROBABILIDAD_DE_PRESENTE = 0.95

# v es la cantidad de pasajes vendidos
for v in range(MAX_CAPACIDAD, PASAJES_VENDIDOS + 1):
  promedio = 0

  # i es el indice de cada simulacion
  for i in range(Q_SIMULACIONES):
    presentes = 0
    for p in range(v):
      if np.random.rand() < PROBABILIDAD_DE_PRESENTE:  # Determino si la persona p esta presente
        presentes += 1
    if presentes <= MAX_CAPACIDAD:
      promedio += v*GANANCIA_NETA_PASAJE    # Venta del pasaje
    else:
      promedio += v*GANANCIA_NETA_PASAJE - (presentes-MAX_CAPACIDAD)*COMPENSACION   # Venta menos compensación
  promedio /= Q_SIMULACIONES
  ganancias.append(promedio)
  vendidos.append(v)

# Imprimo el valor máximo
imax = ganancias.index(max(ganancias))
print("Al vender", vendidos[imax], "pasajes, se espera ganar: $", ganancias[imax])

plt.figure(figsize=(12, 6))
plt.plot(vendidos, ganancias)
plt.plot(vendidos[imax], ganancias[imax], 'ro')   # Muestro el valor máximo
plt.grid()
plt.show()


###################################################

