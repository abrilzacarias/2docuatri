Algoritmo camisas
	Definir precio, cantidad, descuento_20, descuento_10, descuento_final20, descuento_final10, precio_cantidad Como Entero
	
	Escribir "¿Cuántas camisas desea comprar?"
	Leer cantidad
	Escribir "¿Qué precio tienen las camisas?"
	Leer precio
	
	
	precio_cantidad <- precio*cantidad
	
	Si cantidad >= 3 Entonces
		descuento_20 <- (precio_cantidad/100)*20
		descuento_final20 <- precio_cantidad - descuento_20
		Escribir "El precio final aplicado el 20% de descuento es de: " , descuento_final20
	SiNo
		descuento_10 <- (precio_cantidad/100)*10
		descuento_final10 <- precio_cantidad - descuento_10
		Escribir "El precio final aplicado el 10% de descuento es de: " , descuento_final10
	FinSi
FinAlgoritmo
