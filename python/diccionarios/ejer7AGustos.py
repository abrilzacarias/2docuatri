dictPersonas = {"brenda": ["1", "2"], "paula": ["3", "4"], "marianela": ["5", "6"], "abril": ["7", "8"]}

def agregueGusto(pPersona, pGusto):
    if pPersona not in dictPersonas.keys():
        dictPersonas[pPersona] = pGusto
    else:
        if (pGusto not in dictPersonas[pPersona]):
            #Para usar funciones integradas, se escribe directamente .funcion (.append)
            #con dictPersonas[pPersona] se accede AL VALOR, no a la llave
            dictPersonas[pPersona].append(pGusto)
        else:
            print("No tiene ningún efecto.")
        return(dictPersonas)

persona=input("Ingrese el nombre: ")
gusto=input("Ingrese su gusto: ")
agregueGusto(persona,gusto)
print(dictPersonas)