import pandas as pd

# Volvemos a abrir el archivo que fue utilizado anteriormente:
datos = pd.read_excel("Datos.xlsx") 
print(datos)

indice = 0
alumno = datos.loc[indice] 
print(alumno)

#####################################################
