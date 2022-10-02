# Mini desafío 2.A

#Calcular el promedio de las notas de química de todos los alumnos en el archivo Datos.xlsx.
#Tip: Podemos usar la función sum( iterable ) para obtener la suma de todos los campos. 
# Un ejemplo de como funciona:

# ¡La función len() también sigue siendo válida!

#mi_lista = [1, 2, 3, 4, 5]
#total = sum(mi_lista)
#print(total)


#Calcular el promedio de las notas de química 
# de todos los alumnos en el archivo Datos.xlsx.

import pandas as pd

archivo = pd.read_excel("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Datos.xlsx")

promedio = sum(archivo['Quimica']) / len(archivo['Quimica'])
prom_dos_decimales = round(promedio, 2)
print(prom_dos_decimales)

#######################################################



