clientes, descC = 50, 0

for cliente in range(1,3+1):
    produc=float(input("Ingrese el precio del producto: "))
    desc=(produc/100)*(clientes)
    clientes-=1
    print(f"El descuento por el {cliente} cliente es de {desc} ")
    descC+=desc

print(f"El descuento total por los {cliente} clientes es de {descC} ")
