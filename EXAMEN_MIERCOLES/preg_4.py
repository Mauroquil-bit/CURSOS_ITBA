# Un grupo de investigación está utilizando un instrumento de medición 
# para obtener datos de uno de los circuitos electrónicos con los que trabajan. 
# Los datos fueron exportados a un archivo y se quiere usar este simple código 
# para visualizar los resultados 
# ¿Cuál de los siguientes gráficos fue generado usando este programa?

import matplotlib.pyplot as plt
import pandas as pd

archivo = pd.read_csv('step_response.csv')
datos = archivo.to_dict('list')
time = datos['Time']
signal = datos['Amplitud']

plt.plot(time, signal, 'b--')
plt.ylabel('Tensión [V]')
plt.xlabel('Tiempo [s]')
plt.grid()
plt.savefig('Plot 11_A.png', dpi=300)
plt.show()



# Respuesta:
# El gráfico que fue generado usando este programa es el de la izquierda.
# ¿Qué hace este programa?
# Este programa lee un archivo csv y lo convierte en un diccionario.
# Luego grafica los datos del diccionario.
# ¿Qué imprime?
# El programa grafica los datos del diccionario.
#
#
# ¿Qué hace import matplotlib.pyplot as plt?
# importa la librería matplotlib.pyplot y la renombra como plt
# ¿Qué hace import pandas as pd?
# importa la librería pandas y la renombra como pd
# ¿Qué hace archivo = pd.read_csv('step_response.csv')?
# lee el archivo csv y lo guarda en la variable archivo
# ¿Qué hace datos = archivo.to_dict('list')?
# convierte el dataframe archivo en un diccionario y lo guarda en la variable datos
# ¿Qué hace time = datos['Time']?
# guarda en la variable time los datos de la columna Time del diccionario datos
# ¿Qué hace signal = datos['Amplitud']?
# guarda en la variable signal los datos de la columna Amplitud del diccionario datos
# ¿Qué hace plt.plot(time, signal, 'b--')?
# grafica los datos de las variables time y signal
# ¿Qué hace plt.ylabel('Tensión [V]')?
# agrega el título Tensión [V] al eje y
# ¿Qué hace plt.xlabel('Tiempo [s]')?
# agrega el título Tiempo [s] al eje x
# ¿Qué hace plt.grid()?
# agrega una grilla al gráfico
# ¿Qué hace plt.savefig('Plot 11_A.png', dpi=300)?
# guarda el gráfico en un archivo png
# ¿Qué hace plt.show()?
# muestra el gráfico
#
#
# ¿Que hace el tercer argumento de plt.plot(time, signal, 'b--')?
# El tercer argumento de plt.plot(time, signal, 'b--') es el color y el tipo de línea.
# ¿Qué hace el tercer argumento 'b--'?
# El tercer argumento 'b--' es el color y el tipo de línea.
# ¿Qué hace 'b--'?
# 'b--' es el color y el tipo de línea.
# ¿Qué hace 'b'?
# 'b' es el color.
# ¿Qué hace 'b'?
# 'b' es el color.
# ¿Que color es 'b'?
# 'b' es el color azul.
# ¿Qué hace '--'?
# '--' es el tipo de línea.
# ¿Qué tipo de línea es '--'?
# '--' es una línea punteada.
# ¿Qué hace plt.ylabel('Tensión [V]')?

# El tercer argumento de plt.plot(time, signal, 'k--')
# ¿Qué hace el tercer argumento 'k--'?
# El tercer argumento 'k--' es el color y el tipo de línea.
# ¿Qué hace 'k'?
# 'k' es el color.
# ¿Qué color es 'k'?
# 'k' es el
# ¿Qué hace '--'?
# '--' es el tipo de línea.
# ¿Qué tipo de línea es '--'?
# '--' es una línea punteada.

# El tercer argumento de plt.plot(time, signal, 'b--')
# ¿Qué hace el tercer argumento 'b--'?
# El tercer argumento 'b--' es el color y el tipo de línea.
# ¿Qué hace 'b'?
# 'b' es el color.
# ¿Qué color es 'b'?
# 'b' es el color azul.
# ¿Qué hace '--'?
# '--' es el tipo de línea.
# ¿Qué tipo de línea es '--'?
# '--' es una línea punteada.

# ¿Qué hace plt.savefig('Plot 11_A.png', dpi=300)?
# guarda el gráfico en un archivo png
# ¿Qué hace dpi=300?
# dpi=300 es la resolución del archivo png.
# ¿Qué hace dpi=300?
# dpi=300 es la resolución del archivo png.






