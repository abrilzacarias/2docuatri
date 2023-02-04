nros=int(input("Ingrese cuantos numeros se introducirán: "))

primernro=int(input("Ingrese el primer número: "))

for nro in range(nros):
    numero = int(input("Ingrese un número: "))
    if (numero<primernro):
        print(f'{numero} es menor a {primernro} ')