def relacion(pa, pb):
    if pa>pb:
        return 1
    elif pa<pb:
        return -1
    else:
        return 0

nro1=int(input("Ingrese el primer número: "))
nro2=int(input("Ingrese el segundo número: "))

print(relacion(nro1,nro2))