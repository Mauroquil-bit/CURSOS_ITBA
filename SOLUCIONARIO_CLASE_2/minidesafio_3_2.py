# Parte 2

# Importamos la librería matplotlib.pyplot
import matplotlib.pyplot as plt

# Definimos las etiquetas de cada categoría
labels = ('Frutilla', 'Menta', 'Anana', 'Limón', 'Manzana', 'Naranja')
sizes = [10, 6, 2, 9, 4, 1]
colors = ['red', 'green', 'blue', 'yellow', 'lime', 'orange']

# Definimos el tamaño del gráfico
fig = plt.figure(figsize=(6, 6))

# Dibujamos el gráfico
plt.pie(sizes, labels=labels, colors=colors, autopct='%5.01f%%', pctdistance=0.85, startangle=0)

# Dibujar un círculo blanco para mejorar la estética del gráfico
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig.gca().add_artist(centre_circle)

# Mostramos el gráfico
plt.show()


##########################################################

