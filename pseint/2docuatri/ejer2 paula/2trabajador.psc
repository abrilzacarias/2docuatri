Algoritmo trabajador
	Definir sueldo, base, sueldo_base, descuento_10, descuento_final10 Como Real
	Definir descuento_5, descuento_final5 Como Real
	Definir descuento_3, descuento_final3 Como Real
	
	Escribir "¿Cuál es el sueldo del trabajador?"
	Leer sueldo
	base <- 1000
	
	Si sueldo <= 1000 Entonces
		descuento_10 <- (sueldo/100)*10
		descuento_final10 <- sueldo - descuento_10
		Escribir "El sueldo neto es de: " , descuento_final10 " y aplicado el descuento del 10% es de: " descuento_10
	FinSi
	Si sueldo > 1000 Y sueldo <= 2000 Entonces
		sueldo_base <- sueldo - base
		descuento_5 <- (sueldo_base/100)*5
		descuento_final5 <- sueldo - descuento_5
		Escribir "El sueldo neto es de: " , descuento_final5 " y aplicado el descuento del 5% es de: " descuento_5
	FinSi
	Si sueldo > 2000 Entonces
		descuento_3 <- (sueldo/100)*3
		descuento_final3 <- sueldo - descuento_3
		Escribir "El sueldo neto es de: " , descuento_3 " y aplicado el descuento del 3% es de: " descuento_3
	FinSi

FinAlgoritmo
