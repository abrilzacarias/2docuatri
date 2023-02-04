lista = []
c=0
while c<10:
    nro = int(input("Ingrese un número entre 1 y 100: "))
    if (nro>=1) and (nro<100):
        nroCuadrado=nro**2
        nroCubo=nro**3
        lista.append(nro)
        c+=1
        lista.append(nroCuadrado)
        lista.append(nroCubo)
    else:
        print("Nro incorrecto, intente de nuevo")

print(f"Lista: {lista} ")