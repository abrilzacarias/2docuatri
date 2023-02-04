
ladoA = float(input("Ingrese el lado A del lote: "))
ladoB = float(input("Ingrese el lado B del lote: "))
ladoC = float(input("Ingrese el lado C del lote: "))

triangulo_area = ladoB*(ladoA-ladoC)/2
rectangulo_area = ladoB*(ladoA-ladoC)

area_final = rectangulo_area+triangulo_area

print(f"El valor del área calculada es de: {area_final}") 

if (area_final<=10000):
    print("El lote es un lote rural pequeño")
elif ((area_final>10000) & (area_final<=20000)):
    print("El lote es un lote rural medio")
else:
    print("El lote es un lote rural grande")



