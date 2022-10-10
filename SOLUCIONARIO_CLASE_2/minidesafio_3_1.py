# Mini desafío 3
# Visualizar usando un piechart la cuota de mercado de diferentes compañías que ofrecen un producto (por ejemplo: marcas de celulares). 
# Buscar en internet los valores actuales para el producto que eligieron.
# Averiguar el color favorito de caramelos Sugus de diferentes amigos o conocidos y visualizar la información con un gráfico piechart, 
# mostrando los colores de cada sección que corresponden al color de caramelo.

# Parte 1

import matplotlib.pyplot as plt

labels = ('Apple', 'Samsung', 'Huawei', 'Xiaomi', 'vivo', 'Oppo', 'Lenovo', 'Otros')
sizes = [72.3, 70.4, 56.2, 32.9, 31.5, 31.4, 11.7, 94.7] #Millones de unidades: 2019 Q4
colors = ['silver', 'royalblue', 'orangered', 'orange', 'cornflowerblue', 'green', 'red', 'grey']

fig = plt.figure(figsize=(6, 6))

plt.pie(sizes, labels=labels, colors=colors, autopct='%5.01f%%', pctdistance=0.85, startangle = 90)

# Dibujar un círculo blanco para mejorar la estética del gráfico
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

plt.show()

########################################################################

# 
# ¿Qué es un piechart?
#
# Un piechart es un gráfico circular que muestra la proporción de cada categoría en un conjunto de datos.
#
# ¿Cómo se usa?
#
# Se usa para mostrar la proporción de cada categoría en un conjunto de datos.
#
# ¿Que hace el código?

# Importamos la librería matplotlib.pyplot
import matplotlib.pyplot as plt

# Definimos las etiquetas de cada categoría
labels = ('Apple', 'Samsung', 'Huawei', 'Xiaomi', 'vivo', 'Oppo', 'Lenovo', 'Otros')

# Definimos el tamaño de cada categoría
sizes = [72.3, 70.4, 56.2, 32.9, 31.5, 31.4, 11.7, 94.7] #Millones de unidades: 2019 Q4

# Definimos los colores de cada categoría
colors = ['silver', 'royalblue', 'orangered', 'orange', 'cornflowerblue', 'green', 'red', 'grey']

# Definimos el tamaño del gráfico
fig = plt.figure(figsize=(6, 6))

# Dibujamos el gráfico
plt.pie(sizes, labels=labels, colors=colors, autopct='%5.01f%%', pctdistance=0.85, startangle = 90)

# Dibujamos un círculo blanco para mejorar la estética del gráfico
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Mostramos el gráfico
plt.show()

#########################################################################


 