def validarDni(pDni):
    c, valido, i = 0, False, 0
    for i in pDni:
        c+=1
    if (c==7) or (c==8):
        valido=True
        return valido
    else:
        print("DNI incorrecto, inténtelo de nuevo.")
        return valido

def id(pNombre, pDni):
    cNom=0
    for letra in pNombre:
        cNom+=1
    #funcion xq no se como hacer sino
    primerosTres=pDni[:3]
    id=f"{pNombre}{cNom}{primerosTres} "
    return id

valido, dni = False, "1"
while (dni!="99"):
    valido=False
    nombre=input("Ingrese su nombre: ")
    while (valido==False):
        dni=input("Ingrese su DNI (99 para finalizar): ")
        if dni=="99":
            print("Ha finalizado el programa")
            break
        else:
            valido=validarDni(dni)

    if valido==True:
        print(f"Su identificador de socio es: {id(nombre, dni)} \n")
