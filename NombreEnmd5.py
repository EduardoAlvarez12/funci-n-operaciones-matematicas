from hashlib import md5

nombre = (input("Ingrese su nombre: "))
codificado = md5(nombre.encode("utf-8")).hexdigest()
print(codificado)
