c=0
validacionCantidad=False
validacionEspecial=False 
validacionNum=False
validacionVocal=False
j=False

while j==False:
    palabra = input("Ingrese una contraseña: ")
    for unaLetra in palabra: 
        c+=1 
        if (c>=8):
            validacionCantidad=True
        if (unaLetra=="A") or (unaLetra=="E") or (unaLetra=="I") or (unaLetra=="O") or (unaLetra=="U"):
            validacionVocal=True
        if (unaLetra=="0") or (unaLetra=="1") or (unaLetra=="2") or (unaLetra=="3") or (unaLetra=="4") or (unaLetra=="5"):
            validacionNum=True
        if (unaLetra=="#") or (unaLetra=="@"):
            validacionEspecial= True
    
    #.isdigit es una función y retorna verdadero si se ingresa un int
    #if (validacionCantidad) & (validacionVocal) & (validacionNum) & (validacionEspecial): ABREVIADO
    if (validacionCantidad==True) & (validacionVocal==True) & (validacionNum==True) & (validacionEspecial==True):
        print("¡Su contraseña es válida!")
        j=True
    else: 
        print("Contraseña incorrecta ¡Intente nuevamente!")