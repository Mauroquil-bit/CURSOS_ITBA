# Llévame en tu bicicleta

import pandas as pd
import numpy as np

archivo = pd.read_csv("recorridos-realizados-2021-sample.csv") 

# Obtenemos el número de filas en el archivo
numero_de_filas = len(archivo)

# Usamos .value_counts() para obtener una cuenta de cuantas veces ocurre cada valor
# Dividimos la cantidad de veces que aparece 'NORMAL' por la cantidad de filas
estado_count = archivo['Estado cerrado'].value_counts()
porcentaje_normal = 100*(estado_count['NORMAL'] / numero_de_filas)
print(f'El {porcentaje_normal:.2f}% de los viajes se completaron en estado NORMAL')

# Usamos .mean() para calcular el promedio
duracion_promedio = round(archivo['Duración'].mean())
print(f'La duración promedio es de {duracion_promedio//60} minutos {duracion_promedio%60} segundos')

# Con pd.to_datetime() convertimos strings a objetos datetime
# Usamos .dt.hour para obtener únicamente el valor de hora
# Con .value_counts() y luego .idxmax() encontramos el índice que más veces aparece
horarios_de_inicio = archivo['Fecha de inicio']
horarios_de_inicio = pd.to_datetime(horarios_de_inicio)
horas_de_inicio = horarios_de_inicio.dt.hour
hora_pico = horas_de_inicio.value_counts().idxmax()
print(f'La hora más concurrida es de {hora_pico}hs a {hora_pico+1}hs')

# Con pd.concat unimos las columnas de estaciones de inicio y fin,
# en caso de que una estación aparece sólo en una de ellas
# Usando len() y .value_counts() encontramos la cantidad total de estaciones
estaciones_inicio = archivo['Nombre de estación de inicio']
estaciones_fin = archivo['Nombre de estación de fin de viaje']
estaciones_total = pd.concat([estaciones_inicio, estaciones_fin])
print(f'Se utilizaron {len(estaciones_total.value_counts())} estaciones en total')


###############################################################################

