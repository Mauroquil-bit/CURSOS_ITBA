# Conociendo el funcionamiento de .values_counts() de Pandas: 
# ¿Cuál es la salida del siguiente programa(https://imgur.com/FbMrCyu) con la base de datos: 
# https://www.kaggle.com/brendan45774/test-file/version/6)?
#

# ¿Cuál es la salida del siguiente programa?

import pandas as pd
tabla = pd.read_csv("https://www.kaggle.com/datasets/brendan45774/test-file/version/6")
print(tabla["Pclass"].value_counts(normalize=True, ascending=True))

# 3    0.551066
# 2    0.242424
# 1    0.206510
# Name: Pclass, dtype: float64




