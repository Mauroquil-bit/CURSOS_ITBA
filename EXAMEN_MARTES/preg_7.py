# Determine qué archivo de formato excel generará este programa 
# (https://imgur.com/YmCo6TX).

import pandas as pd
import numpy as np

tabla = np.array([[4,6,5], [8,8,8], [5,7,8]]) 
df =  pd.DataFrame(tabla, columns=["Matemática", "Física", "Química"])

df2 = pd.DataFrame(df, columns['Química', 'Matemática'])
df2 = to_excel("Alumnos.xlsx")

# Alumnos.xlsx
# Matemática	Física	Química
# 0	4	6	5
# 1	8	8	8
# 2	5	7	8

# ¿Qué hace df2 = pd.DataFrame(df, columns['Química', 'Matemática'])?
# df2 = pd.DataFrame(df, columns['Química', 'Matemática'])
# genera un nuevo dataframe con las columnas "Química" y "Matemática" del dataframe df.

# ¿Qué hace df2 = to_excel("Alumnos.xlsx")?
# df2 = to_excel("Alumnos.xlsx")
# guarda el dataframe df2 en el archivo excel "Alumnos.xlsx".

# ¿Qué hace df =  pd.DataFrame(tabla, columns=["Matemática", "Física", "Química"])?
# df =  pd.DataFrame(tabla, columns=["Matemática", "Física", "Química"])
# genera un dataframe con las columnas "Matemática", "Física" y "Química" a partir de la tabla.

# ¿Qué hace tabla = np.array([[4,6,5], [8,8,8], [5,7,8]])?
# tabla = np.array([[4,6,5], [8,8,8], [5,7,8]])
# genera una tabla con los valores 4,6,5,8,8,8,5,7,8.

# ¿Qué hace import numpy as np?
# import numpy as np
# importa la librería numpy y la renombra como np.

# ¿Qué hace import pandas as pd?
# import pandas as pd
# importa la librería pandas y la renombra como pd.



