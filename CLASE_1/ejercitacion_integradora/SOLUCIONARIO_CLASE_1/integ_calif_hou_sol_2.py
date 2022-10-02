# Solución 2 - Con funciones propias de la libreria pandas

import pandas as pd

viviendas = pd.read_excel("california_housing_train.xlsx") 

#Pregunta 1 y 2 (utilizando filtrado)
filtro_lon = (-120 <= viviendas['longitude']) & (viviendas['longitude'] <= -118)
filtro_val = viviendas['median_house_value'] > 80000
q_viviendas_en_zona = viviendas[filtro_lon & filtro_val].count().iloc[0]
print(q_viviendas_en_zona)
q_habitaciones = viviendas[filtro_lon & filtro_val]['total_rooms'].sum()
print(q_habitaciones/q_viviendas_en_zona)

#Pregunta 1 y 2 (sin utilizar filtrado)
ans = 0
hab = 0
for i,lon in enumerate(viviendas['longitude']):
    if -120 <= lon and lon<=-118 :
        if viviendas['median_house_value'][i] > 80000:
            ans+=1
            hab+=viviendas['total_rooms'][i]
print(ans)
print(hab/ans)

#Pregunta 3
valor_mas_caro = viviendas['median_house_value'].max()
casas_mas_caras = viviendas[viviendas['median_house_value'] == valor_mas_caro]['median_house_value'].count()
print(valor_mas_caro)
print(casas_mas_caras)

#pregunta 4
media = viviendas['median_house_value'].mean()
varianza = viviendas['median_house_value'].var()
print(media)
print(varianza)


# ###############################################################################

