
nro1=int(input("Ingrese el primer número: "))
nro2=int(input("Ingrese el segundo número: "))
i=1
for i in range(nro1, nro2):
    if ((i%2)==0):
        print(f'{i} PAR ')
    else:
        print(f'{i} IMPAR ')
    i=nro1+1
