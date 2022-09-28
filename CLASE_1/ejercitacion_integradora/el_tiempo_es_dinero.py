""" El tiempo es dinero
Temas:
Analisís de información estructurada
Librerías
La administración del dinero es una tarea que requiere una altísima fiabilidad. 
En esta ocasión tu objetivo será programar un script que actualize la cantidad de dinero de una serie de usuarios a partir de la información de las transferencias que fueron realizadas. 
Más concretamente recibiras una base de datos con la cantidad de dinero de una serie de usuarios, un base de datos con una serie de transferencias que los usuarios se realizan entre si, 
y deberás generar con eso una nueva base de datos con el dinero actualizado de cada usuario.
Importar el archivo Finanzas.xlsx que contiene la cantidad de dinero de los usuarios y las transferencias en dos hojas de archivo.
Exportar un archivo usuarios_actualizados.xlsx que contiene las cantidades de dinero actualizadas.
"""

import pandas as pd
import numpy as np


usuarios_archivo = pd.read_excel("Finanzas.xlsx", "Usuarios",index_col="Usuario") 
#leemos los usuarios "indexados" por su nombre

transferencias_archivo = pd.read_excel("Finanzas.xlsx", "Transferencias")

# Generar una nueva base de datos con el dinero actualizado de cada usuario
# y exportarla a un archivo usuarios_actualizados.xlsx

#creamos un diccionario con los usuarios y sus cantidades de dinero
usuarios = {}
for i in range(len(usuarios_archivo)):
    usuarios[usuarios_archivo.index[i]] = usuarios_archivo.iloc[i,0]

#actualizamos las cantidades de dinero de los usuarios
for i in range(len(transferencias_archivo)):
    usuario_origen = transferencias_archivo.iloc[i,0]
    usuario_destino = transferencias_archivo.iloc[i,1]
    cantidad = transferencias_archivo.iloc[i,2]
    usuarios[usuario_origen] -= cantidad
    usuarios[usuario_destino] += cantidad

#creamos un dataframe con los usuarios y sus cantidades de dinero
usuarios_actualizados = pd.DataFrame.from_dict(usuarios, orient="index", columns=["Dinero"])

#exportamos el dataframe a un archivo excel
usuarios_actualizados.to_excel("usuarios_actualizados.xlsx")

print(usuarios_actualizados)


#fin del script

#############################################################################################################

