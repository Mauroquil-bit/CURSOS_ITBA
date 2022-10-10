# Pregunta 2:

# Elegir cuál de las opciones completa el código 
# (https://imgur.com/BJKoooM) en función de la siguiente base de datos 
# (https://imgur.com/k1PRYDJ).

import pandas as pd

tabla = pd.read_csv("LigaArgentina.xlsx")
dataframe = tabla.to_dict('list')


print(dataFrame["Boca Juniors"]["Puntaje"])

# ¡Respuesta!

# dataFrame["Boca Juniors"]["Puntaje"]

# Pregunta 3:

# Elegir cuál de las opciones completa el código

# (https://imgur.com/BJKoooM) en función de la siguiente base de datos
# (https://imgur.com/k1PRYDJ).

import pandas as pd

tabla = pd.read_xlsx("LigaArgentina.xlsx", endex_col='Equipo')
dataframe = tabla.to_dict('index')

print(dataFrame["Boca Juniors"]["Puntaje"])


# ¿Qué hace tabla = pd.read_xlsx("LigaArgentina.xlsx", endex_col='Equipo')?
# Lee el archivo LigaArgentina.xlsx y lo guarda en la variable tabla,
# con el índice de la tabla siendo la columna Equipo

# ¿Qué hace dataframe = tabla.to_dict('index')?
# Convierte la tabla en un diccionario, donde cada clave es el índice de la tabla
# y el valor es un diccionario con los valores de la fila

# ¿Qué hace print(dataFrame["Boca Juniors"]["Puntaje"]?
# Imprime el puntaje del equipo Boca Juniors

# ¡Respuesta!

# ¿Que hace el método idxmax()?
# Devuelve el índice del valor máximo de la serie

# ¿Que hace el método idxmin()?
# Devuelve el índice del valor mínimo de la serie
