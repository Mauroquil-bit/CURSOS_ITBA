# Solución 3 - La tercera solución es con el comando to_dict("index"). 
# Se indexa por el nombre de los equipos que debe ser unico de cada equipo.

import pandas as pd

archivo = pd.read_excel("Tabla1.xlsx", index_col="Equipo")

data = archivo.to_dict("index") # diccionario de diccionarios
# la clave de cada campo del diccionario es el nombre del equipo (index_col)
# el contenido de cada campo del diccionario es un diccionario con la información del equipo

print("Diferencias de gol:")

for equipo in data.keys():
    print(equipo, ":", data[equipo]["Goles a favor"] - data[equipo]["Goles en contra"])


###########################################################################

