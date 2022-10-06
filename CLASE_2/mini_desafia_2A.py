# Mini desafío 2.A
# Se pide realizar un gráfico del valor del Bitcoin de los últimos 10 años, 
# marcar con un punto el valor máximo del gráfico y calcular cuándo sucedió.
# Nota:
# Usen la función pd.read_csv. Un .csv funciona prácticamente igual a un .xlsx.
# Los valores a graficar estan la columna "Open" (usando to_dict("list") podrían resolver el problema).

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np


archivo = pd.read_csv("GOOGLE.csv")
fechas = []
cotizaciones = []
hoy = dt.datetime.today().date()
#el date() del final es para que se eliminen las hh:mm:ss del resultado
fecha_limite = hoy - dt.timedelta(days=3650)

for i in range(len(archivo)):
    fecha = archivo["Date"][i]
    fecha = dt.datetime.strptime(fecha, "%Y-%m-%d").date()
    if fecha >= fecha_limite:
        fechas.append(fecha)
        cotizaciones.append(archivo["Open"][i])

cotizacion_max = max(cotizaciones)
indice_max = cotizaciones.index(cotizacion_max)
fecha_max = fechas[indice_max]

plt.plot(fechas, cotizaciones)
plt.scatter(fecha_max, cotizacion_max, color="red")
plt.show()

print("La cotización máxima fue de", cotizacion_max, "y sucedió el", fecha_max)


#plt.plot(fechas, cotizaciones, 'b-', label='Valor del Bitcoin')
#plt.legend()
#plt.show()

##########################################################

# 