clave = int(input("Ingrese la clave del articulo (10, 20, 30, 40, 50 o 60): "))

materiaPrima = float(input("Ingrese el costo de la materia prima: "))

if (clave==30) or (clave==40):
    manoObra = (materiaPrima/100)*75
elif (clave==10) or (clave==50):
    manoObra = (materiaPrima/100)*80
elif (clave==20) or (clave==60):
    manoObra = (materiaPrima/100)*85

if (clave==20) or (clave==50):
    gastosFabricacion=(materiaPrima/100)*30
elif (clave==30) or (clave==60):
    gastosFabricacion=(materiaPrima/100)*35
elif (clave==10) or (clave==40):
    gastosFabricacion=(materiaPrima/100)*28

costoProduccion = materiaPrima+manoObra+gastosFabricacion
costo45 = (costoProduccion/100)*45
precioVenta = costoProduccion+costo45
print(f'El precio de venta es ${precioVenta} ')