import pandas as pd

archivo = pd.read_excel("Tabla1.xlsx")
data = archivo.to_dict("list")
filas = len(data["Equipo"])
print("Diferencias de gol:")
for i in range(len(data["Equipo"])):
    print(data["Equipo"][i], ":", int(data["Goles a favor"][i] - data["Goles en contra"][i]))


