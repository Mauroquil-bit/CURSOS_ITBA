#Podemos ver que Pandas representa las celdas vacías con el texto "NaN" (Not a Number). 
# Podríamos filtrar estos valores de forma similar a los ejemplos anteriores. 
# Esta vez tendremos que usar un método específico para detectar que el valor no sea NaN:

import pandas as pd

datos2 = pd.read_excel("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Datos2.xlsx")

datos2_matematica = datos2[ (datos2['Matematica'].notna()) & (datos2['Matematica'] != 'A')  ]

datos2_matematica = datos2_matematica['Matematica'] # Nos quedamos con la columna de interés

print('Notas válidas en Matemática: ')
print(datos2_matematica)




