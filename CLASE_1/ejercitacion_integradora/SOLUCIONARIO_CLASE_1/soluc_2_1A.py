# Solución 2 - La segunda solución es con el comando to_dict("records")

import pandas as pd

archivo = pd.read_excel("Tabla1.xlsx")

data = archivo.to_dict("records") # lista de diccionarios
# cada elemento de la lista es un diccionario que contiene los valores de cada fila

print("Diferencias de gol:")

for i in range(len(data)):
    print(data[i]["Equipo"], ":", data[i]["Goles a favor"] - data[i]["Goles en contra"])

###########################################################################

