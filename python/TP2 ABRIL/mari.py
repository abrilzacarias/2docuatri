montoBeca = 0
montoBecaTotal = 0
montoAnual = 0
for alumnos in range(1, 9):
    edad = int(input(f"Ingresar la edad del alumno n°{alumnos}:"))
    promedio = float(input("Indicar promedio: "))
    if edad > 18:
        if promedio >= 9:
            montoBeca = 2000
        elif promedio >= 7.5:
            montoBeca = 1000
        elif (promedio >= 6) and (promedio < 7.5):
            montoBeca = 500
        else:
            print("No cumple con el promedio para obtener la beca. Continue intentandolo :D")
        montoAnual = montoBeca * 12
        montoBecaTotal = montoBecaTotal + montoAnual
    else:
        print("Edad fuera del rango para obtener la beca. ")

print(f"El monto de beca total entre todos los alumnos es ${montoBecaTotal}")