articulos = int(input("Ingrese cuantos artículos desea: "))
total=0
for articulo in range(1,articulos+1):
    art = int(input("Ingrese el precio del artículo: "))
    if art>=2000:
        descuento=art*0.15
    elif (art>1000) & (art<2000):
        descuento=art*0.12
    else:
        descuento=art*0.10
    precioFinal=art-descuento
    total+=precioFinal
    print(f"El precio del articulo {articulo} es de {art} y con descuento es de {precioFinal} ")

print(f"Se pagará un total de: ${total} con los descuentos aplicados")