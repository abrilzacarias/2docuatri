import json

servidoresLista = []
with open("servidores.json") as jsonfile:
    servidoresLista = json.load(jsonfile)
    
def fnEstadoServidorId(pId):
    for servidor in servidoresLista:
        for v in servidor.values():
            if v == pId:
                print(f'Estado del servidor con ID {pId}: {servidor["Estado"]}')

def fnServidoresEstado(pEstado):
    for servidor in servidoresLista:
        for v in servidor.values():
            if v == pEstado:
                print(f'Servidores con estado {servidor["Estado"]}: {servidor["Servidor"]} ')

def fnCantidadDeServidores():
    cantidadServidores = len(servidoresLista)
    return f"La cantidad de servidores es de {cantidadServidores}"

def fnMaximoIds():
    maxServidores = len(servidoresLista)+1
    return maxServidores

def fnNuevoServidor():
    ip = input("Ingrese la IP del servidor: ")
    estado = input("Ingrese el estado del servidor (Activo/Inactivo): ").capitalize()
    servidorNuevo = {"Id": int(fnMaximoIds()),
    "Servidor": "Servidor"+str(fnMaximoIds()),
    "IP": ip,
    "Estado": estado}
    servidoresLista.append(servidorNuevo)
    print("Se añadió correctamente.")

def menu():
    print("""
    1- Consultar el estado de un servidor
    2- Consultar los servidores según su estado
    3- Consultar cuantos servidores existen
    4- Consultar máximo de IDs
    5- Agregar una nueva entrada a la base de datos
    6- Salir""")

j = True
while j == True:
    menu()
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        idIngresada = int(input("Ingrese una ID: "))
        fnEstadoServidorId(idIngresada)
    elif opcion == 2:
        estadoIngresado = input("Ingrese un estado (Activo/Inactivo): ").capitalize()
        fnServidoresEstado(estadoIngresado)
    elif opcion == 3:
        print(fnCantidadDeServidores())
    elif opcion == 4:
        print(fnMaximoIds())
    elif opcion == 5:
        fnNuevoServidor()
        with open("servidores.json", "w") as jsonfile:
            json.dump(servidoresLista, jsonfile)
    elif opcion == 6:
        print("Ha salido del programa.")
        j=False
    else:
        print("Seleccione una opcion correcta")