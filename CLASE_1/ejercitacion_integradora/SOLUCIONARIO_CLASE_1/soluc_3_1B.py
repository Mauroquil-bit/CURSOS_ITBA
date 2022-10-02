# Solución 3 - 
# Esta solución requiere una mayor comprensión de DataFrames, 
# pero resulta más fácil de entender para el expectador, 
# ya que no requiere de ciclos dentro del código de uno, 
# sino que utiliza una función propia de pandas

import pandas as pd

tabla_de_puntajes = pd.read_excel("Tabla1.xlsx") 

# Buscamos al campeón, que es el que mayor puntaje obtuvo de todos los participantes. 
# Utilizamos la función iloc, debido a que el resultado propio de pandas nos devuelve las filas del DataFrame que cumplen con lo pedido. 
# Nosotros queremos la 1ra, que es la única fila
campeon = tabla_de_puntajes[tabla_de_puntajes['Puntos'] == tabla_de_puntajes['Puntos'].max()].iloc[0]

#Buscamos al que quedó último, que es el que menor puntaje obtuvo de todos los participantes
# Utilizamos la función iloc, debido a que el resultado propio de pandas nos devuelve las filas del DataFrame que cumplen con lo pedido. 
# Nosotros queremos la 1ra, que es la única fila
peor = tabla_de_puntajes[tabla_de_puntajes['Puntos'] == tabla_de_puntajes['Puntos'].min()].iloc[0]

print(campeon['Equipo'], 'resultó campeón con', campeon['Puntos'])
print(peor['Equipo'], 'resultó último con', peor['Puntos'])


###########################################################################



