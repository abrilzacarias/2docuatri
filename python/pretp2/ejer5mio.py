bankucp=True
multa, c, ganancia = 2000, 0, 0
while bankucp==True:
    saldoAnterior=float(input("Ingrese su saldo anterior: "))
    #montoCompras=float(input("Ingrese el monto de compras que realizó: ")) dato innecesario
    pagoDepositado=float(input("Ingrese el pago que depositó en el corte anterior: "))
    saldoActual=float(input("Ingrese su saldo actual: "))

    if (saldoAnterior==pagoDepositado):
        print("No posee multa por demora en el pago.")
    else:
        saldonoPagadoAnterior = saldoAnterior-pagoDepositado
        intereses = saldonoPagadoAnterior*0.12
        saldoActual = saldoActual+intereses+multa
        ganancia+=intereses+multa
    
    pagoMinimo=saldoActual*0.15
    pagoNoIntereses=saldoActual*0.85
    print(f"El saldo actual del cliente es de ${saldoActual} ")
    print(f"El pago mínimo del cliente es de ${pagoMinimo} ")
    print(f"El pago  para no generar intereses del cliente es de ${pagoNoIntereses} ")
    c+=1
    
    cliente=int(input("¿Desea añadir un cliente más? \n1) SI 2) NO: "))
    if cliente==1:
        print("")
    else:
        bankucp=False

print(f"La ganancia obtenida por clientes morosos es ${ganancia}")
