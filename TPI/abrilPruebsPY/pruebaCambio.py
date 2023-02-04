def cambioClave(pContrasenaIngresada):
    for cuenta in listaCuentas:
        if cuenta['contrasena'] == pContrasenaIngresada:
            contrasenaNueva = input("Ingrese la contraseña nueva: ")
            cuenta['contrasena'] == contrasenaNueva
            print("Contraseña modificada exitosamente. ")

