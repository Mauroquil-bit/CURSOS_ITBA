# Mini desafío 2.B - Challenge
#Se pide realizar un gráfico de la cotización de las acciones diarias de las compañias Amazon y Google de los últimos 10 años. 
# Encontrar los puntos donde se cruzan los dos gráficos y marcarlos con un punto. 
# Usar dos tipos de línea distintos.
#Nota:
#Usen la función read_csv. Recuerden que un .csv es prácticamente identico a un .xlsx.
#Los valores a graficar estan la columna Open (usando to_dict("list") podrían resolver el problema).
#Tip: Ya que los gráficos son discretos, 
# para detectar un cruce deberán revisar que la acción que es la más cara hoy sea la que era más barata ayer. 
# Esto es porque sería muy raro que haya un día en el cual ambas acciones tengan exactamente el mismo precio. 
# Para interpretar mejor este comentario pueden observar que en la siguiente imagen se producen 2 cruces, 
# pero sólamente en el primero el cruce es exactamente sobre el mismo valor:

import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

archivo = pd.read_csv("C:\Users\exa13769\OneDrive - AMX Argentina S.A\Documentos\CURSOS_ITBA\GOOGLE.csv")

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

# plt.plot(fechas, cotizaciones, 'b-', label='Valor del Bitcoin')
# plt.legend()
# plt.show()

# ##########################################################

