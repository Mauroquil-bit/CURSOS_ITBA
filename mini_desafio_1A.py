#Leer el archivo Tabla1.xlsx que contiene los puntos de un campeonato. 
# El archivo tiene cuatro columnas:

#Equipo
#Puntos
#Goles a favor
#Goles en contra
#Determinar de cada equipo la diferencia de gol (goles a favor - goles en contra), 
# y mostrar todas las diferencias usando print.

#¿Cómo leer un archivo excel con Python usando pandas?

#Para leer un archivo excel con Python, usamos la función read_excel() de la librería pandas. 
# Esta función recibe como parámetro el nombre del archivo a leer. 
# Por ejemplo, si el archivo se llama Tabla1.xlsx, la función se llama así:

#import pandas as pd

#dif_goles = pd.read_excel('Tabla1.xlsx')

#¿Cómo leer una columna de un archivo excel con Python usando pandas?

#Para leer una columna de un archivo excel con Python, 
# usamos la función read_excel() de la librería pandas.
# Esta función recibe como parámetro el nombre del archivo a leer 
# y el nombre de la columna a leer.

# Por ejemplo, si el archivo se llama Tabla1.xlsx y la columna se llama Equipo,
# la función se llama así:

#import pandas as pd
#datos_xlsx = pd.read_excel('Tabla1.xlsx') # , usecols=['Equipo']
#print(datos_xlsx)


#¿Cómo agregar una columna al archivo excel?

#Para agregar una columna al archivo excel,
# usamos la función to_excel() de la librería pandas.
# Esta función recibe como parámetro el nombre del archivo a leer
# y el nombre de la columna a agregar.


#import pandas as pd
#archivo = pd.read_excel("Tabla1.xlsx")
#data = archivo.to_dict("list")
#filas = len(data["Equipo"])
#print("Diferencias de gol:")
#for i in range(len(data["Equipo"])):
#    print(data["Equipo"][i], ":", data["Goles a favor"][i] - data["Goles en contra"][i])



"""
import pandas as pd
archivo = pd.read_excel("Datos.xlsx") 
# La variable archivo es de un tipo de dato especial de pandas llamado 'DataFrame'
print(archivo)
"""

import pandas as pd

archivo = pd.read_excel("Tabla1.xlsx")
data = archivo.to_dict("list")
filas = len(data["Equipo"])
print("Diferencias de gol:")
for i in range(len(data["Equipo"])):
    print(data["Equipo"][i], ":", int(data["Goles a favor"][i] - data["Goles en contra"][i]))

print(archivo)







