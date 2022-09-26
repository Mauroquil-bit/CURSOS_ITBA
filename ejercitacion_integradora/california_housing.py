"""★  California Housing
Temas:
Analísis de información estructurada
Librerías

Este archivo contiene un conjunto de datos de viviendas de California, 
el cual fue extraido del censo de nacional estadounidense de 1990. 
Para mas info sobre el set de datos: 
Extraer la siguiente información:
¿Cuantas casas hay con valor 'median_house_value' mayor a 80000 tomando de la longitud -120 a -118? Rta: 5466
¿Cual es el promedio de habitaciones por manzana ('total_rooms') de estas casas? Rta: 2466.31
¿Cual es la casa más cara? ¿Cuántas hay con este valor? Rta: 500001.0 - 814
★★  Obtener la media y la varianza de la propiedad 'median_house_value'. 
Rta: 207300.91 - 13451442293.57
Tip: ¡Pueden investigar funciones de numpy para conseguir la media y la varianza! numpy.var
"""

import pandas as pd
import numpy as np


df = pd.read_csv("california_housing_train.xlsx")

# ¿Cuantas casas hay con valor 'median_house_value' mayor a 80000 tomando de la longitud -120 a -118? Rta: 5466

df = df[ (df['median_house_value'] > 80000) & (df['longitude'] > -120) & (df['longitude'] < -118) ]
print('Cantidad de casas con valor "median_house_value" mayor a 80000 tomando de la longitud -120 a -118')
print(len(df))

# ¿Cual es el promedio de habitaciones por manzana ('total_rooms') de estas casas? Rta: 2466.31

print('Promedio de habitaciones por manzana ("total_rooms") de estas casas')
prom = df['total_rooms'].mean()
prom = round(prom, 2)
print(prom)

# ¿Cual es la casa más cara? ¿Cuántas hay con este valor? Rta: 500001.0 - 814

print('Casa más cara')
print(df['median_house_value'].max())
print('Cantidad de casas con el valor más alto')
print(len(df[ df['median_house_value'] == df['median_house_value'].max() ]))

# ★★  Obtener la media y la varianza de la propiedad 'median_house_value'.

print('Media y varianza de la propiedad "median_house_value"')

import numpy as np

media = np.mean(df['median_house_value'])
media = round(media, 2)
varianza = np.var(df['median_house_value'])
varianza = round(varianza, 2)

print(media, varianza)

##############################################################3333







