nro1, nro2, i, cont= 1, 0, 0, 0
while nro2<=nro1:
    nro1=int(input("Ingrese el número mínimo: "))
    nro2=int(input("Ingrese el número máximo: "))
    if (nro2<nro1):
        print("El número minimo es mayor al máximo, intente nuevamente.")
    elif (nro2==nro1):
        print("Los números son iguales, intente nuevamente.")
    else:
        while nro2>nro1:
            nroSolicitado=int(input("Ingrese un número dentro del rango: "))
            if (nroSolicitado>=nro1) & (nroSolicitado<=nro2):
                #print(nroSolicitado)
                cont = cont+1
            else:
                print("Ha salido del programa, este número no está en el rango.")
                break

print(f'La cantidad de números en este rango es de {cont} ')