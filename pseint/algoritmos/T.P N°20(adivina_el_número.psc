Algoritmo adivina_el_número
	intentos<-10
	núm_secreto<-azar(100)+1
	Escribir "ingrese un valor"
	Leer num_ingresado
	Mientras num_ingresado<>núm_secreto y intentos>1 Hacer
		Si núm_secreto>num_ingresado Entonces
			Escribir "Incorrecto! El número tiene que ser mayor";
		SiNo
			
			Escribir "Incorrecto! El número tiene que ser menor"
		Fin Si
		
		intentos<-intentos-1	
		Escribir "Intentos restantes:",intentos, " intentos";
		Leer num_ingresado
	Fin Mientras
	Si num_ingresado=núm_secreto Entonces
		Escribir "Correcto! Adivino en ", 11-intentos," intentos.", "El número secreto era: ",núm_secreto
	SiNo
		Escribir "El número era: ", núm_secreto
	Fin Si
FinAlgoritmo
