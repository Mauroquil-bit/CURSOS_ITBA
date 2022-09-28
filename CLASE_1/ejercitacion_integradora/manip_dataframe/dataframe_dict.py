import pandas as pd

# Volvemos a abrir el archivo que fue utilizado anteriormente:
datos = pd.read_excel("Datos.xlsx") 
print(datos)

# Recordar que -datos- es un DataFrame, 
# no un diccionario.
# Pero su uso es similar:



columna = 'Quimica'
print(datos[columna])

# Esto es equivalente a:
print(datos[columna].to_dict("list"))

#####################################################



