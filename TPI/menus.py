def menuPrincipal():
    print("""
    1. CONSULTA DE MOVIMIENTOS.
    2. TRANSACCIONES.
    3. PLAZO FIJO.
    4. COMPRA Y VENTA DE DOLÁRES.
    5. CAMBIO DE CLAVE.
    6. CERRAR SESIÓN.
    """)

'''    
salir = True
while (salir == True):
    menuPrincipal()
    respuesta = int(input("¿QUÉ OPERACIÓN DESEA REALIZAR?: "))
    if (respuesta == 1):
        print ("consulta movimientos")
    elif (respuesta == 2):
        print ("transacciones")
    elif (respuesta == 3):
        print ("plazo fijo")
    elif (respuesta == 4):
        print ("compra y venta de dolares")
    elif (respuesta == 5):
        print ("cambio de clave")
    elif (respuesta == 6):
        print ("volver al login")
        salir = False
    else:
        print("Opcion incorrecta. Por favor vuelva a intentar. ")
#print("Ha salido del programa.")
'''


def menuLogin():
    print ("----------------------------------------------------")
    print ("|"'\033[1m' + '     BIENVENIDO  AL  BIG  BROTHER  BANK 💱💰🏧 ' + '\033[0m'"|")     
    print("----------------------------------------------------")
    print("""
    1. ACCEDER A CUENTA EXISTENTE.
    2. CREAR UNA NUEVA CUENTA. 
    3. OLVIDÉ MI CLAVE DE ACCESO.
    """)

menuLogin()


