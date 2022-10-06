# Mini desafío 3
# Obtener el promedio general sólo para aquellos alumnos 
# que aprobaron Matemática (con nota >= 6) en el archivo Datos.xlsx.

import pandas as pd

datos = pd.read_excel("CLASE_1\Datos.xlsx")

aprobadosMate = datos[(datos['Matematica']>=6)]
promedios = (aprobadosMate["Quimica"] + aprobadosMate["Matematica"] + aprobadosMate["Fisica"])/3

promedio_general = sum(promedios)/len(promedios)

print("El promedio general es %0.2f " % promedio_general)


###############################################################################

# Qué hace pd.read_excel("Datos.xlsx")?
# pd.read_excel("Datos.xlsx")
# lee el archivo excel "Datos.xlsx" y lo guarda en el dataframe datos.

# Qué hace datos[(datos['Matematica']>=6)]?
# datos[(datos['Matematica']>=6)]
# genera un nuevo dataframe con los alumnos que aprobaron matemática.

# Qué hace promedios = (aprobadosMate["Quimica"] + aprobadosMate["Matematica"] + aprobadosMate["Fisica"])/3?
# promedios = (aprobadosMate["Quimica"] + aprobadosMate["Matematica"] + aprobadosMate["Fisica"])/3
# genera un nuevo dataframe con los promedios de los alumnos que aprobaron matemática.

# Qué hace promedio_general = sum(promedios)/len(promedios)?
# promedio_general = sum(promedios)/len(promedios)
# calcula el promedio general de los alumnos que aprobaron matemática.

# Qué hace print("El promedio general es %0.2f " % promedio_general)?
# print("El promedio general es %0.2f " % promedio_general)
# imprime el promedio general de los alumnos que aprobaron matemática.

# Qué hace import pandas as pd?
# import pandas as pd
# importa la librería pandas y la renombra como pd.



