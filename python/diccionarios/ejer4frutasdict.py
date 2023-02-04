j,c,frutaMasVendida = True, 0, 0
dictFrutas= {}
while j==True:
    nombreFruta= input("Ingrese el nombre de la fruta: ")
    cantidadFruta= int(input("Ingrese la cantidad de fruta vendida: "))
    precioFruta=int(input("Ingrese el precio de la fruta: "))
    dictFrutas[nombreFruta] = [cantidadFruta, precioFruta]
    nuevaFruta= int(input("¿Desea ingresar otra fruta? \n1)SI 2)NO: "))
    if nuevaFruta==2:
        j=False
    else:
        print("")

frutaMasVendida=0

for k,v in dictFrutas.items():
    if v[0]>=frutaMasVendida:
        frutaMasVendida=v[0]
        frutaListaMasVendida=k
        
print(f"La fruta más vendida fue: {frutaListaMasVendida} ")



