from funciones import *
from menus import *
listaCuentas = fnLeerArchivoCuentas() # ver
fnLeerArchivoMovimientos()

validarContra = True
salirPrincipal = True
salirLogin = True
while salirLogin:
    menuLogin()
    respuesta = int(input("SELECCIONE UNA OPCIÓN: "))
    if (respuesta == 1):
        validoIngreso = True 
        while validoIngreso:
            cuitIngresado = input("C.U.I.T: ")
            contrasenaIngresada = input("CONTRASEÑA: ")
            validoIngreso = fnIngresar(cuitIngresado,contrasenaIngresada, validoIngreso)
            print ("--------------------------------------------------")
        while salirPrincipal:
            menuPrincipal()
            opcion = int(input("¿QUÉ OPERACIÓN DESEA REALIZAR?: "))
            if (opcion == 1):
                fnMostrarMovimientos(cuitIngresado)
            elif (opcion == 2):
                monedaOpcion = int(input("Ingrese la moneda para hacer su transacción: 1) Dólar 2) Pesos: "))  #global
                fnMonedaOpcionSaldo(monedaOpcion, cuitIngresado)
                montoATransferir =  float(input("Ingrese el monto a transferir: ")) #monto total tiene que ser mayor a  monto transferir tine eu
                personaATransferir = input("Ingrese el alias al que desea transferir: ") #transacciones
                fnTransaccionesEnvia(monedaOpcion, montoATransferir, cuitIngresado)
                # aca va la fn transacciones recibe
                fnTransaccionesRecibe(monedaOpcion, personaATransferir, montoATransferir)
                fnMovimientos(cuitIngresado, montoATransferir, personaATransferir, monedaOpcion)
                guardarArchivoCuentas()
                guardarArchivoMovimientoss()
            elif (opcion == 3): #terminado
                print ("--------------------------------------------------")
                menuPlazoTipos()
                operacion = int(input("¿QUÉ OPERACIÓN DESEA REALIZAR?: "))
                if (operacion == 1):
                    print ("--------------------------------------------------")
                    menuPlazos()
                    plazo = input("INGRESE LA OPCIÓN CORRECTA DE DÍAS POR LOS QUE DESEA REALIZAR EL PLAZO: ")
                    print ("--------------------------------------------------")
                    menuAcreditacion()
                    acreditacion = input("INGRESE LA OPCIÓN CORRECTA DE LA ACCIÓN QUE DESEA AL VENCIMIENTO: ") 
                    plazoFijoPesos(cuitIngresado, plazo, acreditacion)
                if (operacion == 2):
                    print ("--------------------------------------------------")
                    menuPlazos()
                    plazo = input("INGRESE LA OPCIÓN CORRECTA DE DÍAS POR LOS QUE DESEA REALIZAR EL PLAZO: ")
                    print ("--------------------------------------------------")
                    menuAcreditacion()
                    acreditacion = input("INGRESE LA OPCIÓN CORRECTA DE LA ACCIÓN QUE DESEA AL VENCIMIENTO: ")
                    plazoFijoDolar(cuitIngresado, plazo, acreditaciones)
            elif (opcion == 4): #terminado
                print ("--------------------------------------------------")
                CompraVenta()
                seleccion = int(input("¿QUÉ ACCIÓN DESEA REALIZAR?: "))
                if (seleccion == 1):
                    listaRetornaCompra = compraDolares(cuitIngresado)
                    print(f"Compra realizada correctamente. El monto por el que se compró dólares es ${listaRetornaCompra[0]}, la cantidad de dólares comprados fue ${listaRetornaCompra[1]}")
                elif (seleccion == 2):
                    listaRetornaVenta = ventaDolares(cuitIngresado)
                    print(f"Venta realizada correctamente. El monto de dólares vendido es ${listaRetornaVenta[0]}, la ganancia en pesos es de ${listaRetornaVenta[1]}.")
                else:
                    print ("opcion seleccionada no corresponde.")
            elif opcion == 5:
                cambioClave(contrasenaIngresada)
            elif opcion == 6:
                salirPrincipal = False
                #menuLogin()
            else:
                print("LA OPERACIÓN NO EXISTE. VUELVA A INTENTARLO")
    elif (respuesta == 2):
        fnCrearCuenta()
    else:
        print("LA OPERACIÓN NO EXISTE. VUELVA A INTENTARLO")
        