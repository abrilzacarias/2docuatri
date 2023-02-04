listaCuentas = [{"alias": "ysyalejo", "contrasena": "Noviembre11#", "cuit": "11111111111", "cvu": 3356117711, "Caja Ahorro Pesos": 570, "Caja Ahorro Dolar": 460},
{"alias": "abril", "contrasena": "Noviembre11#", "cuit": "11111111111", "cvu": 3356117711, "Caja Ahorro Pesos": 570, "Caja Ahorro Dolar": 460}]
def fnExtraerSaldoPesos(pAlias):
    saldoPesos = 0
    for unaCuenta in listaCuentas:
        if unaCuenta['alias'] == pAlias:
            saldoPesos = unaCuenta['Caja Ahorro Pesos']
    return saldoPesos

def fnExtraerSaldoDolar(pAlias):
    saldoDolar = 0
    for unaCuenta in listaCuentas:
        if unaCuenta['alias'] == pAlias:
            saldoDolar = unaCuenta['Caja Ahorro Dolar']
    return saldoDolar

def fnTransaccionesEnvia():    #envia dinero a otra persona
    aliasPrueba="ysyalejo"
    global monedaOpcion, personaATransferir, montoATransferir
    monedaOpcion = int(input("Ingrese la moneda para hacer su transacción: 1) Dólar 2) Pesos: "))  #global
    if monedaOpcion == 1:
        saldoActual = (fnExtraerSaldoDolar(aliasPrueba))
        print (saldoActual)
    elif monedaOpcion == 2:
        saldoActual = fnExtraerSaldoPesos(aliasPrueba)
        print (saldoActual)
    else: 
        print ("La opción ingresada no es correcta")
    montoATransferir =  float(input("Ingrese el monto a transferir: ")) #monto total tiene que ser mayor a  monto transferir tine eu
    personaATransferir = input("Ingrese el alias al que desea transferir: ") #transacciones
    if monedaOpcion==1:
        saldoActual = fnExtraerSaldoDolar(aliasPrueba)
        saldoTotal = saldoActual - montoATransferir
        for unaCuenta in listaCuentas:
            if unaCuenta['alias'] == aliasPrueba:
                unaCuenta['Caja Ahorro Dolar'] = saldoTotal
        print(f"Ha depositado ${montoATransferir} y su saldo actual es ${saldoTotal}.")
    elif monedaOpcion==2:
        saldoActual = fnExtraerSaldoPesos(aliasPrueba)
        saldoTotal = saldoActual - montoATransferir
        for unaCuenta in listaCuentas:
            if unaCuenta['alias'] == aliasPrueba:
                unaCuenta['Caja Ahorro Pesos'] = saldoTotal
        print(f"Ha depositado ${montoATransferir} y su saldo actual es ${saldoTotal}.")
    else:
        print("Seleccione una opcion correcta")

def fnTransaccionesRecibe(pMonedaOpcion, pPersonaATransferir, pMontoATransferir):    #recibe dinero de otra persona
    aliasPruebaRecibe=pPersonaATransferir
    if pMonedaOpcion == 1:
        saldoActual = (fnExtraerSaldoDolar(aliasPruebaRecibe))
        print (saldoActual)
        
    elif pMonedaOpcion == 2:
        saldoActual = fnExtraerSaldoPesos(aliasPruebaRecibe)
        print(saldoActual)
    else: 
        print ("La opción ingresada no es correcta")
    #montoATransferir =  float(input("Ingrese el monto a transferir: ")) #monto total tiene que ser mayor a  monto transferir tine eu
    #personaATransferir = input("Ingrese el alias al que desea transferir: ") #transacciones  #global
    if pMonedaOpcion==1:
        saldoActual = fnExtraerSaldoDolar(aliasPruebaRecibe)
        saldoTotal = saldoActual + pMontoATransferir
        for unaCuenta in listaCuentas:
            if unaCuenta['alias'] == aliasPruebaRecibe:
                unaCuenta['Caja Ahorro Dolar'] = saldoTotal
        print(f"Ha recibido ${pMontoATransferir} y su saldo actual es ${saldoTotal}.")
    elif pMonedaOpcion==2:
        saldoActual = fnExtraerSaldoPesos(aliasPruebaRecibe)
        saldoTotal = saldoActual + pMontoATransferir
        for unaCuenta in listaCuentas:
            if unaCuenta['alias'] == aliasPruebaRecibe:
                unaCuenta['Caja Ahorro Pesos'] = saldoTotal
        print(f"Ha recibido ${pMontoATransferir} y su saldo actual es ${saldoTotal}.")
    else:
        print("Seleccione una opcion correcta")

fnTransaccionesEnvia()
fnTransaccionesRecibe(monedaOpcion, personaATransferir, montoATransferir)