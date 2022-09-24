# Obtener el promedio general sólo para aquellos alumnos que aprobaron Matemática 
# (con nota >= 6) en el archivo Datos.xlsx.

import pandas as pd

df = pd.read_excel("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Datos.xlsx")

df = df[ df['Matematica'] >= 6 ]

promedio = (df['Quimica'] + df['Matematica'] + df['Fisica']) / 3

print('Promedio general de los alumnos que aprobaron Matemática')

prom_gral = promedio.mean()
prom_gral = round(prom_gral, 2)

print(prom_gral)

# que hace mean()?


#######################################################





