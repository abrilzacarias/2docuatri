def validarEmail(pDireccion):
    letra=0
    valido=False
    for letra in pDireccion:
        if (letra=="@"):
            valido=True
    return valido

direccion=input("Ingrese su dirección de email: ")
valido = validarEmail(direccion)
if (valido==True):
    print(f"La direccion {direccion} es VÁLIDA.") 
else:
    print(f"La direccion {direccion} es inválida.")
