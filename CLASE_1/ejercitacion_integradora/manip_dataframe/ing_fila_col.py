import pandas as pd

# Volvemos a abrir el archivo que fue utilizado anteriormente:
datos = pd.read_excel("Datos.xlsx")
print(datos)


# Podemos ingresar primero a la fila y luego a la columna:

indice = 0
alumno = datos.loc[indice] 
print(alumno['Matematica'])