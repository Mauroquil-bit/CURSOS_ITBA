# Solución 2 - Se pueden utilizar las funciones de pandas, sum y len

import pandas as pd

notas = pd.read_excel("Datos.xlsx") 

print(notas['Quimica'].sum()/len(notas['Quimica']))


###############################################################################

