# Mini desafío 2.A
# Calcular el promedio de las notas de química de todos los alumnos en el archivo Datos.xlsx.
# Tip: Podemos usar la función sum( iterable ) para obtener la suma de todos los campos. 
# Un ejemplo de como funciona:


mi_lista = [1, 2, 3, 4, 5]
total = sum(mi_lista)
print(total)

import pandas as pd

datos = pd.read_excel("Datos.xlsx") 
data = datos['Quimica']

print(sum(data) / len(data))

# ¡La función len() también sigue siendo válida!

###############################################################################

