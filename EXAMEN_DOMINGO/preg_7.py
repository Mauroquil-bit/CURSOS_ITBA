#  Pregunta 7:


import pandas as pd

tabla = pd.read_csv("tested.csv")
print (tabla['Pclass'].value_counts(normalize=True, ascending=True))

# ¿Qué hace tabla['Pclass'].value_counts(normalize=True, ascending=True)?
# Cuenta la cantidad de veces que aparece cada valor de la columna Pclass,
# y los ordena de menor a mayor, y los divide por la cantidad total de valores
# de la columna Pclass


# AtributeError:  plt.plot(time, signal, 'b-', legend='Signal')
# ¿Qué hace AtributeError:  plt.plot(time, signal, 'b-', legend='Signal')?
# Muestra un error de que no existe el atributo legend en el método plot
# de la librería matplotlib.pyplot


# Grafica la señal signal en función del tiempo time, con una línea azul y
# con la leyenda "Signal"



