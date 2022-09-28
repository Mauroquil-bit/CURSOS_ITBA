"""
Es importante en este momento tomar en cuenta una limitación crucial que tiene la computación, 
el hecho de que la cantidad de información que puedo manejar es limitada ¿A qué nos referimos con esto? 
A que para graficar la función para todos los valores que puede tomar  x  entre  0  y  1 , 
se necesitaría infinita información ya que hay infinitos valores posibles de  x  en este intervalo, 
por lo tanto habrá infinitos valores de  y  que corresponden a cada uno de estos.
A partir de esta limitación surge la necesidad de "discretizar" la función. 
En lugar de graficar una curva perfecta para nuestra función, 
vamos a graficar solamente algunos puntos de ella, 
y los uniremos con lineas rectas. Si la cantidad de puntos que graficamos es lo suficientemente alta, 
la diferencia será imperceptible.
Vamos a hacer un ejemplo, crearemos cada uno de los puntos a graficar y para eso utilizaremos una lista de las coordenadas  x  de los puntos y otra lista de la misma longitud con las coordenadas  y  correspondientes, 
continuaremos usando el ejemplo anterior:  y=x2
"""

# Para este ejemplo elegimos valores de "x" a distancia 0.1 
x = [0.0, 0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9,  1.0]

# Los valores de "y" son los valores de "x" elevados al cuadrado
y = [0.0, 0.01, 0.04, 0.09, 0.16, 0.25, 0.36, 0.49, 0.64, 0.81, 1.0]

print(x)
print(y)

###########################################################################





