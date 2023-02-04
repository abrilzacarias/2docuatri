Algoritmo kms
	Definir monto_fijo, km, imp, monto_ad, monto_ad_final, monto_ad_final2, impuesto, impuesto2 Como Entero
	
	monto_fijo <- 300000
	Escribir "¿Cuàntos kilómetros recorró el vehículo alquilado?"
	Leer km
	
	
	Si km < 300 Entonces
		imp <- (monto_fijo/100)*20
		Escribir "El monto total a pagar es de: $" , monto_fijo
		Escribir "El monto del impuesto IVA es de: $" imp
	FinSi
	Si km >= 300 Y km <= 1000 Entonces
		monto_ad <- km - 300
		monto_ad_final <- monto_fijo+(monto_ad*15000)
		impuesto <- (monto_ad_final/100)*20
		Escribir "El monto total a pagar es de: $" , monto_ad_final
		Escribir "El monto del impuesto IVA es de: $" impuesto
	FinSi
	Si km > 1000 Entonces
		monto_ad <- km - 300
		monto_ad_final2 <- monto_fijo+(monto_ad*10000)
		impuesto2 <- (monto_ad_final2/100)*20
		Escribir "El monto total a pagar es de: $" , monto_ad_final2
		Escribir "El monto del impuesto IVA es de: $" impuesto2
	FinSi
	
	
FinAlgoritmo
