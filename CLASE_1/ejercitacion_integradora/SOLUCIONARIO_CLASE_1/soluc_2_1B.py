# Solución 2 - 
# Esta solución es un poco más práctica y versátil

import pandas as pd

archivo = pd.read_excel("Tabla1.xlsx", index_col ="Equipo") 
# Indicamos que la columna de indexación será Equipo.

data = archivo.to_dict("index")

data_tuple = data.items() # provocamos que los datos esten como una lista de la forma (clave, contenido)

def criterioDeOrden(item): # esta función determina el criterio de orden
    clave, contenido = item
    return contenido["Puntos"] # indicamos que al criterio le importa los puntos

data_ordenada = sorted(data_tuple, reverse=True, key=criterioDeOrden)

ganador = data_ordenada[0][0] # el primer 0 indica que es el primer elemento (el ganador), el segundo 0 indica que nos interesa la clave (si fuera un 1 sería el contenido)
perdedor = data_ordenada[-1][0] # el primer -1 indica que es el utimo elemento (el perdedor), el segundo 0 indica que nos interesa la clave (si fuera un 1 sería el contenido)

print(ganador,"resulto campeón con",data[ganador]["Puntos"],"puntos")
print(perdedor,"resulto último con", data[perdedor]["Puntos"],"puntos")

###########################################################################

# ¿Qué hace archivo = pd.read_excel("Tabla1.xlsx", index_col ="Equipo")?
# archivo = pd.read_excel("Tabla1.xlsx", index_col ="Equipo")
# lee el archivo excel "Tabla1.xlsx" y lo guarda en la variable archivo. Además, indica que la columna de indexación será Equipo.

# ¿Qué hace data = archivo.to_dict("index")?
# data = archivo.to_dict("index")
# convierte el dataframe archivo en un diccionario y lo guarda en la variable data.

# ¿Qué hace data_tuple = data.items()?
# data_tuple = data.items()
# convierte el diccionario data en una lista de tuplas y lo guarda en la variable data_tuple.

# ¿Qué hace def criterioDeOrden(item)?
# def criterioDeOrden(item):
# define una función que se llama criterioDeOrden y recibe un parámetro llamado item.

# ¿Qué hace clave, contenido = item?
# clave, contenido = item
# desempaqueta el parámetro item en dos variables llamadas clave y contenido.

# ¿Qué hace return contenido["Puntos"]?
# return contenido["Puntos"]
# devuelve el valor de la clave "Puntos" del diccionario contenido.

# ¿Qué hace data_ordenada = sorted(data_tuple, reverse=True, key=criterioDeOrden)?
# data_ordenada = sorted(data_tuple, reverse=True, key=criterioDeOrden)
# ordena la lista de tuplas data_tuple en orden descendente según el criterio de orden definido por la función criterioDeOrden y lo guarda en la variable data_ordenada.

# ¿Qué hace ganador = data_ordenada[0][0]?
# ganador = data_ordenada[0][0]
# guarda en la variable ganador el primer elemento de la lista data_ordenada y luego el primer elemento de la tupla que se encuentra en la posición 0 de la lista data_ordenada.

# ¿Qué hace perdedor = data_ordenada[-1][0]?
# perdedor = data_ordenada[-1][0]
# guarda en la variable perdedor el último elemento de la lista data_ordenada y luego el primer elemento de la tupla que se encuentra en la posición -1 de la lista data_ordenada.

# ¿Qué hace print(ganador,"resulto campeón con",data[ganador]["Puntos"],"puntos")?
# print(ganador,"resulto campeón con",data[ganador]["Puntos"],"puntos")
# imprime el nombre del ganador, la frase "resulto campeón con", los puntos del ganador y la palabra "puntos".



