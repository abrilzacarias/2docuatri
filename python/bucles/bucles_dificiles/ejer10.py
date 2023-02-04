ABCCONST= "ABDEFGHIJKÑMNOPQRDTUVWXYZ"

msj = input("Ingrese su mensaje para cifrar: ")

clave = 3
cifrado = ""

for letra in msj.upper():
    if letra in ABCCONST:
        indice = ABCCONST.find(letra)
        indice += clave
        if indice >= 27:
            indice -= 27
        cifrado += ABCCONST[indice]
    else:
        cifrado += letra
print(cifrado)