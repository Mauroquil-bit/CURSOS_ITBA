# Mini desafio 1.C - Extra Challenge
# Determinar qué equipos obtuvieron mas de 20 puntos, 
# y mostrar sus diferencias de goles
# Plus: ordenar los equipos de mayor a menor en puntaje (de forma descendiente)

import pandas as pd

tabla_de_puntajes = pd.read_excel("Tabla1.xlsx")

print('Todos los equipos')
for indice, equipo in tabla_de_puntajes.iterrows():
  print(equipo['Equipo'], 'obtuvo un puntaje de', equipo['Puntos'], ', y su diferencia de goles es de:', equipo['Goles a favor'] - equipo['Goles en contra'])
print()

# Nos quedamos solo con los equipos con puntaje mayor que 20
# Utilizamos la función iloc, debido a que el resultado propio de pandas nos devuelve las filas del DataFrame que cumplen con lo pedido. 
# Nosotros queremos la 1ra, que es la única fila
equipos_top = tabla_de_puntajes[tabla_de_puntajes['Puntos'] > 20]
print("Equipos top")
for indice, equipo in equipos_top.iterrows():
  print(equipo['Equipo'], 'obtuvo un puntaje de', equipo['Puntos'], ', y su diferencia de goles es de:', equipo['Goles a favor'] - equipo['Goles en contra'])
print()

# Para el plus, tenemos que ordenar los equipos segun el puntaje que sacaron. 
# Por defecto, se ordena de menor a mayor.
#  Como queremos de mayor a menor, le indicaremos que el ordenamiento no sea en formato
equipos_top_ordenados = equipos_top.sort_values(by=['Puntos'], ascending=False)
print("Equipos top ordenados")
for indice, equipo in equipos_top_ordenados.iterrows():
  print(equipo['Equipo'], 'obtuvo un puntaje de', equipo['Puntos'], ', y su diferencia de goles es de', equipo['Goles a favor'] - equipo['Goles en contra'])


###########################################################################

