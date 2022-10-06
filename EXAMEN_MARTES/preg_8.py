# Un docente del ITBA tiene en un archivo .xlsx las notas de sus alumnos.  
# Las columnas del archivo son 'Legajo', 'Cursada' y 'Final'. 
# El docente desea ordenar su archivo tal que las notas de finales aparezcan 
# en forma descendiente con notas de cursada ascendiente para cada grupo de notas de finales.  
# A continuación se adjunta una captura de cómo se debería ver el dataframe antes y después de ordenarlo. 
# Indique cuál sería la forma más conveniente de usar .sort_values().

import pandas as pd
import numpy as np

df = pd.read_excel("notas.xlsx")
df = df.sort_values(by=['Final', 'Cursada'], ascending=[False, True])
df.to_excel("notas_ordenadas.xlsx")

# ¿Qué hace df = df.sort_values(by=['Final', 'Cursada'], ascending=[False, True])?
# df = df.sort_values(by=['Final', 'Cursada'], ascending=[False, True])
# ordena el dataframe df por las columnas "Final" y "Cursada" en forma descendiente y ascendiente respectivamente.

# ¿Qué hace df.to_excel("notas_ordenadas.xlsx")?
# df.to_excel("notas_ordenadas.xlsx")
# guarda el dataframe df en el archivo excel "notas_ordenadas.xlsx".

# ¿Qué hace df = pd.read_excel("notas.xlsx")?
# df = pd.read_excel("notas.xlsx")
# lee el archivo excel "notas.xlsx" y lo guarda en el dataframe df.

# ¿Qué hace df = df.sort_values(by=['Final', 'Cursada'], ascending=[False, True])?
# df = df.sort_values(by=['Final', 'Cursada'], ascending=[False, True])
# ordena el dataframe df por las columnas "Final" y "Cursada" en forma descendiente y ascendiente respectivamente.

# ¿Qué hace df.to_excel("notas_ordenadas.xlsx")?
# df.to_excel("notas_ordenadas.xlsx")
# guarda el dataframe df en el archivo excel "notas_ordenadas.xlsx".

# ¿Qué hace df = pd.read_excel("notas.xlsx")?
# df = pd.read_excel("notas.xlsx")
# lee el archivo excel "notas.xlsx" y lo guarda en el dataframe df.

# ¿Qué hace df = df.sort_values(by=['Final', 'Cursada'], ascending=[False, True])?
# df = df.sort_values(by=['Final', 'Cursada'], ascending=[False, True])
# ordena el dataframe df por las columnas "Final" y "Cursada" en forma descendiente y ascendiente respectivamente.

# ¿Qué hace df.to_excel("notas_ordenadas.xlsx")?
# df.to_excel("notas_ordenadas.xlsx")
# guarda el dataframe df en el archivo excel "notas_ordenadas.xlsx".

# ¿Qué hace df = pd.read_excel("notas.xlsx")?
# df = pd.read_excel("notas.xlsx")
# lee el archivo excel "notas.xlsx" y lo guarda en el dataframe df.

# df.sort_values(by = ['Final'] + ['Cursada'], ascending = [False, True])
# df.sort_values(by = ['Final'] + ['Cursada'], ascending = [False, True])
# df.sort_values(by = ['Final'] + ['Cursada'], ascending = [False, True])
# df.sort_values(by = ['Final'] + ['Cursada'], ascending = [False, True])

# ¿Qué hace df.sort_values(by = ['Final'] + ['Cursada'], ascending = [False, True])?
# df.sort_values(by = ['Final'] + ['Cursada'], ascending = [False, True])
# ordena el dataframe df por las columnas "Final" y "Cursada" en forma descendiente y ascendiente respectivamente.

# ¿Qué hace df.sort_values(by = ['Final'] + ['Cursada'], ascending = [False, True])?
# df.sort_values(by = ['Final'] + ['Cursada'], ascending = [False, True])
# ordena el dataframe df por las columnas "Final" y "Cursada" en forma descendiente y ascendiente respectivamente.





