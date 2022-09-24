# Esta solución es parecida a la de mini_desafio_2B.py, 
# pero en vez de usar un diccionario, usa un DataFrame.


import pandas as pd

datos = pd.read_excel("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Datos.xlsx")

promedios = (datos['Quimica'] + datos['Matematica'] + datos['Fisica']) / 3
print('Todos los promedios')
print(promedios)
print('El promedio maximo es', promedios.max())

# El promedio maximo es 8.666666666666666