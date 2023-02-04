dias, acGasto, acKm, acRecaudado = 0, 0, 0, 0

kmRecorridos=int(input("Ingrese la cantidad de kilómetros recorridos: "))

if kmRecorridos==0:
    print("Ingrese un número que no sea 0.")
else:
    while (kmRecorridos!=0):
        acKm+=kmRecorridos
        
