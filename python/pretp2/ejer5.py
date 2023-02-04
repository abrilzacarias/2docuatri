clientes = int(input("Ingresar la cantidad de clientes: "))
multa = 2000
saldoActualFinal = 0
ganancia = 0
while clientes > 0:
    saldoAnterior = float(input("Ingresar saldo anterior: "))
    pagoDepositado = float(input("Ingrese el pago depositado anteriormente: "))
    compras_realizadas = float(input('Ingresa el valor de compras realizadas: '))
    saldoActualInicial = float(input("Ingresar saldo actual: "))

    if saldoAnterior == pagoDepositado:
        print("No presenta cargos por demora. ")
        saldoActualFinal = saldoActualInicial
    else:
        diferencia = saldoAnterior - pagoDepositado
        intereses = (diferencia/100)*112
        saldoActualFinal = saldoActualInicial + intereses + multa
        ganancia = ganancia + intereses + multa
        
    clientes = clientes - 1
    pagoMinimo = saldoActualFinal*0.15
    pagoParaNoGenerarIntereses = saldoActualFinal*0.85
    print(f"El saldo actual del cliente es un monto de ${saldoActualFinal}")
    print(f"Su pago minimo : ${pagoMinimo}")
    print(f"Pago para no generar intereses: ${pagoParaNoGenerarIntereses}")

print(f"***La ganancia obtenida por clientes morosos es ${ganancia}")
    