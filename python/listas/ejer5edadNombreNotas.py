j=True
nombreLista, nombreLista2, edadLista, notaLista= [], [], [], []
while j==True:
    nombres = input("Ingrese los nombres de los alumnos( * para salir): ")
    ast=nombres.find("*")
    if ast==-1:
        edades = int(input("Ingrese las edades de los alumnos: "))
        notas = float(input("Ingrese las notas de los alumnos: "))
        if edades>20:
            nombreLista.append(nombres)
            edadLista.append(edades)
        if notas>5:
            nombreLista2.append(nombres)
            notaLista.append(notas)
    else:
        j=False

nombreEdadLista = list(zip(nombreLista,edadLista))
nombreNotasLista = list(zip(nombreLista2,notaLista))
print(f"Lista de los nombres de los alumnos mayores de 20 años: {nombreEdadLista} ")
print(f"Lista de los nombres de los alumnos con nota mayor a 5: {nombreNotasLista} ")