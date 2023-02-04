""""Ejercicio 1: Una función que reciba un diccionario y que genere una lista con 
todos los valores de las claves."""

dicc = {"brenda": "frutilla", "abril": "chocolate", "marianela": "menta granizada"}

def x(dicc):
    listaValores = []
    for v in dicc.values():
        listaValores.append(v)
    return listaValores

print(x(dicc))