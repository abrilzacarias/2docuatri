alumnos, beca, montoMensualC, becaTotal = 8, 0, 0, 0

for alumno in range(1, alumnos+1):
    edad=int(input(f"Ingrese la edad del {alumno} alumno: "))
    promedio=float(input(f"Ingrese el promedio del {alumno} alumno: "))
    if (edad>18):
        if (promedio>=9):
            beca=2000
        elif (promedio>=7.5):
            beca=1000
        elif (promedio<7.5) & (promedio>=6):
            beca=500
        else:
            print("No cumple con el promedio")
    else:
        print("Edad fuera de rango")
    montoAnual = beca * 12
    becaTotal+=montoAnual

print(f"El costo anual de becas por 1 año: {becaTotal} ")

#72000