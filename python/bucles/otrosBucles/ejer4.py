nro = 0
suma = 0

for i in range(5):
    nro = int(input(f"Ingrese el número {i+1}: "))
    suma +=  nro

if (suma<=50):
    print(f'El resultado de la suma de los números es de: {suma} y da menos de 50')
else:
    print(f'El resultado de la suma de los números es de: {suma} y da más de 50')
