import json
import random
listCuentas= [{"alias": "ysyalejo", "contrasena": "Noviembre11#", "cuit": "11111111111", "cvu": 3356117711, "Caja Ahorro Pesos": 570, "Caja Ahorro Dolar": 460}]

"""with open("cuentasgrupo.json") as jsonfile:
    listCuentas = json.load(jsonfile)"""

movimientosPersonas = []
with open("funcionMov.json") as jsonfile:
    movimientosPersonas = json.load(jsonfile)
    
def fnCrearCVU():
    cvu = random.randint(0000000000, 9999999999)
    j = True
    while j:
        for unaCuenta in listCuentas:
            if unaCuenta["cvu"] != cvu:
                print(f"CVU: {cvu}")
                j = False
                break
            else:
                print("")
    return cvu

def fnCuit():
    j = True
    while j == True:
        cuit = input("Ingrese su CUIT: ")
        cantNums = len(cuit)
        if cantNums == 11:
            j = False
        else:
            print("Por favor, ingrese el cuit correctamente. ")
    return cuit

def fnCrearAlias():
    alias = input("Ingresar alias: ")

    for unaCuenta in listCuentas:
        while unaCuenta["alias"] == alias:
            print("Alias existente. Intente nuevamente. ")
            alias = input("Ingresar alias: ")
    return alias

def fnCrearPass():
    caracterEspecial =['$', '@', '#', '%'] 
    valido = True
    msgError = ""
    validacion = True
    while validacion:
        passwd = input("Contraseña: ")
        if len(passwd) > 8: 
            valido = True
        else:
            msgError = 'Debe ser mayor a 8.'
        if len(passwd) < 20: 
            valido = True
        else: 
            msgError = 'Debe ser menor a 20.'
        if any(caracteres.isdigit() for caracteres in passwd): 
            valido = True
        else:
            msgError = msgError + 'Añadir un numero.'
        if not any(caracteres.isupper() for caracteres in passwd): 
            valido = False
            msgError = msgError + 'Añadir letra en mayuscula.'
        else:
            valido = True
        if not any(caracteres.islower() for caracteres in passwd): 
            msgError = msgError + 'Añadir letra en minuscula.'
            valido = False
        else:
            valido = True
        if not any(caracteres in caracterEspecial for caracteres in passwd): 
            valido = False
            msgError = msgError + 'Añadir un caracter especial $@#.'
        else:
            valido = True
        if valido == True: 
            validacion = False
            print("Contraseña añadida correctamente. ")
            break
        else:
            print (f"No es correcto. {msgError}")
    return passwd


def fnAcreditacionPesos():
    saldoAcreditado = random.randint(400,800)
    print(f"Saldo acreditado en pesos: AR${saldoAcreditado}")
    return saldoAcreditado

def fnAcreditacionDolar():
    saldoAcreditado = random.randint(400,800)
    print(f"Saldo acreditado en dolares: U$D {saldoAcreditado}")
    return saldoAcreditado

def fnCrearCuenta():
    print("Bienvenido. Siga los siguientes pasos para registrarse correctamente. ")
    alias = fnCrearAlias()
    contrasena = fnCrearPass()
    cuit = fnCuit()
    cvu = fnCrearCVU()
    cajaPesos = fnAcreditacionPesos()
    cajaDolar = fnAcreditacionDolar()
    listCuentas.append({"alias" : alias , "contrasena" : contrasena , "cuit": cuit, "cvu": cvu, "Caja Ahorro Pesos": cajaPesos, "Caja Ahorro Dolar" : cajaDolar})
    
    crearMovimiento= {"alias": alias, "movimientos": []}
    movimientosPersonas.append(crearMovimiento)
    return listCuentas

fnCrearCuenta()
with open("funcionMov.json", "w") as jsonfile:
    json.dump(movimientosPersonas, jsonfile)
"""with open("cuentasgrupo.json", "w") as jsonfile:
    json.dump(listCuentas, jsonfile)"""