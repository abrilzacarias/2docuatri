dictCiudad = {}
ciudad = " "

while ciudad != "*":
    ciudad = input("Ingrese el nombre de la ciudad ('*' para salir): ")
    if ciudad!="*":
        listaHabitantes = []
        cantHabitantes= int(input("¿Cuántos habitantes desea ingresar?: "))
        for hab in range(1,cantHabitantes+1):
            habitante = input("Ingrese el nombre de un habitante: ")
            listaHabitantes.append(habitante)
            dictCiudad[ciudad] = listaHabitantes

print(dictCiudad)