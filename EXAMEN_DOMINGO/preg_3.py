# Siendo "pi" un punto de los puntos marcados en rojo en la figura, 
# se tiene el siguiente código. 
# ¿Cuál de las siguientes definiciones de "points" 
# reproduce el gráfico de la figura (sin los labels de cada punto)?:

import matplotlib.pyplot as plt

xi = [-1.00, -0.75, -0.50, -0.25, 0.00, 0.25, 0.50, 0.75, 1.00]
yi = [-1.00, -0.75, -0.50, -0.25, 0.00, 0.25, 0.50, 0.75, 1.00]

p0 = [-1.00, 0.00]
p1 = [0.00, 1.00]
p2 = [1.00, 0.00]
p3 = [0.00, -1.00]
p4 = [-1.00, -1.00]
p5 = [0.00, 0.00]
p6 = [1.00, 1.00]

pi = [xi, yi]
points = [p4, p3, p5, p1, p6, p2, p0, p4]
xCoord = []
yCoord = []

for i in range(len(points)):
    xCoord.append(points[i][0])
    yCoord.append(points[i][1])

plt.plot(xCoord, yCoord )
plt.plot(xCoord, yCoord, 'ro')
plt.show()

# ¿Que falta en el código para que se unan las líneas azules en forma de cuadrado?

# ¿Que falta en el código para que se unan las líneas azules en forma de cuadrado?

# ¿Qué hace 





