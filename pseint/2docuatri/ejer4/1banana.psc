Algoritmo bananas
	Definir precio_inicial, precio_final, precio_banana, ganancia, perdida Como Real
	Definir tamano,doc_bananas, doc Como Entero
	Definir tipo Como Caracter
	
	Escribir "Ingrese la cantidad de docenas: "
	Leer doc
	
	Escribir "Ingrese el precio inicial de la docena de bananas: "
	Leer precio_inicial
	
	doc_bananas<-doc*precio_inicial

		Escribir "Seleccione un tipo (A o B):"
		Leer tipo
		
		Escribir "Seleccione un tamaño (1 o 2):"
		Leer tamano
		Si tipo="A" o tipo="a" Entonces
			Si tamano=1 Entonces
				precio_final<-doc_bananas+200
				ganancia<-precio_final-precio_inicial*doc
				Escribir "El precio final de la docena de bananas es: " precio_final
				Escribir "La ganancia de la docena de bananas es: " ganancia
			SiNo
				precio_final<-doc_bananas+300
				ganancia<-precio_final-precio_inicial*doc
				Escribir "El precio final de la docena de bananas es: " precio_final
				Escribir "La ganancia de la docena de bananas es: " ganancia
			FinSi
		SiNo
			Si tamano=1 Entonces
				precio_final<-doc_bananas-30
				ganancia<-precio_final-precio_inicial*doc
				Si ganancia<0 Entonces
					perdida<-ganancia*(-1)
					Escribir "La pérdida de la docena de bananas es: " perdida
				SiNo
					Escribir "El precio final de la docena de bananas es: " precio_final
					Escribir "La ganancia de la docena de bananas es: " ganancia
				FinSi
				
			SiNo
				precio_final<-doc_bananas-50
				ganancia<-precio_final-precio_inicial*doc
				
				Si ganancia<0 Entonces
					perdida<-ganancia*(-1)
					Escribir "La pérdida de la docena de bananas es: " perdida
				SiNo
					Escribir "La ganancia de la docena de bananas es: " ganancia
					Escribir "El precio final de la docena de bananas es: " precio_final
				FinSi
				
			FinSi
	FinSi
	

	
FinAlgoritmo
