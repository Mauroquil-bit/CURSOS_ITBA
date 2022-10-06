# ¿Cuál es la salida del siguiente programa 
# (https://imgur.com/DYM1WGB) con la base de datos 
# (https://imgur.com/qP9tXTO)?


import pandas as pd

tabla = pd.read_csv('LigaArgentina.xlsx')

tabla.dropna(subset["Puntaje", "Diferencia de Gol"])

# Respuesta:
# El programa imprime los valores de la columna Equipo que no coinciden
# con la diferencia de goles.
#
# ¿Qué hace este programa?
# Este programa lee un archivo de excel y lo convierte en un dataframe

# ¿Qué hace tabla = pd.read_csv('LigaArgentina.xlsx')?
# lee el archivo csv y lo guarda en la variable tabla

# ¿Qué hace tabla.dropna(subset["Puntaje", "Diferencia de Gol"])?

# Respuesta:
# Elimina las filas que no tienen valores en las columnas Puntaje y Diferencia de Gol

