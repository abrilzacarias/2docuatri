hamburguesas=int(input("Ingrese el total de hamburguesas que desea: "))
hamburS, hamburD, hamburT = 0, 0, 0
c=0
while (c<hamburguesas):
    tipoHambur = int(input("Ingrese el tipo de hamburguesa que desea. \n1) SIMPLE 2) DOBLE 3) TRIPLE: "))
    if tipoHambur==1:
        hamburS=int(input("Ingrese cuantas hamburguesas simples desea comprar: "))
        c+=hamburS
    elif tipoHambur==2:
        hamburD=int(input("Ingrese cuantas hamburguesas dobles desea comprar: "))
        c+=hamburD
    elif tipoHambur==3:
        hamburT=int(input("Ingrese cuantas hamburguesas triples desea comprar: "))
        c+=hamburT
    else:
        print("Debe seleccionar una opción correcta.")
        continue
    if (c<hamburguesas):
        hamburFaltantes=hamburguesas-c
        print(f"Faltan comprar {hamburFaltantes} hamburguesas.")
    elif (c>hamburguesas):
        print(f"Se ha superado la cantidad ingresada. Ingrese una cantidad menor.")
        c = 0
    else:
        hamburSTotal=1000*hamburS
        hamburDTotal=1500*hamburD
        hamburTTotal=1800*hamburT
        compra = hamburSTotal+hamburDTotal+hamburTTotal

        pago=int(input("¿Pagará con tarjeta de crédito? 1) SI 2) NO: "))

        if (pago==1):
            compraDesc=(compra)*0.05
            print(f"Debe pagar un total de ${compra+compraDesc} ")
        else:
            print(f"Debe pagar un total de ${compra} ")