def validarDni(pDni):
    c, i= 0, 0
    for i in pDni:
        c+=1
    if (c==7) or (c==8):
        valido=True
    else:
        valido=False
    return valido

dni=input("Ingrese su DNI: ")
print(validarDni(dni))