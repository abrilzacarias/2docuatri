import json
from datetime import datetime


movimientosPersonas = []
with open("funcionMov.json") as jsonfile:
    movimientosPersonas = json.load(jsonfile)

def fnMovimientoEmisor(pAliasIngresado, pMovNuevo):
    for persona in movimientosPersonas:
        if persona["alias"] == pAliasIngresado:
            persona["movimientos"].insert(0, pMovNuevo)
            #break

def fnMovimientoReceptor(pPersonaATransferir, pfecha, pMonto, pAliasIngresado):
    for persona in movimientosPersonas:
        if persona["alias"] == pPersonaATransferir:
            movimientoNuevo = [{"fecha": pfecha,
            "monto": pMonto,
            "emisor_Receptor": pAliasIngresado}]
            persona["movimientos"].insert(0, movimientoNuevo)
        else:
            pass

def fnMovimientos():
    aliasIngresado = input("Ingrese su alias: ")
    #monto: input("Ingrese el monto que desea transferir: ") transacciones
    personaATransferir = input("Ingrese el alias al que desea transferir: ") #transacciones
    monedaOpcion = int(input("Ingrese: 1) Dolar 2) Peso: "))
    if monedaOpcion==1:
        moneda = "U$D"
    elif monedaOpcion==2:
        moneda = "AR$"
    else:
        print("Seleccione una opcion correcta")

    monto, fecha = 200, str(datetime.now())
    movimientoNuevo = {"fecha": fecha,
                        "monto": moneda+str(monto),
                        "emisor_Receptor": personaATransferir}
    #función que agregue el movimiento del emisor al JSON
    fnMovimientoEmisor(aliasIngresado, movimientoNuevo)
    #funcion que agregue el movimiento al remitente, si es que existe en la base de datos
    fnMovimientoReceptor(personaATransferir, fecha, monto, aliasIngresado)
    with open("funcionMov.json", "w") as jsonfile:
        json.dump(movimientosPersonas, jsonfile)

fnMovimientos()
for persona in movimientosPersonas:
    print("")
    for k,v in persona.items():
        print(f"{k}: {v} ")
    