pais = float(input(f"""Ingrese la zona a la que va dirigido el paquete: 
    1. América del Norte 
    2. América Central 
    3. América del Sur 
    4. Europa 
    5. Asia
    """))

gramos = float(input(f'Ingrese la cantidad de gramos que pesa su paquete: '))

if (gramos <= 5000):
    if pais==1:
        precio=gramos*11.00
    elif pais==2:
        precio=gramos*10.00
    elif pais==3:
        precio=gramos*12.00
    elif pais==4:
        precio=gramos*24.00
    elif pais==5:
        precio=gramos*27.00
    print(f"El cobro por la entrega de un paquete es de: {precio} ")
else:
    print("Se ha rechazado su paquete")