Algoritmo llantas
	Definir cant_llantas, costo_llanta1, costollanta_undesc, costollanta_final, descuento_20 Como Entero
	Definir nombre Como Caracter
	Definir costo_llanta2, descuento_25 Como Entero
	
	Escribir "Ingrese su nombre"
	Leer nombre
	Escribir "¿Cuántas llantas desea comprar?"
	Leer cant_llantas
	

	Si cant_llantas < 12
		costo_llanta1 <- 2500
		descuento_20 <- (costo_llanta1/100)*20
		costollanta_undesc <- costo_llanta1 - descuento_20
		costollanta_final <- costollanta_undesc*cant_llantas
		Escribir "El nombre del cliente es " , nombre " y el precio final a pagar por " , cant_llantas " llantas es de: " costollanta_final
	SiNo
		//funcion?
		costo_llanta2 <- 2200
		descuento_25 <- (costo_llanta2/100)*25
		costollanta_undesc <- costo_llanta2 - descuento_25
		costollanta_final <- costollanta_undesc*cant_llantas
		Escribir "El nombre del cliente es " , nombre " y el precio final a pagar por " , cant_llantas " llantas es de: " costollanta_final
	FinSi
	
	
FinAlgoritmo
