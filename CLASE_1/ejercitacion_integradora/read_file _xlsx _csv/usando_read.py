import pandas as pd

archivo = pd.read_excel("Datos.xlsx") 
# La variable archivo es de un tipo de dato especial de pandas llamado 'DataFrame'
print(archivo)

######################################################

# Para convertir el DataFrame en un diccionario:
data = archivo.to_dict("list")
print(data)

######################################################

