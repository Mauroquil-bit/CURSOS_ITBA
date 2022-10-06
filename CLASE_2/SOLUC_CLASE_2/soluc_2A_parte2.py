# Solución 2: Utilizando la función max de pandas y condicionales dentro del dataframe

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import time

archivo = pd.read_csv("BTC.csv")        #Leemos el .csv

#Creamos las variables para el precio mas alto
precio_mas_alto = archivo["Open"].max()
dia_del_record = archivo[archivo["Open"] == precio_mas_alto]["Date"].values[0]

print("El precio mas alto es:", precio_mas_alto)
print("Sucedio el dia:", dia_del_record)
#Diseñamos el label para poner en el gráfico
record_label = f'Precio Record: {precio_mas_alto:.2f}\nDía del record: {dia_del_record}'

# #Creamos el gráfico
plt.figure(figsize=(12, 4))
plt.plot(archivo["Date"], archivo["Open"])
plt.plot(dia_del_record, precio_mas_alto, 'ko', label=record_label)   #Ploteamos un punto, 'ko' le da el tipo de punto, y le asignamos el label
plt.xticks([f'{y}-01-01' for y in range(2015, 2020)]) # Mostrar el primer día de cada año
plt.grid( axis='y' )   # Mostrar una grilla horizontal
plt.legend()           # Mostrar labels
plt.show()