def contar_vocales(pPalabra):
    cont = 0
    for v in pPalabra: 
        if v.lower() in "aeiou":
            #convierto todas las letras en minus con lower
            cont+=1
    return cont

palabra = input("Ingrese una palabra o texto: ")
cant = contar_vocales(palabra)
print(f"Cantidad de vocales: {cant}" )
