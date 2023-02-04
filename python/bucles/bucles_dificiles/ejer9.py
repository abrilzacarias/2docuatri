edades = input("Ingrese la edad del huésped (ok para salir): ")
precioAc = 0
personaAc = 0
if (edades != "ok"):
    while (edades != "ok"):
        edades = input(f"Ingrese la edad del huésped (Ingrese 'ok' para salir): ")
        if (edades != "ok"):
            edadesInt = int(edades)
            if (edadesInt <= 2):
                precio = 0.00
            elif (edadesInt >= 3) and (edadesInt <= 12):
                precio = 140.00
            elif (edadesInt >= 65):
                precio = 180.00
            else:
                precio = 230.00
            personaAc += 1
            precioAc = precioAc + precio
    else:
        print(f"El precio final para {personaAc} personas es {precioAc}")
else:
    print("Ha salido del programa.")