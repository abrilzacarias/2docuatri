import json

def fnLeerArchivo():
    global listaCuentas
    listaCuentas = []
    try:
        with open("cuentasgrupo.json") as archivoJson:
            listaCuentas = json.load(archivoJson)
    except:
        print("Error al abrir el archivo")

def fnExtraerSaldoPesos(pAlias):
    saldoPesos = 0
    for unaCuenta in listaCuentas:
        if unaCuenta['alias'] == pAlias:
            saldoPesos = unaCuenta['Caja Ahorro Pesos']
    return saldoPesos

fnLeerArchivo()
print(fnExtraerSaldoPesos("ysyalejo"))