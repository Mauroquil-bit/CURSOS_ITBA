#En el siguiente archivo se tienen las notas de algunos alumnos, 
# donde la letra "A" representa que el estudiante se inscribió al examen pero estuvo Ausente
#  y una celda vacía representa que el alumno no se inscribió al examen:

import pandas as pd


datos2 = pd.read_excel("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Datos2.xlsx") 
print("Datos:\n")
print(datos2)


# ¿Cuántos alumnos se inscribieron al examen de Química?
# ¿Cuántos alumnos se inscribieron al examen de Matemática?
# ¿Cuántos alumnos se inscribieron al examen de Física?
