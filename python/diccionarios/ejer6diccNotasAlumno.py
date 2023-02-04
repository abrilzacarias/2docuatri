clase={}

listaNombres=[]
cantidadAlumnos = int(input("Introduce la cantidad de alumnos: "))

for i in range(1,cantidadAlumnos+1):
    nombre = input("Ingrese el nombre del alumno: ")
    listaNombres.append(nombre)
    listaNotas=[]
    #listaNotas dentro del bucle asi se borra en cada iteración
    notascant = int(input("Indicar la cantidad de notas que desea ingresar: "))
    for i in range (1, notascant + 1):
        nota = float(input(f"Ingrese la nota {i}: "))
        listaNotas.append(nota)

    clase[nombre] = listaNotas.copy()
    # En cada iteracion va copiando la lista de notas en la nueva key(nombre). 
    print(clase)
    #.copy copia la lista literalmente

for alumno, notas in clase.items():
    print(f"{alumno} ha sacado de nota media de: {(sum(notas)/len(notas))}")
