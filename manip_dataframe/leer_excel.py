import pandas as pd

# Volvemos a abrir el archivo que fue utilizado anteriormente:
datos = pd.read_excel("Datos.xlsx") 
print(datos)

# Convertimos el DataFrame en un diccionario:
data = datos.to_dict("index")
print(data)

#####################################################

