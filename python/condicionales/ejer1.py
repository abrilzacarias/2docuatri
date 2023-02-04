#Sistema de hoteles
hotel1= float(input("Ingrese el presupuesto por día del primer hotel en moneda extranjera: "))
hotel2= float(input("Ingrese el presupuesto por día del segundo hotel en moneda extranjera: "))
hotel3= float(input("Ingrese el presupuesto por día del tercer hotel en moneda extranjera: "))

if ((hotel1>hotel2) & (hotel1>hotel3)):
    nHotel="Hotel 1"
    hotel=hotel1
elif (hotel2>hotel1) & (hotel2>hotel3):
    nHotel="Hotel 2"
    hotel=hotel2
else:
    nHotel="Hotel 3"
    hotel=hotel3

guarani=0.021
hotelCotizado=hotel*guarani
print(f'El hotel más económico es el {nHotel} y su precio cotizado a pesos es de ${hotelCotizado}')
#print(hotel)

#Sistema cheque
dias = int(input("Ingrese la cantidad de días que el empleado debe estar en Asunción: " ))
comida = int(input("Ingrese  el monto para comida por día: "))
otrosGastos= 1500
gastos= hotelCotizado+comida+otrosGastos
cheque=gastos*dias

print(f'El monto del cheque con ${hotelCotizado} de hotel, ${comida} para comida y ${otrosGastos} por día por {dias} días es de: {cheque}')