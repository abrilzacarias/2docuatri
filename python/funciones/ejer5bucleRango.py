def nroEntre(pnumMin,pnumMax):
    print(f"Entre {pnumMin} y {pnumMax} están los siguientes números: ")
    for i in range(pnumMin+1, pnumMax):
        print(i)

nroMin=int(input("Ingrese el número minimo: "))
nroMax=int(input("Ingrese el número máximo: "))
nroEntre(nroMin,nroMax)