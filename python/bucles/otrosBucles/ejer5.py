nros=0
while nros!=1:
    nros=int(input("Ingrese cuantos numeros se introducirán: "))
    if nros<=0:
        print(f"Intente nuevamente, {nros} no es válido. ")
    else:
        primernro=int(input("Ingrese el primer número: "))
        for nro in range(nros):
            numero = int(input(f"Ingrese un número mayor a {primernro}: "))
            if (numero<primernro):
                print(f'{numero} es menor a {primernro} ')
        break

print("El programa ha finalizado.")