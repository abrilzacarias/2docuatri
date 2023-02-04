listCuentas = [{"alias": "abril"}, {"alias": "mari"}]

def fnCrearAlias():
    alias = input("Ingresar alias: ")

    for unaCuenta in listCuentas:
        while unaCuenta["alias"] == alias:
            print("Alias existente. Intente nuevamente. ")
            alias = input("Ingresar alias: ")
    
    return alias
print(fnCrearAlias())
