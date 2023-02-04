movimientosPersonas = [{"alias": "abril", "movimientos": []}, 

{"alias": "mari", "movimientos": []}]

def fnMovimientoEmisor(pAliasIngresado, pMovNuevo):
    for persona in movimientosPersonas:
        if persona["alias"] == pAliasIngresado:
            persona["movimientos"].insert(0, pMovNuevo)
            #break
        if persona["alias"] != pAliasIngresado:
            personaNueva= {"alias": pAliasIngresado,
            "movimientos": pMovNuevo}
            movimientosPersonas.append(personaNueva)

aliasIngresado = input("Ingrese su alias: ")
#monto: input("Ingrese el monto que desea transferir: ") transacciones
personaATransferir = input("Ingrese el alias al que desea transferir: ") #transacciones
movimientoNuevo = [{"fecha": "11-11",
            "monto": 2000,
            "emisor_Receptor": personaATransferir}]
fnMovimientoEmisor(aliasIngresado, movimientoNuevo)

for persona in movimientosPersonas:
    for k,v in persona.items():
        print(f"{k}: {v} ")
    print("")