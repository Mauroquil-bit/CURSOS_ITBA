# El tiempo es dinero

#leemos los usuarios en el formato index, para tenerlos indexados por el nombre de usuario
#Es decir, para que la clave sea el nombre de los usuarios y sea facil referenciar
#a los usuarios
usuarios_archivo = pd.read_excel("Finanzas.xlsx", "Usuarios",index_col="Usuario") 

#Mostramos los usuarios recien leidos
print("Usuarios:")
print(usuarios_archivo)
print(" ")

usuarios = usuarios_archivo.to_dict("index")


#Leemos las transferencias en el formato records, es decir conseguimos una lista con las transferencias
transferencias_archivo = pd.read_excel("Finanzas.xlsx", "Transferencias")
transferencias = transferencias_archivo.to_dict("records")

#Mostramos las transferencias recien realizadas
print("Transferencias:")
print(transferencias_archivo)
print(" ")

for transferencia in transferencias: # iteramos todas las transferncias distintas
    # obtenemos la info de la transferencia
    emisor = transferencia["Emisor"]
    receptor = transferencia["Receptor"]
    monto = transferencia["Monto"]

    usuarios[emisor]["Presupuesto"] -= monto # le retiramos el dinero al emisor
    usuarios[receptor]["Presupuesto"] += monto #le ortorgamos el dinero al receptor

# generamos el nuevo archivo excel, orient="index" provoca que las claves se coloquen en la primera fila,
# En este caso los usuarios son las claves y queremos que la primerea fila del archivo
# tenga todos los nombres de usuario
usuarios_actualizados = pd.DataFrame.from_dict(usuarios, orient="index")

#Mostramos los saldos de los usuarios luego de realizar las transferencias
print("Usuarios luego de realizar las transferencias:")
print(usuarios_actualizados)

#Grabamos la información final
usuarios_actualizados.to_excel("usuarios_actualizados.xlsx")


###############################################################################

