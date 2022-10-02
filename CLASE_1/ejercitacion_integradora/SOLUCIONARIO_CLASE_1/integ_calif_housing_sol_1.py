# California Housing
# Temas:
# Analísis de información estructurada
# Librerías

# Solución 1

import pandas as pd
import numpy as np

archivo = pd.read_excel("california_housing_train.xlsx") 

#Pregunta 1 y 2 (utilizando filtrado)
ans = 0
hab = 0
filtro_lon = (-120 <= archivo['longitude']) & (archivo['longitude'] <= -118)
filtro_val = archivo['median_house_value'] > 80000
ans = len( archivo[filtro_lon & filtro_val] )
hab = sum(archivo[filtro_lon & filtro_val]['total_rooms'])
print(ans)
print(hab/ans)

#Pregunta 1 y 2 (sin utilizar filtrado)
ans = 0
hab = 0
for i,lon in enumerate(archivo['longitude']):
    if -120 <= lon and lon<=-118 :
        if archivo['median_house_value'][i] > 80000:
            ans+=1
            hab+=archivo['total_rooms'][i]
print(ans)
print(hab/ans)

#Pregunta 3
m = max(archivo['median_house_value'])
c = sum(archivo['median_house_value'] == m)
print(m)
print(c)

#pregunta 4
m = np.mean(archivo['median_house_value'])
v = np.var(archivo['median_house_value'])
print(m)
print(v)


###############################################################################

