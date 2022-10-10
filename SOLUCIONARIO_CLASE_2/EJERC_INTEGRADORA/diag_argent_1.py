# Solución 1

import matplotlib.pyplot as plt
import pandas as pd

archivo = pd.read_csv("PopulationArgentina2019.csv")
datos = archivo.to_dict('list')
Age = datos['Age']
M = datos['M']
F = datos['F']

total = sum(M) + sum(F)
M_porcentual = [ 100* i/total for i in M ]
F_porcentual = [ 100* i/total for i in F ]

plt.figure(figsize=(16, 8))
plt.subplot(2, 1, 1)
plt.title('Distribución etaria en mujeres')
plt.bar(Age, F_porcentual)
plt.ylabel('Porcentaje')

plt.subplot(2, 1, 2)
plt.title('Distribución etaria en hombres')
plt.bar(Age, M_porcentual)
plt.ylabel('Porcentaje')
plt.show()

