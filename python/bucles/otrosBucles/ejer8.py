nro, suma=1,0
while nro>0:
    nro=int(input("Escriba un número (Ingrese uno negativo para salir): "))
    if nro>0:
        suma+=nro
print(f"La suma de los números positivos introducidos es {suma} ")
