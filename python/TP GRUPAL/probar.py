dictCuentas = {700: ["cuit", 7, "S"]}

def opcionMenu():
    print(""""
    1. Consulta de saldo por numero de cuenta
    2. Depositar dinero por número de cuenta.
    3. Retirar dinero por número de cuenta.
    4. Salir de la cuenta. 
    """)
def listadosMenu():
    print(""""
    1. Listado de todas las cuentas.
    2. Listados de cuetas por CUIT
    3. Listado de cuentas con saldo negativo.
    4. Listado de cuentas que pueden tener saldo negativo. 
    5. Listado de cuentas que no pueden tener saldo negativo.
    """)
def listados(pOpcion):
    listaTodasCuentas = []
    listaCuentasCuit = []
    listaCuentasSaldoNegativo = []
    for claves,valores in dictCuentas.items():
            listaCuentasCuit.append(valores[0])
            listaTodasCuentas.append(claves)
            listaCuentasSaldoNegativo.append(valores[1])
    #print(listaTodasCuentas)
    #print(listaCuentasCuit)

salir = True

while (salir == True):
    ingresarOpcion = int(input("Ingresar como 1. Cliente  2. Banco: "))
    if ingresarOpcion == 1: 
        numeroCuenta = int(input("Ingrese el número para ingresar/crear una cuenta (ingrese 0 para salir del sistema): "))
        if numeroCuenta in dictCuentas.keys():
            opcionMenu()
            respuesta = int(input("¿Que desea realizar?: "))
            if (respuesta == 1):
                print(dictCuentas[numeroCuenta][1])
            elif (respuesta == 2):
                dineroDepositado = float(input("Ingresar la cantidad de dinero a depositar: "))
            elif (respuesta == 3):
                dineroRetirar = float(input("Ingrese la cantidad de dinero a retirar: ")) 
                for claves, valores in dictCuentas.items()

            elif (respuesta == 4):
                print("")
            else:
                print("Opcion incorrecta. Por favor vuelva a intentar. ")
                #veremos despues
        elif (numeroCuenta == 0):
            salir = False
        else:
            print(f"Su número de cuenta es {numeroCuenta} ")
            cuit = int(input("Ingrese su CUIT: "))
            saldo = float(input("Ingrese su saldo: "))
            dictCuentas[numeroCuenta] = [cuit,saldo]
    elif ingresarOpcion == 2:
        listastadosM
        opcionListados = int(input("Indicar lo que desea ver: "))
        listados(opcionListados)

    else:
        print("Ingrese una opción válida.")
print(dictCuentas)







'''
agenda = {}
while salir==True
    opcion = int(input("""
1. Añadir/modificar.
2. Buscar.
3. Borrar.
4. Listar.
5. Salir.
Seleccione la opción: """))
    if (opcion==1) or (opcion==3):
        nombre=input("Ingrese el nombre: ")
    if opcion==1:
        if nombre in agenda:
            print(agenda[nombre])
            opcionModificar = input("Seleccione: n\ 1) Para modificar. 2) NO modificar.")
            if opcionModificar == "1":
                numNuevo = input("Ingrese el nuevo número de teléfono: ")
                agenda[nombre] = numNuevo
        else:
            telef=input("El nombre no se encuentra, ingrese el teléfono: ")
            agenda[nombre] = telef
    elif opcion == 2:
        busqueda = input("Ingrese caracteres para buscar: ")

        for k in agenda.keys():
            #.startswith() para buscar un string que empiece con las letras ingresadas.
            if k.startswith(busqueda):
                #imprimir k directamente para imprimir la clave, y agenda[k] para imprimir su valor
                print(f"Nombre: {k} Número: {agenda[k]}") 
    elif opcion==3:
        opcionBorrar = input("Seleccione: n\ 1) Para borrar. 2) NO borrar.")
        if opcionBorrar == "1":
            agenda.pop(nombre)
            print("Ha borrado este contacto.")
    elif opcion==4:
        print(agenda)
    elif opcion==5:
        salir=False
    else:
        print("Ingrese una opción correcta.")

print("Ha salido del programa.")"""agenda = {}

""""""""""""
while salir==True:
    opcion = int(input("""
1. Añadir/modificar.
2. Buscar.
3. Borrar.
4. Listar.
5. Salir.
Seleccione la opción: """))
    if (opcion==1) or (opcion==3):
        nombre=input("Ingrese el nombre: ")
    if opcion==1:
        if nombre in agenda:
            print(agenda[nombre])
            opcionModificar = input("Seleccione: n\ 1) Para modificar. 2) NO modificar.")
            if opcionModificar == "1":
                numNuevo = input("Ingrese el nuevo número de teléfono: ")
                agenda[nombre] = numNuevo
        else:
            telef=input("El nombre no se encuentra, ingrese el teléfono: ")
            agenda[nombre] = telef
    elif opcion == 2:
        busqueda = input("Ingrese caracteres para buscar: ")

        for k in agenda.keys():
            #.startswith() para buscar un string que empiece con las letras ingresadas.
            if k.startswith(busqueda):
                #imprimir k directamente para imprimir la clave, y agenda[k] para imprimir su valor
                print(f"Nombre: {k} Número: {agenda[k]}") 
    elif opcion==3:
        opcionBorrar = input("Seleccione: n\ 1) Para borrar. 2) NO borrar.")
        if opcionBorrar == "1":
            agenda.pop(nombre)
            print("Ha borrado este contacto.")
    elif opcion==4:
        print(agenda)
    elif opcion==5:
        salir=False
    else:
        print("Ingrese una opción correcta.")

print("Ha salido del programa.")
'''entas)
