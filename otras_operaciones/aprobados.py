#Podemos hacer otro ejemplo en donde mostramos los alumnos que 
# reprobaron al menos una materia, 
# es decir que:
#(la nota de Química es menor a 4) o 
# (la nota de Matemática es menor a 4) o 
# (la nota de Física es menor a 4).

import pandas as pd

datos = pd.read_excel("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Datos.xlsx")

aprobados = datos[ (datos['Quimica'] < 4) | (datos['Matematica'] < 4) | (datos['Fisica'] < 4) ]
print("Reprobaron al menos una materia:")
print(aprobados)

#Reprobaron al menos una materia:

