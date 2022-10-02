# Unificación de bases de datos

"""
El objetivo de este problema es unificar dos bases de datos que contienen mails. 
Esto quiere decir, tomar dos bases de datos de formato .csv: 
lista1.csv y lista2.csv y combinarlas en una misma base de datos listafinal.csv. 
El contenido de las bases de datos son listas de mails, que contienen mails y otras informaciones de distintos usuarios. Tener en cuenta que las dos bases de datos pueden tener informaciones distintas de los usuarios.
Recomendamos descargar los archivos para ver su contenido (Con excel pueden abrirlos, 
pensar que un csv es prácticamente equivalente a un excel).
"""

! wget "https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/lista1.csv" 
# primera lista de clientes

! wget "https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/lista2.csv"
# segunda lista de clientes

"""
Solución
Este es un problema con una solucion que puede parecer tediosa pero resuelve un problema muy común y su lógica luego puede aplicarse a otros casos similares.
La solución propuesta consiste en armar una nueva base de datos con los contenidos combinados de los usuarios acorde a la información extraida de las dos bases de datos originales.
Para esto se debe crear una nueva de base de datos unificada a la que le iremos progresivamente agregando los valores primero de la base de datos 1 lista1.csv y en segundo lugar los valores de la base de datos 2 lista2.csv.
Esta nueva de base de datos unificada tendrá la forma de un diccionario donde las claves serán los mails de los usuarios y el contenido la información de cada usuario (es decir el mismo formato que las bases de datos originales)
Hay que tener una consideración que es que en las bases de datos lista1.csv y lista2.csv la información que se tiene de los usuarios puede ser distinta. Por ejemplo, si en la lista1 tenemos como información la edad de los usuarios en una columna puede pasar que en la lista2 no este.
Entonces es importante ir almacenando en un set (todosloscampos) todos los campos (es decir las columnas) que vamos encontrando en un set que va almacenanado progresivamente todos los campos que vamos encontrando en las bases de datos. Tiene que ser un set para evitar la repetición de campos en la base de datos final.
"""

import pandas as pd

# aca almacenamos las bases de datos que vamos a unificar
listas = [ "lista1.csv", "lista2.csv" ]

# en este diccionario vamos a ir amlacenando la información de la base de datos unificada
# la clave son los mails, el contenido la información de los usuarios

clientes = dict() 

#en este set almacenamos todas las columnas que se van progresivamente encontrando
todosloscampos = set() #set=conjunto


for lista in listas: # iteramos todas las bases de datos 

    # leemos el contenido indexando por mail (es decir la clave de los diccionarios será el mail de los usuarios)
    archivo = pd.read_csv(lista, index_col =["Mail"])
    data = archivo.to_dict("index") 
    
    # mostramos en pantalla
    print("Base de datos", lista)
    print(archivo)

    # iteramos los mails de la base de datos
    for mail in data: 
        # si el mail es uno nuevo para nuetra base de datos unificada, lo inicializamos como un diccionario vacio sin información
        # la cual se la agregaremos despues
        # si el mail ya existe no es necesario, significa que lo vimos en una base de datos anterior

        if mail not in clientes: 
            clientes[mail] = dict() 
        
        # leemos todos los campos (las columnas) que tenemos del mail en la base de datos original que estamos procesando
        campos = data[mail]

        # iteramos todos los campos del mail encontrado, y le asignamos sus valores en la base de datos unificada
        for campo in campos:
            # le asignamos a "clientes" que es la base de datos unificada el campo actual
            # que esta en data[mail], que tiene la información de la base de datos que estamos procesando del
            # campo correspondiente 
            clientes[mail][campo] = data[mail][campo]

            # le agregamos al set de campos (columas) el campo encontrado
            # como es un set los repetidos no van a agregarse
            todosloscampos.add(campo)

    print("  ")
            
# Por ultimo escribimos el archivo final, colocando las claves de los elementos de la base unificada (es decir los mails)
# En la primera columna (por eso orient="index")

df = pd.DataFrame.from_dict(clientes, orient='index')

# Mostramos los resultados y los guardamos en un archivo final
print("Base de datos unificada")
print(df)

df.to_csv('listafinal.csv')


############################################################################################################

