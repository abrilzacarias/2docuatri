doc = int(input("Ingrese la cantidad de kilos de uva: "))
precioInicial = int(input("Ingrese el precio inicial del kilo de uva: "))
kiloUvas=doc*precioInicial

tipo = input("Ingrese el tipo de uva (A o B): ")
tamano = int(input("Ingrese el tamaño de uva (1 o 2): "))

if (tipo=="A") or (tipo=="a"):
    if tamano==1:
        precioFinal=kiloUvas+20
    else:
        precioFinal=kiloUvas+30
else:
    if tamano==1:
        precioFinal=kiloUvas-30
    else:
        precioFinal=kiloUvas-50

ganancia=precioFinal-precioInicial*doc
print(f"El precio final de la docena de bananas es: {precioFinal} ")
print(f"La ganancia de la docena de bananas es: {ganancia} ")



