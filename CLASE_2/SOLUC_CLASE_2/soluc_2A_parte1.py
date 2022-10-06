# Solución 1: Iterando sobre los valores del dataframe


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import time

archivo = pd.read_csv("BTC.csv")        #Leemos el .csv
data = archivo.to_dict("list")          #Pasamos la data a un formato diccionario en lista
cant = len(data["Date"])                #Obtenemos la cantidad de fechas
#Creamos las variables para los ejes x e y
x = []
y = []

#Creamos las variables para el precio mas alto
precio_mas_alto = 0
dia_del_record = ""

#Recorremos la data, y agregamos a nuestros vectores: la fecha en x y en y el precio
for i in range(cant):
  x.append(data["Date"][i])
  y.append(data["Open"][i])

  if y[i] > precio_mas_alto:        #De paso comparamos el precio con el precio mas alto actual
    precio_mas_alto = y[i]
    dia_del_record = x[i]

print("El precio mas alto es:", precio_mas_alto)
print("Sucedio el dia:", dia_del_record)
#Diseñamos el label para poner en el gráfico
record_label = f'Precio Record: {precio_mas_alto:.2f}\nDía del record: {dia_del_record}'

#Creamos el gráfico
plt.figure(figsize=(12, 4))
plt.plot(x, y)
plt.plot(dia_del_record, precio_mas_alto, 'ko', label=record_label)   #Ploteamos un punto, 'ko' le da el tipo de punto, y le asignamos el label
plt.xticks([f'{y}-01-01' for y in range(2015, 2020)]) # Mostrar el primer día de cada año
plt.grid( axis='y' )   # Mostrar una grilla horizontal
plt.legend()           # Mostrar labels
plt.show()


##########################################################



