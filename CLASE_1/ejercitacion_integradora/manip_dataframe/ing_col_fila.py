import pandas as pd

# Volvemos a abrir el archivo que fue utilizado anteriormente:
datos = pd.read_excel("Datos.xlsx")
print(datos)

# Podemos ingresar primero a la columna y luego a la fila:

indice = 0
matematica = datos['Matematica']
print(matematica[indice])

#####################################################

