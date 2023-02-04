meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
diaMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mesIngresado = int(input("Ingrese un mes(1 al 12): "))
if (mesIngresado<1) or (mesIngresado>12):
    print("Mes ingresado incorrecto")
else:
    print(f"El mes es: {meses[mesIngresado-1]} y tiene {diaMes[mesIngresado-1]} días. ")