cont = 0
validacioncant = False
validacionesp = False 
validacionnum = False
validacionvocal = False

unaPalabra = input("Ingrese una contraseña: ")

for unaLetra in unaPalabra: 
    cont = cont + 1

    if (cont > 7):
        validacioncant = True
    if (unaLetra == "A") or (unaLetra == "E") or (unaLetra == "I") or (unaLetra == "O") or (unaLetra == "U"):
        validacionvocal = True
    if (unaLetra == "0") or (unaLetra == "1") or (unaLetra == "2") or (unaLetra == "3") or (unaLetra == "4") or (unaLetra == "5"):
        validacionnum = True
    if (unaLetra == "#") or (unaLetra == "@"):
        validacionesp = True
        
if (validacioncant == True) and (validacionvocal == True) and (validacionnum == True) and (validacionesp == True):
    print("¡Su contraseña es válida!")
else: 
    print("Su contraseña es incorrecta. Intente nuevamente.")