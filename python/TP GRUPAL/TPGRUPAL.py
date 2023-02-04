dictCuentas = {700: [27568526931, 7000, "S"]}

def opcionMenu():
    print("""
    1. Consulta de saldo por numero de cuenta
    2. Depositar dinero por número de cuenta.
    3. Retirar dinero por número de cuenta.
    4. Salir de la cuenta. 
    """)

def listadosMenu():
    print(""""
    1. Listado de todas las cuentas.
    2. Listados de cuentas por CUIT
    3. Listado de cuentas con saldo negativo.
    4. Listado de cuentas que pueden tener saldo negativo. 
    5. Listado de cuentas que no pueden tener saldo negativo.
    """)
    
def listados(pOpcion):
    listaCuentasCuit, listaCuentasSaldoNegativo, listaCuentasS, listaCuentasN = [], [], [], []
    for claves,valores in dictCuentas.items():
        listaCuentasCuit.append(claves)
        listaCuentasCuit.append(valores[0])
        
        if valores[1]<0:
            listaCuentasSaldoNegativo.append(claves)
            listaCuentasSaldoNegativo.append(valores[1])
        if valores[2]=="S":
            listaCuentasS.append(claves)
        elif valores[2]=="N":
            listaCuentasN.append(claves)
    
    if pOpcion == 1:
        return dictCuentas
    elif pOpcion == 2:
        return listaCuentasCuit
    elif pOpcion == 3:
        return listaCuentasSaldoNegativo
    elif pOpcion == 4:
        return listaCuentasS
    elif pOpcion == 5:
        return listaCuentasN

def consultaSaldo(pnumeroCuenta, pdictCuentas):
    saldoP = (pdictCuentas[pnumeroCuenta][1])
    return saldoP
    
def depositoDinero(pdineroDepositado, pdicCuentas):
    for claves, valores in pdicCuentas.items():
        saldoActual = valores [1]
        saldoTotal = saldoActual + pdineroDepositado
        valores [1] = saldoTotal
    return print (f"Ha depositado ${pdineroDepositado} y su saldo actual es ${saldoTotal}.")    

def retiroDinero(pdineroRetirado, pdicCuentas):
    for claves, valores in pdicCuentas.items():
        saldoTotal = valores [1]
        negativoSaldo = valores[2]
    if (negativoSaldo == "S"):
        saldoRestante = saldoTotal - pdineroRetirado
        valores[1] = saldoRestante
        print (f"Ha retirado ${pdineroRetirado} y su saldo actual es ${saldoRestante}.")
    else:
        print("Lo lamento, no puede retirar el dinero.")

salir = True
correctoSaldo = False

while (salir == True):
    ingresarOpcion = int(input("Ingresar como 1. Cliente  2. Banco: "))
    if ingresarOpcion == 1: 
        numeroCuenta = int(input("Ingrese el número para ingresar/crear una cuenta (ingrese 0 para salir del sistema): "))
        if numeroCuenta in dictCuentas.keys():
            opcionMenu()
            respuesta = int(input("¿Que desea realizar?: "))
            if (respuesta == 1):
                resultado = consultaSaldo(numeroCuenta, dictCuentas)
                print (resultado)
            elif (respuesta == 2):
                dineroDepositado = float(input("Ingresar la cantidad de dinero a depositar: "))
                depositoDinero(dineroDepositado, dictCuentas)          
            elif (respuesta == 3):
                dineroRetirar = float(input("Ingrese la cantidad de dinero a retirar: ")) 
                retiroDinero(dineroRetirar, dictCuentas)  
            elif (respuesta == 4):
                print("")
            else:
                print("Opcion incorrecta. Por favor vuelva a intentar. ")
        elif (numeroCuenta == 0):
            salir = False
        else:
            print(f"Su número de cuenta es: {numeroCuenta} ")
            cuit = int(input("Ingrese su CUIT: "))
            saldo = float(input("Ingrese su saldo: "))
            correctoSaldo = False   
            while (correctoSaldo == False):       
                saldoNegativo = input("¿El cliente puede retirar dinero aunque tenga saldo insuficiente? Ingrese 'S' (si es posible) o 'N':  (no es posible): ").upper()
                if (saldoNegativo == "S") or (saldoNegativo == "N"):
                    dictCuentas[numeroCuenta] = [cuit,saldo,saldoNegativo]
                    correctoSaldo = True
                else: 
                    correctoSaldo = False
    elif ingresarOpcion == 2:
        listadosMenu()
        opcionListados = int(input("Indicar lo que desea ver: "))
        print(listados(opcionListados))
    else:
        print("Ingrese una opción válida.")
print("Ha salido del programa.")