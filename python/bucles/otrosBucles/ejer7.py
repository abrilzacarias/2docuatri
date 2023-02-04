#continue, se saltea el código siguiente y ejecuta de nuevo desde el comienzo
nrosPositivos, cont1, cont2, nro = 1, 0, 0, 0
while nrosPositivos!=0:
    nrosPositivos = int(input("Escriba la cantidad de números positivos a escribir: "))
    if nrosPositivos<0:
        print("La cantidad debe ser mayor que 0. Inténtelo de nuevo ")
        nrosPositivos=1
    else:
        while (nrosPositivos!=cont2):
            nro=int(input("Escriba un número: "))
            cont1+=1
            if nro>=0:
                cont2+=1
        break

print(f"Ha escrito {cont1} números, {cont2} de ellos positivos.")


