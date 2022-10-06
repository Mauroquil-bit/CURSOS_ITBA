# Una empresa registra en una base de datos cada vez que recibe un reclamo de sus clientes. 
# Esta base de datos tiene en la columna "Categoría" el tipo de reclamo, 
# y ahora desea averiguar cuál es el tipo de reclamo que ocurre más seguido 
# ¿Cuál de los siguientes comandos cumple esta función?

# archivo['Categoría'].value_counts().idxmax()
# archivo['Categoría'].value_counts().max()
# archivo['Categoría'].idxmax().value_counts()
# archivo['Categoría'].max().value_counts()

# ¿Cuál de los siguientes comandos cumple esta función?
# archivo['Categoría'].value_counts().idxmax()
# archivo['Categoría'].value_counts().max()
# archivo['Categoría'].idxmax().value_counts()
# archivo['Categoría'].max().value_counts()

# Respuesta:
# archivo['Categoría'].value_counts().idxmax()

# Explicación:
# archivo['Categoría'].value_counts().idxmax() devuelve el valor de la categoría que más se repite
# archivo['Categoría'].value_counts().max() devuelve la cantidad de veces que se repite la categoría que más se repite
