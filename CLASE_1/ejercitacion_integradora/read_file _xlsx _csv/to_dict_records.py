import pandas as pd

archivo = pd.read_excel("Datos.xlsx") 

data = archivo.to_dict("records") 
# "records" significa que vamos a obtener el contenido separado por cada fila

print(data)
print(data[2])            # Accedemos a los datos de una fila
print(data[2]['Nombre'])  # Accedemos a la columna 'Nombres' de la fila con índice 2

#######################################################

