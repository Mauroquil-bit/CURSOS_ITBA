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


# dif#erencia entre record y list

# record es un array de numpy

# list es una lista de python

#¿Qué es un array de numpy?

#Un array de numpy es una estructura de datos que permite almacenar datos de un mismo tipo.

# ¿Cómo se usa un array de numpy?

# Para crear un array de numpy se usa la función array() de numpy.

# ¿Cómo se usa la función array() de numpy?
# La función array() de numpy recibe como parámetro una lista de python y devuelve un array de numpy.
# ejemplo de array de numpy

import numpy as np

lista = [1, 2, 3, 4, 5]

array = np.array(lista)

print(array)






