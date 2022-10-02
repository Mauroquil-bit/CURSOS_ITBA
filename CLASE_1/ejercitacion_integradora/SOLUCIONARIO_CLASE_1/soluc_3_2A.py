# Solución 3 - Se puede utilizar directamente la función mean de pandas

import pandas as pd

notas = pd.read_excel("Datos.xlsx") 

print(notas['Quimica'].mean())

###############################################################################

