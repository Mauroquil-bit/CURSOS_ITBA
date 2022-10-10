# 

import pandas as pd

! wget "https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/NotasFinitos.csv"

def isNaN(num):
    return num != num

def getNota(estado):
  #Definimos la forma de tomar cada calificación
  if estado == 'Ausente':
    return 0
  if isNaN(estado):
    return 0
  return int(estado)
  
def aprobado(parcial1,parcial2,parcial3):
  #Definimos las condiciones de borde para aprobar
  if parcial1+parcial2+parcial3<160:
    return False
  if parcial1>=60 and parcial2>=60:
    return True
  elif parcial1>=60 and parcial3>=60:
    return True
  elif parcial2>=60 and parcial3>=60:
    return True
  else:
    return False



# usamos funciones de pandas (es decir no usamos to_dict, se podría resolver también usando to_dict)
datos = pd.read_csv("NotasFinitos.csv") 

notas = [datos['1P'], datos['2P'], datos['3P']]
N = len(notas[0]) # La cantidad de alumnos notasNumericas

sum = [0, 0, 0]                   #Aca guardamos la suma de los parciales
sumAprobados = [0, 0, 0]          #Aca guardamos la suma de los parciales de los alumnos aprobados
alumnosAprobados = 0

for i in range(len(notas[0])):    #Por cada alumno
  nota = [0, 0, 0]              
  for j in range(len(nota)):    
    nota[j] = getNota(notas[j][i])  #Obtengo sus notas de cada parcial
    sum[j] += nota[j]               #Y las sumo al total de TODOS los alumnos
  
  estaAprobado = aprobado(nota[0],nota[1],nota[2])
  if estaAprobado:                  #Si aparte esta aprobado
    alumnosAprobados += 1           #Aumento la cantidad de aprobados
    for j in range(len(sumAprobados)):  
      sumAprobados[j] += nota[j]    #Sumo sus notas al total de los alumnos aprobados
    
prom = []
for i in range(len(sum)):
  prom.append(sum[i]/N)             #Obtengo el promedio de TODOS los alumnos para cada parcial
  
promAprobados = []                  
for i in range(len(sumAprobados)):  #Por cada parcial
  promAprobados.append(sumAprobados[i]/alumnosAprobados) #Obtengo el promedio solo de los aprobados

print('Cantidad alumnos:',N, '  Cantidad alumnos aprobados:',alumnosAprobados)
print('Promedios para parciales: P1=',prom[0],'P2=',prom[1],'P3=',prom[2])
print('Promedios de los aprobados: P1=',promAprobados[0] ,'P2=',promAprobados[1],'P3=',promAprobados[2] )



