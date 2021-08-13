def genCod(nombre):
    #Separamos el nombre por espacios
    nombreSep = nombre.split()

    #obtenemos el primer nombre y primer apellido
    prNombre = nombreSep[0]
    prApellido = nombreSep[2]

    #generamos el código con las primeras letras y lo devolvemos
    codigo = prNombre[0] + prApellido[0] + "2021"
    return codigo

nombre = input("Ingrese el nombre completo del estudiante: ")

print(f"Su código es: {genCod(nombre)}")