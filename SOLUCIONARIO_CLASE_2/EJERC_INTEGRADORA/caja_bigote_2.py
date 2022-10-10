# Solución 2: utilizando propiedades de pandas

def isNaN(num):
   return num != num

import pandas as pd
import matplotlib.pyplot as plt
datos = pd.read_csv("NotasFinitos.csv") 

notas1 = datos.loc[~isNaN(datos['1P']) & (datos['1P'] != 'Ausente'), '1P']
notas2 = datos.loc[~isNaN(datos['2P']) & (datos['2P'] != 'Ausente'), '2P']
notas3 = datos.loc[~isNaN(datos['3P']) & (datos['3P'] != 'Ausente'), '3P']


intervalos_superiores=[30,60,90,120,140]
nombreDeDatasets=['Parcial 1','Parcial 2','Parcial 3']
plt.hist([parcial1,parcial2,parcial3], bins=intervalos_superiores ,label=nombreDeDatasets)
plt.legend(loc="upper right")
plt.show()

_=plt.boxplot([parcial1,parcial2,parcial3]) 
# ax1.show()


# ¿Qué hace datos = pd.read_csv("NotasFinitos.csv")?
# Lee el archivo NotasFinitos.csv y lo guarda en la variable datos

# ¿Qué hace la función isNaN(num)?
# Devuelve True si el valor de num es NaN, False en caso contrario
# NaN es un valor especial que representa "Not a Number"

# ¿Que hace pandas as pd?
# Importa la librería pandas y la renombra como pd

# ¿Que hace matplotlib.pyplot as plt?
# Importa la librería matplotlib.pyplot y la renombra como plt

# ¿Qué hace notas1 = datos.loc[~isNaN(datos['1P']) & (datos['1P'] != 'Ausente'), '1P']?
# Asigna a la variable notas1 la columna 1P del dataframe datos, filtrando los valores NaN y Ausente
# ¿Qué hace ~isNaN(datos['1P'])?
# Devuelve True si el valor de la columna 1P no es NaN, False en caso contrario
# ¿Qué hace ~?
# Devuelve el valor opuesto de lo que le sigue
# ¿Que hace ~isNaN?


