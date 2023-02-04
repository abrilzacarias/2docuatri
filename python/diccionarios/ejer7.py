'''Suponga un diccionario que contiene como llave el nombre de una persona y como valor una lista con todas sus
“gustos”. Desarrolle una función def agregueGusto(persona, gusto) tal que: Si la persona no existe la agregue al
diccionario con una lista que contiene un solo elemento. Si la persona existe y el gusto existe en su lista, no tiene ningún
efecto. Si la persona existe y el gusto no existe en su lista, agrega el gusto a la lista.'''

dictPersonas = {"brenda": ["1", "2"], "paula": ["3", "4"], "marianela": ["5", "6"], "abril": ["7", "8"]}
persona=input("Ingrese el nombre: ")
gusto=input("Ingrese su gusto: ")
dictPersonasCopia = dictPersonas.copy()
def agregueGusto(persona, gusto):
    for k,v in dictPersonasCopia.items():
        if persona not in dictPersonas.keys():
            dictPersonas.setdefault(persona, gusto)
            #dictPersonas.append(persona)
            #dictPersonas[persona] = [gusto]
        else:
            if gusto not in dictPersonas.values():
                #if persona in dictPersonas.keys():
                dictPersonas[persona] = v.append(gusto)

agregueGusto(persona,gusto)
print(dictPersonas)
#for k,v in dictPersonas.items():
    #agregueGusto(k, v)
    
   # dictionary = {'A': 1, 'B': 2, 'C': 3}
    #key, value = 'D', 4
 
    #dictionary.setdefault(key, value)
    #print(dictionary)        # {'A': 1, 'B': 2, 'C': 3, 'D': 4}