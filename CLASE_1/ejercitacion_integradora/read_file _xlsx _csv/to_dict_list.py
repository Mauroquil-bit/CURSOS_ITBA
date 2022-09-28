import pandas as pd

archivo = pd.read_excel("Datos.xlsx") 
data = archivo.to_dict("list") 
# "list" significa que vamos a almacenar a cada columna como una lista con su contenido

print(data)
print(data['Nombre'])     # Accedemos a los datos de una columna
print(data['Nombre'][2])  # Accedemos al índice 2 de la columna 'Nombres'

# Para acceder a los datos de una fila, 
# debemos usar el índice de la fila
print(data['Nombre'][2])  # Accedemos al índice 2 de la columna 'Nombres'
print(data['Edad'][2])    # Accedemos al índice 2 de la columna 'Edad'
print(data['Peso'][2])    # Accedemos al índice 2 de la columna 'Peso'

###########################################################


