import pandas as pd

# Indicamos que la columna de indexación será apellido.
archivo = pd.read_excel("Datos.xlsx", index_col ="Apellido") 
print(archivo)

data = archivo.to_dict("index") 
# "index" significa que vamos a obtener el contenido como diccionarios 
# donde la clave es algun campo de cada fila, en este caso la clave de los 
# diccionarios será la clave "Apellido"

# convertimos el tipo de dato de pandas a un dict de python

print(data)
print(data['Martinez'])           # Accedemos a los datos de una fila (usando el dato de índice apropiado)
print(data['Martinez']['Legajo']) # Accedemos a la columna 'Legajo' de la fila con índice 'Martinez'

#####################################################

