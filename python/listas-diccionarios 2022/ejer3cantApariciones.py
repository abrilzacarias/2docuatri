""" Escriba una función que reciba como parámetro una lista de números, que puede contener valores
repetidos, y devuelva un diccionario en el que cada clave sea el un número que aparece en la lista y el valor
sea la cantidad de apariciones."""

listaNros = [1, 3, 4, 8, 8, 4, 7, 3, 0, 3, 7, 5]

def fListaNros(pLista):
    dicc = {}
    c=0
    for i in listaNros:
        #.count devuelve la cantidad de veces q se repite un elemento especificado
        dicc[i] = listaNros.count(i)
    return dicc

print(fListaNros(listaNros))