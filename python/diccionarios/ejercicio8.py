agenda = {}
j = True

while j==True:
    opcion = int(input("""
1. Añadir/modificar.
2. Buscar.
3. Borrar.
4. Listar.
5. Salir.
Seleccione la opción: """))
    if (opcion==1) or (opcion==3):
        nombre=input("Ingrese el nombre: ")
    if opcion==1:
        if nombre in agenda:
            print(agenda[nombre])
            opcionModificar = input("Seleccione: n\ 1) Para modificar. 2) NO modificar.")
            if opcionModificar == "1":
                numNuevo = input("Ingrese el nuevo número de teléfono: ")
                agenda[nombre] = numNuevo
        else:
            telef=input("El nombre no se encuentra, ingrese el teléfono: ")
            agenda[nombre] = telef
    elif opcion == 2:
        busqueda = input("Ingrese caracteres para buscar: ")

        for k in agenda.keys():
            #.startswith() para buscar un string que empiece con las letras ingresadas.
            if k.startswith(busqueda):
                #imprimir k directamente para imprimir la clave, y agenda[k] para imprimir su valor
                print(f"Nombre: {k} Número: {agenda[k]}") 
    elif opcion==3:
        opcionBorrar = input("Seleccione: n\ 1) Para borrar. 2) NO borrar.")
        if opcionBorrar == "1":
            agenda.pop(nombre)
            print("Ha borrado este contacto.")
    elif opcion==4:
        print(agenda)
    elif opcion==5:
        j=False
    else:
        print("Ingrese una opción correcta.")

print("Ha salido del programa.")
