"""
En un DataFrame es posible filtrar los datos según alguna condición. 
Esto se realiza de la siguiente manera:
dataframe[ (condición_1) & / | (condición_2) & / | (condición_3) ... ]
Donde dice & / | porque se puede elegir escribir & para hacer un and, 
o se puede escribir | para hacer un or. 
Recordar que un and es verdadero si se cumplen ambas condiciones, 
mientras que un or lo es si se cumple alguna de ellas. 
Notar también que las condiciones se escriben dentro de paréntesis.
Las condiciones siguien el siguiente formato:
dataframe[ propiedad ] >/</<=/... (número)
Nota: No debe ser una comparación sí o sí con un numero, 
se puede comparar contra cualquier cosa mientras estén definidas las comparaciones (mayor, menor, mayor o igual, igual, etc.).
Veamos un ejemplo extrayendo todos los alumnos que hayan aprobado química (nota >= 4):
"""


import pandas as pd

datos = pd.read_excel("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Datos.xlsx") 
print("Datos:\n")
print(datos)

# No es necesario usar paréntesis si hay una única condición
aprobados = datos[ datos['Quimica'] >= 4 ] 
print("\nAprobados en Química:\n")
print(aprobados)

# No es necesario usar paréntesis si hay una única condición
