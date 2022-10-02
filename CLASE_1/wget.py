# Si no estamos en un entorno linux podemos definir nuestra propia wget
# Esta función nos ayuda a descargar archivos desde la web y no es necesaria para archivos locales
# No es necesario entender cómo funciona, se las mostramos sólo por si alguno llega a necesitarla

# Importamos la libreria requests
import requests

def wget(url):
    r = requests.get(url, allow_redirects=True)
    with open(url[url.rfind('/') + 1::], 'wb') as f:
        f.write(r.content)

wget("https://raw.githubusercontent.com/IEEESBITBA/Curso-Python/master/Curso_Analisis_de_Datos_Datos/Datos.xlsx")

####################################################

