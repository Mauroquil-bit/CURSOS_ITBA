# En función a la base de datos 
# (https://imgur.com/v8VnqEA) 
# determine que imprimirá de este programa 
# (https://imgur.com/KnMRgpw).


import pandas as pd 
tabla = pd.read_excel("LigaArgentina.xlsx")

error = tabla[tabla['Goles convertidos']-tabla['Goles recibidos']!=tabla['Diferencia de Gol']
print(error["Equipo"])

# ¿Qué hace import pandas as pd?
# Importa la librería pandas y la renombra como pd

# ¿Qué hace tabla = pd.read_excel("LigaArgentina.xlsx")?
# Lee el archivo LigaArgentina.xlsx y lo guarda en la variable tabla

# ¿Qué hace error = tabla[tabla['Goles convertidos']-tabla['Goles recibidos']!=tabla['Diferencia de Gol']?
# Guarda en la variable error los equipos que no tienen la diferencia de goles correcta

# ¿Qué hace print(error["Equipo"]?
# Imprime los equipos que no tienen la diferencia de goles correcta





