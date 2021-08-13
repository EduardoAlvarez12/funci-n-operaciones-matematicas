def areaRectangulo(b,h):
    area = b * h
    return area

print("Calculadora de área de un rectángulo")
b = float(input("Ingrese la base del rectángulo en cm: "))
h = float(input("Ingrese la altura del rectángulo en cm: "))

print("El área del rectángulo es: ", areaRectangulo(b,h), "cm^2" )