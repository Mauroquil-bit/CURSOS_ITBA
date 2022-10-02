# Mini desafío 1.B - Challenge
#Determinar qué equipo es el campeón (1ro) y perdedor (último). 
# ¿Qué columnas del archivo hay que analizar en este caso?

import pandas as pd

archivo = pd.read_excel("Tabla1.xlsx", index_col = "Equipo") 
# Indicamos que la columna de indexación será Equipo.
data = archivo.to_dict("index") 
# "index" significa que vamos a obtener el contenido como diccionarios 
# donde la clave es algun campo de cada fila, en este caso la clave de los 
# diccionarios será la clave "Equipo"

# print(data)

maxpunt = 0
minpunt = 1000000
maxname = ''
minname = ''

# Vamos guardando y actualizando los "récords" mientras analizamos cada equipo
for key in data.keys():
    punt = data[key]['Puntos']
    if punt > maxpunt:
        maxpunt=punt
        maxname = key
    if punt < minpunt:
        minpunt=punt
        minname = key

print(maxname, 'resultó campeón con', maxpunt, 'puntos.' )
print(minname, 'resultó último con', minpunt, 'puntos.' )

