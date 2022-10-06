# Un grupo de investigación está utilizando un instrumento de medición 
# para obtener datos de uno de los circuitos electrónicos con los que trabajan.
#  Los datos fueron exportados a un archivo y se quiere usar este simple código para visualizar los resultados 
# ¿Cuál de los siguientes gráficos fue generado usando este programa?

import matplotlib.pyplot as plt
import pandas as pd

archivo = pd.read_csv('respuesta_impulsiva.csv')
datos = archivo.to_dict('list')
time = datos['Time']
signal = datos['Amplitude']

plt.plot(time, signal, 'ko--')
plt.ylabel('Tensión [V]')
plt.xlabel('Tiempo [s]')
plt.grid()
plt.show()

# ¿Que hace plt.plot(time, signal, 'ko--')?
# plt.plot(time, signal, 'ko--')
# genera un gráfico de líneas con puntos

# ¿Que hace plt.ylabel('Tensión [V]')?
# plt.ylabel('Tensión [V]')
# agrega una etiqueta en el eje y

# ¿Que hace plt.xlabel('Tiempo [s]')?
# plt.xlabel('Tiempo [s]')
# agrega una etiqueta en el eje x

# ¿Que hace plt.grid()?
# plt.grid()
# agrega una cuadrícula al gráfico

# ¿Que hace plt.show()?
# plt.show()
# muestra el gráfico

# ¿Que hace archivo = pd.read_csv('respuesta_impulsiva.csv')?
# archivo = pd.read_csv('respuesta_impulsiva.csv')
# lee el archivo respuesta_impulsiva.csv

# ¿Que hace datos = archivo.to_dict('list')?
# datos = archivo.to_dict('list')
# convierte el archivo a un diccionario

# ¿Que hace time = datos['Time']?
# time = datos['Time']
# asigna los valores de la columna Time a la variable time

# ¿Que hace signal = datos['Amplitude']?
# signal = datos['Amplitude']
# asigna los valores de la columna Amplitude a la variable signal

# ¿Que hace plt.plot(time, signal, 'ko--')?
# plt.plot(time, signal, 'ko--')
# genera un gráfico de líneas con puntos





