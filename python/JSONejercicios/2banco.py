import json
import random
listCuentas = []
with open("cuentas.json") as jsonfile:
    listCuentas = json.load(jsonfile)

def menu():
    print("1. Listado de todas las cuentas: \n"
        "2. Ingresar numero de cuenta. \n"
        "3. Consultar salgo negativo. \n"
        "4.Retornar cantidad de cuentas \n"
        "5. Salir")

def fnNumCuenta(num):
    for unaCuenta in listCuentas:
        for v in unaCuenta.values():
            if v == num:
                return unaCuenta

def fnConsultaSaldo(num):
    for unaCuenta in listCuentas:
        if num in unaCuenta.values():
            for v in unaCuenta.values():
                if v == "S":
                    return"Presenta  saldo: POSITIVO"
                if v == "N": 
                    return "Presenta  saldo: NEGATIVO"

def fnCantCuentas(condicion):
    contCuentas= 0
    for unaCuenta in listCuentas:
        for v in unaCuenta.values():
            if v == condicion:
                contCuentas+=1
        return contCuentas

def fnNuevaCuenta():
    num = random.randint(1,999)
    print(f"Su numero de cuenta es: {num}")
    cuit = int(input("Ingrese su cuit: "))
    saldo = float(input("Saldo que desea ingresar: "))
    condicion = input("Ingrese su condicion (S/N): ").capitalize()
    print("Añadido exitosamente. ")
    return listCuentas.append({"numero": num, "cuit": cuit, "saldo": saldo, "saldoN" : condicion})

salir = True
while salir: 
    print("1. Cliente 2. Nuevo cliente 3. Salir")
    pregunta = int(input("Bienvenido. Ingrese una opción. "))
    if pregunta == 1:
        num = int(input("Numero de cuenta: "))
        """cuit = int(input("CUIT: "))
        saldo = float(input("Saldo: "))"""
        #¿para que me pide todo esoooooooOOOOOOOO?
        for unaCuenta in listCuentas:
            for v in unaCuenta.values():
                if v == num:
                    salirCliente = True
                    while salirCliente:
                        menu()
                        opcion = int(input("¿Qué desea realizar? "))
                        if opcion == 1: 
                            print(listCuentas)
                        if opcion == 2:
                            print(fnNumCuenta(num))
                        if opcion == 3:
                            print(fnConsultaSaldo(num))
                        if opcion == 4: 
                            condicion = input("¿S/N?").capitalize()
                            print(f"Cantidad de cuentas con condicion {condicion}: {fnCantCuentas(condicion)}")
                        if opcion == 5:
                            print("Ha salido de su cuenta. ")
                            salirCliente = False
                        else:
                            print("Opcion incorrecta. Vuelva a ingresar. ")
    if pregunta == 2:
        fnNuevaCuenta()
        with open("cuentas.json", "w") as jsonfile:
                json.dump(listCuentas, jsonfile)
    if pregunta == 3: 
        print("Ha salido del programa. ")
        salir = False
