# Solución 2: utilizando funciones de numpy (mejor en cuanto a tiempo de ejecución)

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

ganancias = []
pasajes_vendidos_lista = []
for pasajes_vendidos in range(MAX_CAPACIDAD, PASAJES_VENDIDOS + 1):
  pasajes_vendidos_lista.append(pasajes_vendidos)
  ganancia_total_lista = []
  pasajeros = np.random.rand(Q_SIMULACIONES,pasajes_vendidos)
  for i in range(Q_SIMULACIONES):
    q_presentes =  np.count_nonzero(pasajeros[i][pasajeros[i] < PROBABILIDAD_DE_PRESENTE ])
    if q_presentes <= MAX_CAPACIDAD:
      ganancia_total_lista.append(pasajes_vendidos*GANANCIA_NETA_PASAJE)
    else:
      ganancia_total_lista.append(pasajes_vendidos*GANANCIA_NETA_PASAJE - (q_presentes-MAX_CAPACIDAD)*COMPENSACION)
  promedio = np.sum(ganancia_total_lista)/Q_SIMULACIONES
  ganancias.append(promedio);

max_ganancias = max(ganancias)
indice_max_ganancias = ganancias.index(max(ganancias))
# Imprimo el valor máximo
print("Al vender", pasajes_vendidos_lista[indice_max_ganancias], "pasajes, se espera ganar: $", max_ganancias)

plt.figure(figsize=(12, 6))
plt.plot(pasajes_vendidos_lista, ganancias)
plt.plot(pasajes_vendidos_lista[indice_max_ganancias], max_ganancias, 'ro')   # Muestro el valor máximo
plt.grid()
plt.show()


