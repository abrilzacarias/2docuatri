Algoritmo moto
	Definir dia, precio_moto Como Entero
	Definir descuento_1, descuento_final1 Como Entero
	Definir descuento_2, descuento_final2 Como Entero
	Definir descuento_3, descuento_final3 Como Entero
	
	Escribir "¿Qué día va a comprar su moto?"
	Escribir "Seleccione 1 si martes"
	Escribir "Seleccione 2 si sábado"
	Escribir "Seleccione 3 si feriado"
	Leer dia
	
	Escribir "¿Cuál es el precio de la moto?"
	Leer precio_moto
	
	Segun dia Hacer
		1:
			descuento_1 <- (precio_moto/100)*12
			descuento_final1 <- precio_moto - descuento_1
			Escribir "Si compra la moto un martes, pagará " descuento_final1 " con descuento del 15%"
		2:
			descuento_2 <- (precio_moto/100)*18
			descuento_final2 <- precio_moto - descuento_2
			Escribir "Si compra la moto un sábado, pagará " descuento_final2 " con descuento del 18%"
		3:
			descuento_3 <- (precio_moto/100)*25
			descuento_final3 <- precio_moto - descuento_3
			Escribir "Si compra la moto un feriado, pagará " descuento_final3 " con descuento del 18%"
		De Otro Modo:
			Escribir "NO hay promociones vigentes ese día"
	Fin Segun
	
FinAlgoritmo
