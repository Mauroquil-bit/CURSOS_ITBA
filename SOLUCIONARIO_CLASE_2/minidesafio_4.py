# Mini desafío 4
# Leer el archivo notas.xlsx 
# que tiene en el campo Notas los puntajes de alumnos en un examen (van de 0 a 10) y armar un histograma con los datos, 
# guardarlo en un archivo Notas.png

# Importamos la librería pandas y matplotlib.pyplot
import matplotlib.pyplot as plt
import pandas as pd

# Leemos el archivo notas.xlsx
archivo = pd.read_excel("CLASE_2\notas.xlsx") 

# Definimos el tamaño del gráfico
data = archivo.to_dict("list")

# Con plt.figure elegimos el tamaño del gráfico
plt.figure(figsize=(12, 5))

# Debemos elegir bins del 0 al 11 para que los intervalos de bins correspondan
# a los intervalos semi-abiertos:
# [0, 1) [1, 2) [2, 3) ... [10, 11)
# con align elegimos centrar los bins en el 'borde izquierdo' del intervalo
# Con rwidth controlamos el espesor de las barras
# Con zorder elegimos el orden en que se dibujan los elementos gráficos
plt.hist(data["notas"], range(12), align = 'left', rwidth=0.75, zorder=2)

# xticks de 1 en 1, yticks de 10 en 10
plt.xticks(range(0, 11))
plt.yticks(range(0, 130, 10))

# Grilla horizontal, linea punteada, detras del histograma
plt.grid(axis='y', linestyle='--', zorder=1)

plt.savefig('Notas.png')
plt.show()


#######################################################################

# ¿Qué hace archivo = pd.read_excel("notas.xlsx")?
# Lee el archivo notas.xlsx y lo guarda en la variable archivo

# ¿Qué hace data = archivo.to_dict("list")?
# Convierte el archivo en un diccionario y lo guarda en la variable data

# ¿Qué hace plt.figure(figsize=(12, 5))?
# Elegimos el tamaño del gráfico

# ¿Qué hace plt.hist(data["notas"], range(12), align = 'left', rwidth=0.75, zorder=2)?
# Dibuja el histograma con los datos de la columna notas del diccionario data

# ¿Qué hace plt.xticks(range(0, 11))?
# Elegimos los valores de los ticks en el eje x

# ¿Qué hace plt.yticks(range(0, 130, 10))?
# Elegimos los valores de los ticks en el eje y

# ¿Qué hace plt.grid(axis='y', linestyle='--', zorder=1)?
# Dibuja la grilla horizontal

# ¿Qué hace plt.savefig('Notas.png')?
# Guarda el gráfico en el archivo Notas.png

# ¿Qué hace plt.show()?
# Muestra el gráfico

# OSError: [Errno 22] Invalid argument: 'CLASE_2\notas.xlsx'
# ¿Qué significa este error?
# Que el archivo notas.xlsx no se encuentra en la carpeta CLASE_2




