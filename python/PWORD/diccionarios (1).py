# un contructor que me genera un diccionario
persona = dict()

# SI USO LLAVES ES UN DICCIONARIO
persona = {"nombre": "Juan", "edad": 20, "sexo" : "M"}
print(persona["nombre"])
print(persona["edad"])
print(persona["sexo"])
#ACCEDO AL VALOR POR LA CLAVE

persona["edad"] = 40 #esto es para modificar
print(persona["edad"])

# si la clase no existe, puedo ir agregando
persona["direccion"] = "una direccion"
#otro ejemplo
jugadores = {1: "Arquero", 2: "Defensor"}
print(jugadores[1]) #me devuelve el arquero

#FOR PARA RECORRER EL DICCIONARIO
for clave, valor in persona.items():
    print(f"Clave {clave} valor {valor}")
    
#   PARA BORRAR UNA CLAVE VALOR 
del persona["nombre"]
print(persona)

unDiccionario = {"clave" : "juan", "clave2" : "pedro"}
#PARA ACCEDER
print(unDiccionario["clave"])

#Por ejemplo el del banco
listaCuentas = list()
cuenta1 = {"numero" : 1, "extacciones":[151,5000,6600] , "cuit":235423 , "saldo": 1000, "extNegativa" : "S"}
cuenta2 = {"numero" :2 , "cuit":235423 , "saldo": 1000, "extNegativa" : "S"}
cuenta3 = {"numero" :3 , "cuit":235423 , "saldo": 1000, "extNegativa" : "S"}
listaCuentas.append(cuenta1)
listaCuentas.append(cuenta2)
listaCuentas.append(cuenta3)

for unaCuenta in listaCuentas:
    #si tengo que mostrar el listado de cuentas
    print(unaCuenta["extracciones"])
    
#para mostrar claves
unDiccF = {"arquero" : "rossi" , "defensor" : "rojo"}
for k in unDiccF.keys():
    print(k)
#Para recorrer valores    
for v in unDiccF.values():
    print(v)
#Para recorrer clave y valor    
for k, v in unDiccF.items():
    print(f"clave {k} valor {v}")

# ---------- DICCIONARIOS --------------------------------------------------------------------
#para operar con los valores que están dentro de una lista, dentro de un diccionario
for claves, valores in pdicCuentas.items(): #recorre el diccionario
    saldoTotal = valores [1] #se asigna el valor necesitado a una variable
    negativoSaldo = valores[2] #se asigna el valor necesitado a una variable
    if (negativoSaldo == "S"): #comparacion
        saldoRestante = saldoTotal - pdineroRetirado #operacion
        valores[1] = saldoRestante #de ésta manera se sobreescribe el valor en la posicion
        print (f"Ha retirado ${pdineroRetirado} y su saldo actual es ${saldoRestante}.")

numeroCuenta = int(input("Ingrese el número para ingresar/crear una cuenta (ingrese 0 para salir del sistema): "))
if numeroCuenta in dictCuentas.keys(): #buscar el dato ingresado en las llaves 
    
# -----------------------------------------------------------------------------------------------
