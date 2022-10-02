#Mini desafio 1.C - Extra Challenge
#Determinar qué equipos obtuvieron mas de 20 puntos, 
# y mostrar sus diferencias de goles.

#Plus: ordenar los equipos de mayor a menor en puntaje (de forma descendiente).

import pandas as pd
archivo = pd.read_excel("Tabla1.xlsx")
data = archivo.to_dict("list")
filas = len(data["Equipo"])
print("Equipos con más de 20 puntos:")
for i in range(len(data["Equipo"])):
    if data["Puntos"][i] > 20:
        print(data["Equipo"][i], ":", data["Puntos"][i])

#Plus: ordenar los equipos de mayor a menor en puntaje (de forma descendiente).

