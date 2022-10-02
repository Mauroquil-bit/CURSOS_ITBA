# Opcional: Mini-desafío json

"""
Opcional: Mini-desafío json
Estás encargado de un servidor con millones de usuarios.

Se pide escribir un programa que reciba el email y contraseña del usuario y se fije si existe el usuario y si coincide la contraseña.

Se tienen datos encolumnados en formato json que nos llegan del siguiente formato:

{
    "usuarios": ["mica@mail.co", "jerry@gma.com","alber@soup.co"],
    "contra": ["abc123","caballitos","yoloswag"]
}
La entrada del programa son tres lineas, el programa entonces va tener tres input(). La primer linea contiene el json, la segunda el email a verificar, y la tercera la contraseña. Por ende, las primeras lineas de su programa podrían ser:

import json
usuarios = json.loads(input())
email = input()
password = input()
La salida del programa será OK si el usuario se encuentra en la base de datos y si coincide la contraseña, imprimimos DNE (does not exist) si el usuario no existe y NO en cualquier otro caso.

Caso ejemplo
Entrada:

{"usuarios": ["mica@mail.co","jerry@gma.com","alber@soup.co"],"contra": ["abc123","caballitos","yoloswag"]}
mica@mail.co
caballitos
El usuario existe y la contraseña también... pero no le corresponde la contraseña caballitos al usuario mica@mail.co (la contraseña de mica@mail.co sería abc123) por ende imprimimos:

Salida

NO
Considere que no hay usuarios repetidos.
"""

import json
usuarios = json.loads(input())
email = input("Mail:")
password = input("Contraseña")

if email in usuarios["usuarios"]:
  index = usuarios["usuarios"].index(email)
  if password == usuarios["contra"][index]:
    print("OK")
  else:
    print("NO")

else:
  print("DNE")


