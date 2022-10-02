# Solución 1 - La primera solución es con el comando to_dict("list")

import pandas as pd

archivo = pd.read_excel("Tabla1.xlsx")

data = archivo.to_dict("list") # diccionario de listas.
#La clave de los diccionarios es el nombre de la columna
#El contenido de los diccionarios es una lista con el contenido de la columna

filas = len(data["Equipo"])

print("Diferencias de gol:")

for i in range(len(data["Equipo"])):
    print(data["Equipo"][i], ":", data["Goles a favor"][i] - data["Goles en contra"][i])


###########################################################################

