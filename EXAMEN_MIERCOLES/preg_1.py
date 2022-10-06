# En función a la base de datos (https://imgur.com/v8VnqEA) 
# determine que imprimirá de este programa 
# (https://imgur.com/KnMRgpw).

import pandas as pd
tabla = pd.read_csv('LigaArgentina.xlsx')

error = tabla[tabla['Goles convertidos'] - tabla['Goles recibidos'] != tabla['Diferencia de gol']]
print(error["Equipo"])

#######################################################################

# ¿Qué hace import pandas as pd?
# ¿Qué hace tabla = pd.read_csv('LigaArgentina.xlsx')?
# ¿Qué hace error = tabla[tabla['Goles convertidos'] - tabla['Goles recibidos'] != tabla['Diferencia de gol']]?
# ¿Qué hace print(error["Equipo"])?

#######################################################################

# Respuesta:
# import pandas as pd
# importa la librería pandas y la renombra como pd
# tabla = pd.read_csv('LigaArgentina.xlsx')
# lee el archivo csv y lo guarda en la variable tabla
# error = tabla[tabla['Goles convertidos'] - tabla['Goles recibidos'] != tabla['Diferencia de gol']]
# guarda en la variable error los datos de la tabla que cumplan la condición
# print(error["Equipo"])
# imprime los datos de la columna Equipo de la variable error

#######################################################################



# ¿Que hace este programa?

# Este programa lee un archivo de excel y lo convierte en un dataframe
# luego busca en el dataframe los valores que no coinciden con la
# diferencia de goles y los imprime.

# ¿Que imprime?

# El programa imprime los valores de la columna Equipo que no coinciden
# con la diferencia de goles.

#

