import json
import random
from datetime import datetime
from datetime import timedelta

def fnLeerArchivoCuentas():
    global listaCuentas
    listaCuentas = []
    try:
        with open("cuentasgrupo.json") as archivoJson:
            listaCuentas = json.load(archivoJson)
    except:
        print("Error al abrir el archivo")   
        
def guardarArchivoCuentas():
    with open("cuentasgrupo.json", "w") as archivoJson:
        json.dump(listaCuentas, archivoJson)
        
def fnLeerArchivoMovimientos():
    global movimientosPersonas
    movimientosPersonas = []
    try:
        with open("movimientos.json") as archivoJson:
            movimientosPersonas = json.load(archivoJson)
    except:
        print("Error al abrir el archivo")   
        
def guardarArchivoMovimientoss():
    with open("movimientos.json", "w") as archivoJson:
        json.dump(movimientosPersonas, archivoJson)
        
def fnCrearCVU():
    cvu = random.randint(0000000000, 9999999999)
    validar = True
    while validar:
        for unaCuenta in listaCuentas:
            if unaCuenta["cvu"] != cvu:
                print(f"CVU: {cvu}")
                validar = False
                break
            else:
                print("")
    return cvu

def fnCuit():
    validar = True
    while validar == True:
        cuit = input("Ingrese su CUIT: ")
        cantNums = len(cuit)
        if cantNums == 11:
            validar = False
        else:
            print("Por favor, ingrese el cuit correctamente. ")
    return cuit

def fnCrearAlias():
    alias = input("Ingresar alias: ")
    for unaCuenta in listaCuentas:
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
    listaCuentas.append({"alias" : alias , "contrasena" : contrasena , "cuit": cuit, "cvu": cvu, "Caja Ahorro Pesos": cajaPesos, "Caja Ahorro Dolar" : cajaDolar})
    
    crearMovimiento= {"alias": alias, "movimientos": []}
    movimientosPersonas.append(crearMovimiento)

    return listaCuentas        
        
fechaActual = datetime.now()

def fnExtraerFecha():
    fechaConvertida = fechaActual.strftime('%d/%m/%Y')
    return fechaConvertida

#ABRIL
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
    monedaOpcion = int(input("Ingrese: 1) Dolar 2) Pesos: "))
    if monedaOpcion==1:
        moneda = "U$D"
    elif monedaOpcion==2:
        moneda = "AR$"
    else:
        print("Seleccione una opcion correcta")

    monto, fecha = 200, fnExtraerFecha()
    movimientoNuevo = {"fecha": fecha,
                        "monto": moneda+str(monto),
                        "emisor_Receptor": personaATransferir}
    #función que agregue el movimiento del emisor al JSON
    fnMovimientoEmisor(aliasIngresado, movimientoNuevo)
    #funcion que agregue el movimiento al remitente, si es que existe en la base de datos
    fnMovimientoReceptor(personaATransferir, fecha, monto, aliasIngresado)
    #with open("funcionMov.json", "w") as jsonfile:
        #json.dump(movimientosPersonas, jsonfile)

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

def compraDolares():
    import requests #REVISAR

    URL = "https://api-dolar-argentina.herokuapp.com/api/dolaroficial"

    data = requests.get(URL)
    data = data.json()

    precio_compra = float(data["compra"])
    
    global listaRetornaCompra
    listaRetornaCompra = []

    print(f"Monto disponible: ${}") #mostrar monto disponible en pesos
    operacion = False
    while operacion == False:
        monto = float(
            input("Ingrese el monto en pesos por el que desea comprar dólares: "))
        if monto <=  # disponible:
            compra = monto / precio_compra
            disponible = disponible - monto  # actualizar en el jason
            #disponibleDolar = disponibleDolar + compra
            listaRetornaCompra = [monto, compra] #redondeo acá?
            return listaRetornaCompra
        else:
            print("Monto ingresado no disponible.")
            operacion = False


def ventaDolares():
    import requests #REVISAR

    URL = "https://api-dolar-argentina.herokuapp.com/api/dolaroficial"

    data = requests.get(URL)
    data = data.json()

    precio_venta = float(data["venta"])
    
    global listaRetornaVenta
    listaRetornaVenta = []
    
    print(f"Monto disponible: ${}") #mostrar monto disponible en dolares
    operacion = False
    while operacion == False:
        monto = float(input("Ingrese el monto de dólares que desea vender: "))
        if monto <=  # disponible:
            venta = precio_venta * monto
            disponible = disponible + venta
            #disponibleDolar = disponibleDolar - monto
            listaRetornaVenta = [monto, venta]
            return listaRetornaVenta
        else:
            print("Monto ingresado no disponible.")
            operacion = False

def fnExtraerFechaConPlazo(pDiaIngresado):
    finalPlazo = fechaActual + timedelta(days=pDiaIngresado)
    fechaPlazo = finalPlazo.strftime('%d/%m/%Y')  
    return fechaPlazo

def comprobantePlazo(plistaPlazo):
    print("+----------------------+-----------------------+")
    print("|{:<22}|".format("CAPITAL") + "{:>23}|".format(listaPlazo[0]))
    print("-----------------------+------------------------")
    print("|{:<22}|".format("PLAZO") + "{:>23}|".format(str(listaPlazo[1]) + " días"))
    print("-----------------------+------------------------")
    print("|{:<22}|".format("VENCIMIENTO") + "{:>23}|".format(listaPlazo[2]))
    print("-----------------------+------------------------")
    print("|{:<22}|".format("ACCIÓN AL VENCIMIENTO") + "{:>23}|".format(listaPlazo[3]))
    print("+----------------------+------------------------")
    print("|{:<22}|".format("MONTO A COBRAR") + "{:>23}|".format(listaPlazo[4]))
    print("+----------------------+-----------------------+")

def plazoFijoPesos():
    
    global listaPlazo
    listaPlazo = []
    
    validacion = False
    while validacion == False:
        plazo = input(" 1). 30 días \n 2). 60 días \n 3). 90 días \n Ingrese la opción correcta de días por el desea realizar el plazo: ")
        if plazo == "1":
            plazoIngresado = 30
            tasa = 0.0625
            validacion = True
        elif plazo == "2":
            plazoIngresado = 60
            tasa = 0.125
            validacion = True
        elif plazo == "3":
            plazoIngresado = 90
            tasa = 0.1875
            validacion = True
        else:
            print("Plazo ingresado incorrecto. Intente nuevamente.")
            validacion = False
    fechaFinal = fnExtraerFechaConPlazo(plazoIngresado)
           
    comprobacion = False   
    while comprobacion == False:
        acreditacion = input("1). Renovación Automática \n2). Acreditación En Cuenta \n Ingrese la opción correcta de la acción que desea al vencimiento: ")
        if acreditacion == "1":
            accionVencimiento = "Renovación Automática"
            comprobacion = True
        if acreditacion == "2":
            accionVencimiento = "Acreditación En Cuenta"
            comprobacion = True
        else:
            comprobacion = False
                  
    print(f"Monto disponible: ${}") #mostrar monto disponible en pesos
    operacion = False
    while operacion == False:
        monto = float(input("Ingrese el capital que desea invertir en este plazo fijo: "))
        if monto <=  #disponible:
            cobro = monto + (monto * tasa)
            disponible = disponible - monto  # actualizar en el jason
            listaPlazo = [monto, plazoIngresado, fechaFinal, accionVencimiento, cobro]
            comprobantePlazo(listaPlazo)
            operacion = True     
        else:
            print("Capital ingresado no disponible. Intente nuevamente.")
            operacion = False
                
def plazoFijoDolares():
    
    global listaPlazo
    listaPlazo = []
    
    validacion = False
    while validacion == False:
        plazo = input(" 1). 30 días \n 2). 60 días \n 3). 90 días \n Ingrese la opción correcta de días por el desea realizar el plazo: ")
        if plazo == "1":
            plazoIngresado = 30
            tasa = 0.00043333333
            validacion = True
        elif plazo == "2":
            plazoIngresado = 60
            tasa = 0.00030833333
            validacion = True
        elif plazo == "3":
            plazoIngresado = 90
            tasa = 0.00018333333
            validacion = True
        else:
            print("Plazo ingresado incorrecto. Intente nuevamente.")
            validacion = False

    fechaFinal = fnExtraerFechaConPlazo(plazoIngresado)
            
    comprobacion = False   
    while comprobacion == False:
        acreditacion = input("1). Renovación automática \n 2). Acreditación en cuenta \n Ingrese la opción correcta de la acción que desea al vencimiento: ")
        if acreditacion == "1":
            accionVencimiento = "Renovación Automática."
            comprobacion = True
        if acreditacion == "2":
            accionVencimiento = "Acreditación En Cuenta."
            comprobacion = True
        else:
            comprobacion = False
            
    print(f"Monto disponible: ${}") #mostrar monto disponible en dólares
    operacion = False
    while operacion == False:
        monto = float(input("Ingrese el capital que desea invertir en este plazo fijo: "))
        if monto <=  # disponible:
            cobro = monto * tasa
            disponibleDolares = disponibleDolares - monto  # actualizar en el jason
            listaPlazo = [monto, plazoIngresado, fechaFinal, accionVencimiento, cobro]
            comprobantePlazo(listaPlazo)       
        else:
            print("Capital ingresado no disponible. Intente nuevamente.")
            operacion = False