# Solución 2: Utilizando unicamente propiedades de pandas

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("PopulationArgentina2019.csv")

total = df.sum()
df.M_porcentual = 100*df['M']/(total.M + total.F)
df.F_porcentual = 100*df['F']/(total.M + total.F)

plt.figure(figsize=(16, 8))
plt.subplot(2, 1, 1)
plt.title('Distribución etaria en mujeres')
plt.bar(df.Age, df.F_porcentual)
plt.ylabel('Porcentaje')

plt.subplot(2, 1, 2)
plt.title('Distribución etaria en hombres')
plt.bar(df.Age, df.M_porcentual)
plt.ylabel('Porcentaje')
plt.show()

