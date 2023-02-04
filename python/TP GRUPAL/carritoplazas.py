#Lista de los juegos
steam_juegos = {1: ["Left 4 Dead 2", 129.99 ],
2: ["Rust", 2440.99 ],
3: ["Resident Evil 3", 2499.00],
4: ["FIFA 22 ", 5499.00],
5: ["Red Dead Redemption 2 ", 2499.00],
6: ["Grand Theft Auto IV: The Complete Edition", 1299.00],
7: ["Call of Duty®: Black Ops III - Zombies Chronicles Edition ", 999.00],
8: ["NBA 2K22 ", 5999.00],
9: ["Phasmophobia ", 169.99],
10: ["Prince of Persia", 499.00],
11: ["Escribir el nombre de un juego que no está en la lista", 0],
}

print("Lista de juegos con impuesto IVA incluido:")
#Ciclo para mostrar los juegos con sus precios en pantalla

for k,v in steam_juegos.items():
    print(f"{k} | {v[0]} {v[1]} ")

#En el caso de que se seleccione la opción para agregar y calcular el precio de un juego que no está en la lista
def siEs11():
    try:
            nombre_juego_ingresado = input("Ingrese el nombre del juego: ")
            precio_juego_ingresado = int(input("Ingrese el precio del juego (números): "))
            #Reemplazar/sobreescribir los elementos ingresados en los del array 
            steam_juegos[opcion][0] = nombre_juego_ingresado
            steam_juegos[opcion][1] = precio_juego_ingresado
            print(f'El nombre del juego es de {steam_juegos[opcion][0]} y el precio del juego es {steam_juegos[opcion][1]}')
    #Si el usuario ingresa un caracter no numérico, se vuelve a ejecutar la función
    except ValueError:
            print("El dato ingresado no es válido")
            siEs11()

#Función que aplica los impuestos a los precios
def impuestos():
    #Impuesto PAIS = 35%
    impuestoPais = 30
    valor_original = steam_juegos[opcion][1]
    aumento = valor_original * (impuestoPais / 100)
    valor_con_pais = valor_original + aumento
    #Impuesto a las ganancias = 35%
    impuestoGanancias = 35
    valor_original = steam_juegos[opcion][1]
    aumento = valor_original * (impuestoGanancias / 100)
    valor_con_ganancias = valor_original + aumento
    #Precio final con ambos impuestos
    precionfinal_2impuestos = impuestoPais + impuestoGanancias
    valor_original = steam_juegos[opcion][1]
    aumento = valor_original * (precionfinal_2impuestos / 100)
    valorfinal_juego = valor_original + aumento
    #Muestra en pantalla de los valores
    print(f"El valor del juego con el impuesto PAIS aplicado es: {valor_con_pais}")
    print(f"El valor del juego con el Impuesto a las ganancias aplicado es: {valor_con_ganancias}")
    print(f"El valor del juego con el impuesto PAIS y el impuesto a las ganancias aplicados es: {valorfinal_juego}")

while True:
    try:
        #Numero de opción seleccionado
        opcion = int(input("Ingrese el número del juego del que desea saber el precio + impuestos: "))
        #Si la opción seleccionada es mayor a 1 Y(operador and) menor a 10, se ejecuta en el array con la misma variable
        if (opcion >= 1 and opcion <= 10):
            print(f'El nombre del juego es de {steam_juegos[opcion][0]} y el precio del juego es {steam_juegos[opcion][1]}')
            #Invocar función de impuestos
            impuestos()
            break
        #Si es 11, se ejecuta un input para que se ingresen los datos que se necesitan ;)
        elif (opcion == 11):
            siEs11()
            impuestos()
            break
        #Si se ingresa un número mayor a 11 o menor a 0, se ejecuta el else 
        else: 
            print("Número fuera de rango")
            #Invocar función de impuestos
            impuestos()
            continue
    except ValueError:
        print("El dato ingresado no es válido")
        continue