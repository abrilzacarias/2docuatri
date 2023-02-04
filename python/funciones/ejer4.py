import random

def nroRandom(pnumMin,pnumMax):
    nro = 0
    nro = random.randint(pnumMin,pnumMax)
    print(nro)

nroMin=int(input("Ingrese el número minimo: "))
nroMax=int(input("Ingrese el número máximo: "))
nroRandom(nroMin,nroMax)

