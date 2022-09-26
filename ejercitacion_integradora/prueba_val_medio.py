import pandas as pd
import numpy as np

df = pd.read_excel("california_housing_train.xlsx") 

# ¿Cuantas casas hay con valor 'median_house_value' mayor a 80000 tomando de la longitud -120 a -118? Rta: 5466
# df = df[ (df['median_house_value'] > 80000) & (df['longitude'] > -120) & (df['longitude'] < -118) ]
# print('Cantidad de casas con valor "median_house_value" mayor a 80000 tomando de la longitud -120 a -118')
# print(len(df))