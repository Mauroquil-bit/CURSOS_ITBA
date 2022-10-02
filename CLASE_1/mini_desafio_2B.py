#Mini desafío 2.B
#Escribir una funcion que reciba como parámetros: 
# una variable de tipo DataFrame (la tabla de alumnos) 
# y el índice de un alumno. Luego debe devolver con return el promedio de sus notas en las diferentes materias.

#Mini desafio 2B

import pandas as pd

def prom(df,indice):
    lst_materias = ['Quimica','Matematica','Fisica']
    alumno = df.loc[indice]
    
    suma = 0
    for i in lst_materias:
        suma += int(alumno[i])
        
    prom = suma/len(lst_materias)
    
    return prom
  
def main():
    df = pd.read_excel('Datos.xlsx')
    data_lst = df.to_dict("list")
    
    print('Indice (Ingrese un numero de 0 a {}): '.format(len(data_lst['Legajo'])-1),end='')
    print('Promedio entre materias: {}'.format(round(prom(df,int(input())),4)))
  
main()

# ¿Qué es el main()?
# https://www.youtube.com/watch?v=1QXQXvWpyUA

# ¿Qué es el __name__?
# https://www.youtube.com/watch?v=9Os0o3wzS_I

# ¿Qué es el __main__?
# https://www.youtube.com/watch?v=9Os0o3wzS_I

# ¿Qué es el __name__ == "__main__"?
# https://www.youtube.com/watch?v=9Os0o3wzS_I

