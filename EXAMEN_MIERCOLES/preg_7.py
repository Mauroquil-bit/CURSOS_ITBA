# Se intentó ejecutar el siguiente programa 
# (https://imgur.com/mh4NWaq) con el fin de conocer la calificación
#  de un alumno del curso 
# (puede ver la base de datos en: https://imgur.com/5EQmj4v) 
# pero el mismo terminó en un error de ejecución. 
# ¿Cuál es la causa del problema?

import pandas as pd
tabla = pd.read_csv('archivo.xlsx', index_col="Apellido")
dataFrame = tabla.to_dict("index")
print(dataFrame["Lopez"]["Matemática"])

# Respuesta:
# La causa del error es que el archivo no se encuentra en el directorio
# actual.
# ¿Qué hace este programa?



