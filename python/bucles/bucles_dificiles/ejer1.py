palabra = input("Ingrese una palabra: ")
palabra = palabra.lower()
contA, contE, contI, contO, contU= 0, 0, 0, 0, 0
for i in palabra:
    if i in "a":
        contA=contA+1
    elif i in "e":
        contE=contE+1
    elif i in "i":
        contI=contI+1
    elif i in "o":
        contO=contO+1
    elif i in "u":
        contU=contU+1

print(f'''Cantidad de A: {contA}
Cantidad de E: {contE}
Cantidad de I: {contI}
Cantidad de O: {contO}
Cantidad de U: {contU}''')