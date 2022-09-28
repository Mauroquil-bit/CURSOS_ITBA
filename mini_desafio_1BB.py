#Mini desafío 1.B - Challenge
#Determinar qué equipo es el campeón (1ro) y perdedor (último). 
# ¿Qué columnas del archivo hay que analizar en este caso?

import pandas as pd
archivo = pd.read_excel("Tabla1.xlsx")
data = archivo.to_dict("list")
filas = len(data["Equipo"])
print("")
for i in range(len(data["Equipo"])):
    data_1 = (data["Equipo"][i], ":", data["Goles a favor"][i] - data["Goles en contra"][i])
print("El campeón es:", data["Equipo"][0])
print("El perdedor es:", data["Equipo"][filas-1])
