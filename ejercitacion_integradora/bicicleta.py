"""
Llévame en tu bicicleta
Temas:
Analisís de información estructurada
Librerías
El gobierno de la Ciudad de Buenos Aires recolecta datos acerca del uso de los servicios de bicicletas públicas (ecobici) y publica parte de ellos.
Para este ejemplo usaremos los primeros 10000 viajes de la base de datos del 2021. 
Están invitados a analizar todos los viajes, pero para ello les recomendamos descargar el archivo y ejecutar su programa en forma local (no en Google Golab).
Se quiere conocer más acerca del uso que le dan los usuarios al sistema, 
por lo cual su tarea será extraer la siguiente información:
¿Qué porcentaje de los viajes se completaron en estado NORMAL?
¿Cuál es la duración promedio de cada viaje? (Los datos están en segundos)
¿A qué hora del día se realizaron más viajes? (por ejemplo: de 16hs a 17hs)
¿Cuántas estaciones diferentes fueron utilizadas?
Para cada estación utilizada como inicio de un viaje, 
imprimirlas ordenadas por cantidad de viajes que iniciaron de la misma.
Tip: Recuerden investigar los métodos que tienen los DataFrames para ver si alguno de ellos les ayuda a resolver un problema particular.
"""

import pandas as pd
import numpy as np

archivo = pd.read_csv("recorridos-realizados-2021-sample.csv") 

# ¿Qué porcentaje de los viajes se completaron en estado NORMAL?
print('Porcentaje de viajes completados en estado NORMAL')
print(len(archivo[ archivo['estado'] == 'NORMAL' ]) / len(archivo) * 100)

# ¿Cuál es la duración promedio de cada viaje? (Los datos están en segundos)
print('Duración promedio de cada viaje')
print(archivo['duracion'].mean())

# ¿A qué hora del día se realizaron más viajes? (por ejemplo: de 16hs a 17hs)
print('Hora del día con más viajes')
print(archivo['hora_inicio'].mode())

# ¿Cuántas estaciones diferentes fueron utilizadas?
print('Estaciones diferentes utilizadas')
print(len(archivo['estacion_inicio'].unique()))

# Para cada estación utilizada como inicio de un viaje,
# imprimirlas ordenadas por cantidad de viajes que iniciaron de la misma.
print('Estaciones utilizadas ordenadas por cantidad de viajes')
print(archivo['estacion_inicio'].value_counts())

# ¿Cuál es la estación de inicio más utilizada?
print('Estación de inicio más utilizada')
print(archivo['estacion_inicio'].value_counts().head(1))

# ¿Cuál es la estación de fin más utilizada?
print('Estación de fin más utilizada')
print(archivo['estacion_fin'].value_counts().head(1))

# ¿Cuál es la estación de inicio menos utilizada?
print('Estación de inicio menos utilizada')
print(archivo['estacion_inicio'].value_counts().tail(1))

# ¿Cuál es la estación de fin menos utilizada?
print('Estación de fin menos utilizada')
print(archivo['estacion_fin'].value_counts().tail(1))

# ¿Cuál es la duración promedio de los viajes que comenzaron en la estación más utilizada?
print('Duración promedio de los viajes que comenzaron en la estación más utilizada')
print(archivo[ archivo['estacion_inicio'] == 'Avenida de Mayo 1000' ]['duracion'].mean())

# ¿Cuál es la duración promedio de los viajes que comenzaron en la estación menos utilizada?
print('Duración promedio de los viajes que comenzaron en la estación menos utilizada')
print(archivo[ archivo['estacion_inicio'] == 'Avenida de Mayo 1000' ]['duracion'].mean())










#####################################################

