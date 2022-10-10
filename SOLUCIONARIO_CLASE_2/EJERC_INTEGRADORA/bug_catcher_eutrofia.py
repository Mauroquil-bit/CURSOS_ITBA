# Bug Catcher y el disco de la Eutrofia

import numpy as np
import matplotlib.pyplot as plt
IzIo=0.1
zfNahuel = 56

# despeje (formula)
kNahuel=-np.log(IzIo)/zfNahuel
kRioArriba = 0.009

#despeje (formula)
zfRioArriba = -np.log(IzIo)/kRioArriba

print('Nahuel Huapi k=',kNahuel)
print('Rio Arriba k=',kRioArriba)

# valores de z a gráficar
z = np.arange(0,zfRioArriba,1)

I0= 700

# valores a gráficar
IzNahuel = I0*np.e**(-kNahuel*z)
IzRioArriba = I0*np.e**(-kRioArriba*z)

plt.figure(figsize=(15,9))
plt.plot(z, IzNahuel, "blue",label="Nahuel Huapi")
plt.plot(z, IzRioArriba, "cyan",label="Río arriba")
plt.ylabel("Intensidad Iz [W/m^2]")
plt.xlabel("Profundidad z [cm]")

plt.legend()                                #Habilitamos los labels
plt.title("Abajo con la fabrica")
plt.minorticks_on()
plt.grid(which='minor', linestyle=':', linewidth=0.2, color='black')
#Le asignamos el estilo a la grilla mayor
plt.grid(which='major', linestyle='-', linewidth=0.3, color='black')
plt.show()


