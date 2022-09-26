"""
El tiempo es dinero
Temas:
Analisís de información estructurada
Librerías
La administración del dinero es una tarea que requiere una altísima fiabilidad. 
En esta ocasión tu objetivo será programar un script que actualize la cantidad de dinero de una serie de usuarios a partir de la información de las transferencias que fueron realizadas. 
Más concretamente recibiras una base de datos con la cantidad de dinero de una serie de usuarios, 
un base de datos con una serie de transferencias que los usuarios se realizan entre si, 
y deberás generar con eso una nueva base de datos con el dinero actualizado de cada usuario.
Importar el archivo Finanzas.xlsx que contiene la cantidad de dinero de los usuarios y las transferencias en dos hojas de archivo.
Exportar un archivo usuarios_actualizados.xlsx que contiene las cantidades de dinero actualizadas.
"""

import pandas as pd

df_usuarios = pd.read_excel("Finanzas.xlsx", sheet_name="Usuarios")

df_transferencias = pd.read_excel("Finanzas.xlsx", sheet_name="Transferencias")

df_usuarios.set_index("Usuario", inplace=True)

for i in range(len(df_transferencias)):
    usuario_origen = df_transferencias.iloc[i, 0]
    usuario_destino = df_transferencias.iloc[i, 1]
    monto = df_transferencias.iloc[i, 2]
    df_usuarios.loc[usuario_origen, "Dinero"] -= monto
    df_usuarios.loc[usuario_destino, "Dinero"] += monto

df_usuarios.to_excel("usuarios_actualizados.xlsx")

print(df_usuarios)
print(df_transferencias)

# print(df_usuarios.loc["Usuario1", "Dinero"])

# print(df_transferencias.iloc[0, 0])

# print(df_transferencias.iloc[0, 1])

# print(df_transferencias.iloc[0, 2])

# print(df_transferencias.iloc[1, 0])

# print(df_transferencias.iloc[1, 1])

# print(df_transferencias.iloc[1, 2])

# print(df_transferencias.iloc[2, 0])

