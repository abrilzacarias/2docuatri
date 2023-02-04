nro1 = int(input("Ingrese un número: "))
nroMayor=0

while nro1>=nroMayor:
    nroMayor=nro1
    nro1 = int(input(f"Ingrese un número mayor que {nro1}: "))
    

print(f"{nro1} no es mayor que {nroMayor}. ")