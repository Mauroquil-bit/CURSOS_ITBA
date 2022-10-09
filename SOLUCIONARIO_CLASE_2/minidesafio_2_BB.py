# Solución 2: 
# Explorando el universo de pandas, y teniendo en cuenta que los precios 
# de las acciones son similares si estan a menos de X unidades de diferencia

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leo los dfs
google = pd.read_csv("CLASE_2\GOOGLE.csv")
amazon = pd.read_csv("CLASE_2\AMZN.csv")
# Me fijo que en la misma fecha, ambos valores den relativamente similar (difrencia < X)
# Pongo cruces = ambos.copy porque sino arroja un aviso de que puede estar mal cuando estoy poniéndole valores a la copia
X = 5
ambos = pd.merge(google, amazon, how="inner", on=["Date"],suffixes=('_google', '_amazon'))
cruces = ambos.loc[ abs(ambos["Open_google"] - ambos["Open_amazon"]) < X, :].copy(deep=True)

#PLUS: cambio las fechas, para mostrarlas en formato "dd/mm/aa" y horizontalmente, para lectura más rápida
for index, row in google.iterrows():
  google.loc[index, "Date"] = row["Date"].split('-')[2].replace('\n','')  + '/' + row["Date"].split('-')[1] + '/' + row["Date"].split('-')[0][2:4]
for index, row in amazon.iterrows():
  amazon.loc[index, "Date"] = row["Date"].split('-')[2].replace('\n','')  + '/' + row["Date"].split('-')[1] + '/' + row["Date"].split('-')[0][2:4]
for index, row in cruces.iterrows(): 
  cruces.loc[index, "Date"] = row["Date"].split('-')[2].replace('\n','')  + '/' + row["Date"].split('-')[1] + '/' + row["Date"].split('-')[0][2:4]

plt.figure(figsize=(16, 8))
plt.plot(google["Date"],google["Open"])
plt.plot(amazon["Date"],amazon["Open"])
plt.plot(cruces["Date"],cruces["Open_google"], 'k.')

# En el eje X elijo mostrar 1 cada 250 fechas
# Luego elijo la alineación con el borde derecho del texto
plt.xticks(google["Date"][::250], horizontalalignment='right')

plt.show()


########################################################################


