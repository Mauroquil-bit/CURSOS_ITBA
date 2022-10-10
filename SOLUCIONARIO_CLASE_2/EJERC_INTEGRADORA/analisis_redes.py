# 

import json
import matplotlib.pyplot as plt

json_file = open('youtube_data.json')
data = json.load(json_file)

day = []
emw = []
views = []
likes = []
subs = []

# Organizo la información
for day_info in data['rows']:
  day.append(day_info[0])
  emw.append(day_info[1])
  views.append(day_info[2])
  likes.append(day_info[3])
  subs.append(day_info[4])

# Determino el cambio diario
emw_change = [emw[i] - emw[i-1] for i in range(1, len(emw))]
views_change = [views[i] - views[i-1] for i in range(1, len(views))]
likes_change = [likes[i] - likes[i-1] for i in range(1, len(likes))]
subs_change = [subs[i] - subs[i-1] for i in range(1, len(subs))]

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=(12, 10))

ax1.plot(day, emw)
i = emw_change.index( max(emw_change) ) + 1  # Máximo cambio
ax1.plot(day[i], emw[i], 'ko', label = 'Máximo cambio: {}\n Día: {}'.format(emw[i],day[i]))
ax1.set_title('Estimated Minutes Watched')
ax1.grid()
ax1.legend()

ax2.plot(day, views)
i = views_change.index( max(views_change) ) + 1
ax2.plot(day[i], views[i], 'ko', label = 'Máximo cambio: {}\n Día: {}'.format(views[i],day[i]))
ax2.set_title('Views')
ax2.grid()
ax2.legend()

ax3.plot(day, likes)
i = likes_change.index( max(likes_change) ) + 1
ax3.plot(day[i], likes[i], 'ko', label = 'Máximo cambio: {}\n Día: {}'.format(likes[i],day[i]))
ax3.set_title('Likes')
ax3.grid()
ax3.legend()

ax4.plot(day, subs)
i = subs_change.index( max(subs_change) ) + 1
ax4.plot(day[i], subs[i], 'ko', label = 'Máximo cambio: {}\n Día: {}'.format(subs[i],day[i]))
ax4.set_title('Subscribers Gained')
ax4.grid()
ax4.legend()

fig.autofmt_xdate()
plt.show()

#######################################################

# ¿Qué hace import json?
# json es un módulo de Python que permite trabajar con archivos JSON.
# En este caso, se utiliza para leer el archivo JSON y convertirlo en un diccionario de Python.

# ¿Qué hace json.load(json_file)?
# json.load() es una función que permite leer un archivo JSON
#  y convertirlo en un diccionario de Python.

# ¿Qué hace day = []?
# day = [] es una lista vacía que se utiliza para almacenar los datos de la columna "day".

# ¿Qué hace day.append(day_info[0])?
# day.append(day_info[0]) es una instrucción que permite agregar un elemento a la lista day.

# ¿Qué hace fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=(12, 10))?
# fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, figsize=(12, 10)) 
# es una instrucción que permite crear 4 gráficos en una misma figura.

# ¿Qué hace ax1.plot(day, emw)?
# ax1.plot(day, emw) es una instrucción que permite graficar los datos 
# de la columna "day" en el eje x
#  y los datos de la columna "emw" en el eje y.

# ¿Qué hace ax1.set_title('Estimated Minutes Watched')?
# ax1.set_title('Estimated Minutes Watched') es una instrucción que permite
#  agregar un título al gráfico.

# ¿Qué hace ax1.grid()?
# ax1.grid() es una instrucción que permite agregar una grilla al gráfico.

# ¿Qué hace ax1.legend()?
# ax1.legend() es una instrucción que permite agregar una leyenda al gráfico.

# ¿Qué hace fig.autofmt_xdate()?
# fig.autofmt_xdate() es una instrucción que permite rotar las etiquetas del eje x.

# ¿Qué hace plt.show()?
# plt.show() es una instrucción que permite mostrar los gráficos.

# ¿Qué hace i = emw_change.index( max(emw_change) ) + 1?
# i = emw_change.index( max(emw_change) ) + 1 es una instrucción que permite
#  determinar el índice del elemento máximo de la lista emw_change.

# ¿Qué hace ax1.plot(day[i], emw[i], 'ko', label = 'Máximo cambio: {}\n Día: {}'.format(emw[i],day[i]))?
# ax1.plot(day[i], emw[i], 'ko', label = 'Máximo cambio: {}\n Día: {}'.format(emw[i],day[i]))
# es una instrucción que permite graficar el elemento máximo de la lista emw_change.

# ¿Qué hace ax1.legend()?
# ax1.legend() es una instrucción que permite agregar una leyenda al gráfico.







