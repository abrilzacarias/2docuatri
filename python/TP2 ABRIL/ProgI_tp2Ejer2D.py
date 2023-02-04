totalFinal = 0
cPantalones = 3

for c in range (1, cPantalones+1):
    cantidad = int(input("Ingresa la cantidad: "))
    modelo = int(input("Selecciona un modelo \n1)A 2) B: "))
    talle=int(input("Selecciona una talla: "))
    if (modelo==1):
        tela=4000
        manoObra=3000
    else:
        tela=3900
        manoObra=4500
    precioT=tela+manoObra
    
    if (talle==32) or (talle==36):
        precioT=precioT+(precioT*0.10)
    gananciaEx=precioT+(precioT*0.30)
    totalFinal+=gananciaEx*cantidad
print(f"El recargo extra del 30% de ganancia es $ {totalFinal}")