# Solución 1

def isNaN(num):
   return num != num


def numeralizar(datos):
  datosNumeralizados=[]
  for i in range(len(datos)):
    dato = datos[i]
    if not(isNaN(dato)) and dato != "Ausente":
        datosNumeralizados.append(int(dato))
  return datosNumeralizados


! wget "https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/NotasFinitos.csv"

import pandas as pd
import matplotlib.pyplot as plt
datos = pd.read_csv("NotasFinitos.csv") 

notas1 = datos['1P']
notas2 = datos['2P']
notas3 = datos['3P']

parcial1=numeralizar(notas1)
parcial2=numeralizar(notas2)
parcial3=numeralizar(notas3)


intervalos_superiores=[30,60,90,120,140]
nombreDeDatasets=['Parcial 1','Parcial 2','Parcial 3']
plt.hist([parcial1,parcial2,parcial3], bins=intervalos_superiores ,label=nombreDeDatasets)
plt.legend(loc="upper right")
plt.show()

_=plt.boxplot([parcial1,parcial2,parcial3]) 
# ax1.show()

########################################################

# ¿Qué hace datos = pd.read_csv("NotasFinitos.csv")?
# Lee el archivo NotasFinitos.csv y lo guarda en la variable datos

# ¿Qué hace la función isNaN(num)?
# Devuelve True si el valor de num es NaN, False en caso contrario
# NaN es un valor especial que representa "Not a Number"

# ¿Qué hace la función numeralizar(datos)?
# Recibe una lista de datos y devuelve una lista con los datos que no son NaN

# ¿Que hace datosNumeralizados.append(int(dato))?
# Convierte el dato a entero y lo agrega a la lista datosNumeralizados

# ¿Que hace datosNumeralizados=[]?
# Crea una lista vacía

# ¿Que hace for i in range(len(datos))?
# Recorre la lista datos

# ¿Que hace dato = datos[i]?
# Asigna a la variable dato el valor de la posición i de la lista datos

# ¿Que hace if not(isNaN(dato)) and dato != "Ausente":
# Si el dato no es NaN y no es "Ausente" entonces lo agrega a la lista datosNumeralizados

# ¿Que hace datosNumeralizados.append(int(dato))?
# Convierte el dato a entero y lo agrega a la lista datosNumeralizados

# ¿Qué hace notas1 = datos['1P']?
# Asigna a la variable notas1 la columna 1P del dataframe datos

# ¿Qué hace notas2 = datos['2P']?
# Asigna a la variable notas2 la columna 2P del dataframe datos

# ¿Qué hace notas3 = datos['3P']?
# Asigna a la variable notas3 la columna 3P del dataframe datos

# ¿Qué hace parcial1=numeralizar(notas1)?
# Asigna a la variable parcial1 el resultado de la función numeralizar aplicada a la variable notas1

# ¿Qué hace parcial2=numeralizar(notas2)?
# Asigna a la variable parcial2 el resultado de la función numeralizar aplicada a la variable notas2

# ¿Qué hace parcial3=numeralizar(notas3)?
# Asigna a la variable parcial3 el resultado de la función numeralizar aplicada a la variable notas3

# ¿Qué hace intervalos_superiores=[30,60,90,120,140]?
# Crea una lista con los valores 30, 60, 90, 120 y 140

# ¿Qué hace nombreDeDatasets=['Parcial 1','Parcial 2','Parcial 3']?
# Crea una lista con los valores "Parcial 1", "Parcial 2" y "Parcial 3"

# ¿Qué hace plt.hist([parcial1,parcial2,parcial3], bins=intervalos_superiores ,label=nombreDeDatasets)?
# Grafica un histograma con los datos de las listas parcial1, 
# parcial2 y parcial3, 
# con los intervalos superiores dados por la lista intervalos_superiores y con las etiquetas de los datasets dados por la lista nombreDeDatasets

# ¿Qué hace plt.legend(loc="upper right")?
# Muestra la leyenda del gráfico en la posición superior derecha

# ¿Qué hace plt.show()?
# Muestra el gráfico

# ¿Qué hace _=plt.boxplot([parcial1,parcial2,parcial3])?
# Grafica un diagrama de caja con los datos de las listas parcial1, parcial2 y parcial3

# ¿Qué hace plt.show()?
# Muestra el gráfico

