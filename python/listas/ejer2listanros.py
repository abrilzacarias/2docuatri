nro=0
lista = []
while nro>=0:
    nro=int(input("Ingrese un número (negativo para salir): "))
    if nro>=0:
        print(f"Se añadió {nro} a la lista")
        lista.append(nro)
    else:
        print("Ha salido del programa")

print(lista)