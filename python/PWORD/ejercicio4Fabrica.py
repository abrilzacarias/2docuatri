salir = True

costoProduccion = 0.0
manoObra = 0.0
gastoFabricacion = 0.0
acPrecioVenta = 0.0
while (salir == True):
    costoMateriaPrima = int(input("Ingrese el costo de la materia prima(0 para salir): "))
    if (costoMateriaPrima == 0):
        salir = False
    else:
        claveProduc = int(input("Selecciona una clave de artículo(1, 2, 3, 4, 5 o 6): "))
        if (claveProduc == 3) or (claveProduc == 4):
            manoObra = costoMateriaPrima * 0.75
        elif (claveProduc == 1) or (claveProduc == 5):
            manoObra = costoMateriaPrima * 0.80
        elif (claveProduc == 2) or (claveProduc == 6):
            manoObra = costoMateriaPrima * 0.85
        else:
            print("Clave incorrecta")
        
        if (claveProduc == 2) or (claveProduc == 5):
            gastoFabricacion = costoMateriaPrima * 0.30
        elif (claveProduc == 3) or (claveProduc == 6):
            gastoFabricacion = costoMateriaPrima * 0.35  
        elif (claveProduc == 1) or (claveProduc == 4):
            gastoFabricacion = costoMateriaPrima * 0.28 
        costoTotal = costoMateriaPrima+manoObra+gastoFabricacion
        precioVenta = costoTotal + (costoTotal*0.45)
        print(f"El precio de venta del articulo es: ${precioVenta}")
        acPrecioVenta+=precioVenta
if (acPrecioVenta>0):
    print(f"El precio total de todos los articulos es: ${acPrecioVenta}")
print("Ha salido del programa.")