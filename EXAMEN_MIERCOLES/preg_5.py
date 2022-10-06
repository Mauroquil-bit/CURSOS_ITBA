# Luego de finalizar la inscripción a un evento se quiere analizar los datos 
# de la misma, para ello la información del formulario fue exportada a un archivo
# y se quiere usar este simple código para analizar el dominio de correo electrónico más utilizado 
# ¿Cuál de los siguientes gráficos fue generado usando este programa?

import matplotlib.pyplot as plt
import pandas as pd

archivo = pd.read_csv('Inscripción (respuestas).xlsx')
correos = archivo['Dirección de correo electrónico']
dominios = correos.str.split('@').str[1]

dominios_dic = {}
for k, v in dominios.value_counts().iteritems():
    if v > 20:
        dominios_dic[k] = v
    else:
        dominios_dic['Otros'] = dominios_dic.get('Otros', 0) + v

plt.pie(dominios_dic.values(), labels=dominios_dic.keys(), startangle=90)
plt.title('Dominios de correo electrónico')
plt.show()

# Respuesta:
# El gráfico que fue generado usando este programa es el de la derecha.
# ¿Qué hace este programa?

# Este programa lee un archivo csv y lo convierte en un diccionario.
# Luego grafica los datos del diccionario.
# ¿Qué imprime?


# ¿Qué hace import matplotlib.pyplot as plt?
# importa la librería matplotlib.pyplot y la renombra como plt
# ¿Qué hace import pandas as pd?
# importa la librería pandas y la renombra como pd
# ¿Qué hace archivo = pd.read_csv('Inscripción (respuestas).xlsx')?
# lee el archivo csv y lo guarda en la variable archivo
# ¿Qué hace correos = archivo['Dirección de correo electrónico']?
# guarda en la variable correos los datos de la columna Dirección de correo electrónico
# ¿Qué hace dominios = correos.str.split('@').str[1]?
# guarda en la variable dominios los datos de la columna Dirección de correo electrónico
# ¿Qué hace dominios_dic = {}?
# crea un diccionario vacío
# ¿Qué hace for k, v in dominios.value_counts().iteritems()?
# recorre el diccionario dominios.value_counts()
# ¿Qué hace if v > 20?

# ¿Qué hace plt.pie(dominios_dic.values(), labels=dominios_dic.keys(), startangle=90)?
# grafica los datos del diccionario dominios_dic
# ¿Qué hace plt.title('Dominios de correo electrónico')?
# agrega un título al gráfico
# ¿Qué hace plt.show()?
# muestra el gráfico

# Respuesta:
