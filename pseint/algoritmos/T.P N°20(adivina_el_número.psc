Algoritmo adivina_el_n�mero
	intentos<-10
	n�m_secreto<-azar(100)+1
	Escribir "ingrese un valor"
	Leer num_ingresado
	Mientras num_ingresado<>n�m_secreto y intentos>1 Hacer
		Si n�m_secreto>num_ingresado Entonces
			Escribir "Incorrecto! El n�mero tiene que ser mayor";
		SiNo
			
			Escribir "Incorrecto! El n�mero tiene que ser menor"
		Fin Si
		
		intentos<-intentos-1	
		Escribir "Intentos restantes:",intentos, " intentos";
		Leer num_ingresado
	Fin Mientras
	Si num_ingresado=n�m_secreto Entonces
		Escribir "Correcto! Adivino en ", 11-intentos," intentos.", "El n�mero secreto era: ",n�m_secreto
	SiNo
		Escribir "El n�mero era: ", n�m_secreto
	Fin Si
FinAlgoritmo
