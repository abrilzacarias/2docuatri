def calculaIva(pCantSinIva, pIva = 21):
    porcentaje = (pCantSinIva/100)*pIva
    cantConIva= pCantSinIva+porcentaje
    return cantConIva

porcIva=0
cantSinIva=float(input("Ingrese la cantidad de la factura sin IVA: "))
ivaSiNo=int(input("¿Desea ingresar el porcentaje del IVA? \n1)SI 2)NO: "))
if (ivaSiNo==1):
    porcIva=float(input("Ingrese el porcentaje de IVA a aplicar: "))
    print(calculaIva(cantSinIva,porcIva))
else:
    print(calculaIva(cantSinIva,))
