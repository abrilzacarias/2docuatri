nro1 = int(input("Ingrese un número mayor entero: "))
nro2 = int(input(f"Ingrese un número mayor que {nro1}: "))

while nro1>=nro2:
    nroMayor=nro1
    nro2=int(input(f"{nro2} no es mayor que {nroMayor}, intente nuevamente:  "))

print(f"Los números que ha escrito son {nro1} y {nro2}. ")