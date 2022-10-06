
import pandas as pd
tabla = pd.read_excel("LigaArgentina.xlsx")

lista = tabla[['Partidos']!=tabla['Partidos'].max()]

print(lista["Equipo"])

# ¿Qué hace lista = tabla[['Partidos']==tabla['Partidos'].max()]?
# lista = tabla[['Partidos']==tabla['Partidos'].max()]
# genera una lista con los equipos que tienen la mayor cantidad de partidos jugados.


# lista = tabla[['Partidos']!=tabla['Partidos'].max()]
# genera una lista con los equipos que no tienen la cantidad máxima de partidos jugados.

# ¿Qué hace print(lista["Equipo"]?
# print(lista["Equipo"])
# imprime la lista de equipos que no tienen la cantidad máxima de partidos jugados.

# ¿Qué hace tabla = pd.read_excel("LigaArgentina.xlsx")?
# tabla = pd.read_excel("LigaArgentina.xlsx")
# lee el archivo excel "LigaArgentina.xlsx" y lo guarda en la variable tabla.

# ¿Qué hace lista = tabla[['Partidos']!=tabla['Partidos'].max()]?
# lista = tabla[['Partidos']!=tabla['Partidos'].max()]
# genera una lista con los equipos que no tienen la cantidad máxima de partidos jugados.

# ¿Qué hace print(lista["Equipo"]?
# print(lista["Equipo"])
# imprime la lista de equipos que no tienen la cantidad máxima de partidos jugados.







