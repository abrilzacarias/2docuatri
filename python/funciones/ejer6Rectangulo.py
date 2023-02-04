def area_rectangulo(pBase,pAltura):
    area = pBase*pAltura
    return f"El área del rectángulo es de: {area} "

base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
print(area_rectangulo(base, altura))