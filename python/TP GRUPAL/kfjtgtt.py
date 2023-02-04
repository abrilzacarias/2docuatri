dictCuentas = {"700": ["cuit", "saldo"]}

def opcionMenu():
    print("""""
    1. Ingresar una nueva cuenta.
    2. Consulta de saldo por numero de cuenta
    3. Depositar dinero por número de cuenta.
    4. Retirar dinero por número de cuenta.
    5. Salir.
    """)

respuesta = True

while (respuesta == True):
    opcionMenu()
    respuesta = input("¿Que desea realizar?")
    if (respuesta != 5):
        numeroCuenta = int(input("Ingrese el número de cuenta: "))
        cuit = int(input("Ingrese su CUIT: "))
        saldo = float(input("Ingrese su saldo: "))
    if numeroCuenta in dictCuentas.keys():
        if (respuesta == 1):
            
            dictCuentas[numeroCuenta] = [cuit, saldo]