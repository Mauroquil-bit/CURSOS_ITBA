"""
★  Copy
Temas:
Uso de librerías
Manejo de archivos
Armar una función que copie un archivo .xlsx, 
y lo guarde como "Copia 1 - nombre", 
de ya existir debe guardarlo como Copia 2 -, Copia 3 - , ...
Usar la libreria os para chequear si existe el archivo. 
Tips:
os.path.exists(nombre) devolverá True si ya existe
Se puede importar con: import os
"""

import os

def copiar_archivo(nombre):
    if os.path.exists(nombre):
        print("El archivo ya existe")
        nombre = "Copia 1 - " + nombre
    else:
        print("El archivo no existe")
    return nombre

print(copiar_archivo("Tabla1.xlsx"))

# El archivo no existe
# Tabla1.xlsx

# El archivo ya existe
# Copia 1 - Tabla1.xlsx

