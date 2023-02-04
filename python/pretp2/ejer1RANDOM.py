import random

cont = 0
nrorandom= random.randint(1,20)

nombre = input("Ingrese un nombre: ")
nroIngresado = int(input("Adivine el número entre el 1 y el 20: "))

while (nroIngresado!=nrorandom):
    if nroIngresado<nrorandom:
        nroIngresado = int(input(f"{nombre}, tu estimación es muy baja. Intente de nuevo: "))
    else:
        nroIngresado = int(input(f"{nombre}, tu estimación es muy alta. Intente de nuevo: "))
    cont+=1

print(f"¡Buen trabajo, {nombre}! Has adivinado mi número en {cont+1} intentos. El número era {nrorandom} ")