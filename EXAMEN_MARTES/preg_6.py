# En función a la base de datos (https://imgur.com/5CQ39A1) determine qué imprimirá este programa (https://imgur.com/iu37Huz).
#

import pandas as pd

tabla = pd.read_csv("LigaArgentina.csv", index_col="Equipo")
tabla.loc[["Vélez Sarsfield", "Boca Juniors", "River Plate", "Estudiantes"], ["Partidos"]] = 14

print(tabla.loc[tabla["Partidos"]!=14, ["Puntaje"]])

# imprime la lista de equipos que no tienen la cantidad máxima de partidos jugados.
#
#


