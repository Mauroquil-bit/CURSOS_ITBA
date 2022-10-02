# Buscando la $

"""
Tema: Buscando la $
Procesamiento de información estructurada
Librerías
Utilizando el set de datos del archivo california_housing_train.xlsx
Dividir el area cubierta por el censo en cuadrantes de 0.5 de latitud x 0.5 de longitud, encontrar para qué cuadrante el valor medio de 'median_house_value' es máximo. Asignar el paso como una variable para que pueda cambiarse facilmente. Para filtrar las zonas de muy baja residencia descarten los valores cuando hay menos de 100 casas.
Datos utiles:
Minimo de longitud: -124.3
Máximo de longitud: -114.3
Minimo de latitud: 32.5
Máximo de latitud: 42.5
Tips: El programa va a tardar en correr, 
no se asusten! Pueden investigar funciones de numpy para ayudarlos a resolver el problema, como numpy.arange.
Nota final: ¡Busquen en el mapa estas coordenadas para ver donde quedan!
"""

import pandas as pd
import numpy as np

archivo = pd.read_excel("california_housing_train.xlsx") 
paso = .5

lats = np.arange(32.5,42.5,paso)
lons = np.arange(-124.3,113.3,paso) 
maximoValor = 0
maximaLat = 0
maximaLon = 0
for lat in lats:
    for lon in lons:
        data = archivo[(archivo['latitude']>=lat) & (archivo['latitude']<=lat+paso)]
        data = data[(data['longitude']>=lon) & (data['longitude']<=lon+paso)]
        if(len(data)>100):
            m = np.mean(data['median_house_value'])
            if m > maximoValor:
                maximaLat = lat
                maximaLon = lon
                maximoValor = m
                
print('Latitude:',maximaLat,'Longitude',maximaLon,'Price',maximoValor)


