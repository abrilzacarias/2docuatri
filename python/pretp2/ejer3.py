hamburS=int(input("Ingrese cuantas hamburguesas simples desea comprar: "))
hamburD=int(input("Ingrese cuantas hamburguesas dobles desea comprar: "))
hamburT=int(input("Ingrese cuantas hamburguesas triples desea comprar: "))

hamburSTotal=1000*hamburS
hamburDTotal=1500*hamburD
hamburTTotal=1800*hamburT
compra = hamburSTotal+hamburDTotal+hamburTTotal

pago=int(input("¿Pagará con tarjeta de crédito? 1) SI 2) NO: "))

if (pago==1):
    compraTotal=(compra)*0.05
    print(f"Debe pagar un total de {compra+compraTotal} ")
else:
    print(f"Debe pagar un total de {compra} ")









