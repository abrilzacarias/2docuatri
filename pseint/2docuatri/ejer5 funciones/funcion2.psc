SubProceso anos_funcion(ano_actual,ano_cualq)
	Definir anos como Entero
	
	Si ano_actual>ano_cualq Entonces
		anos<-ano_actual-ano_cualq
		Escribir "Desde el a�o " , ano_cualq " han pasado " , anos " a�os."
	SiNo
		Si ano_cualq>ano_actual Entonces
			anos<-ano_cualq-ano_actual
			Escribir "Para llegar al a�o " , ano_cualq " faltan " , anos " a�os."
		SiNo
			Escribir "Son el mismo a�o."
		FinSi
	FinSi
FinSubProceso

Algoritmo sin_titulo
	Definir ano_actual,ano_cualq Como Entero
	
	Escribir Sin Saltar "�En qu� a�o estamos?: "
	Leer ano_actual
	Escribir Sin Saltar "Escriba un a�o cualquiera: "
	Leer ano_cualq
	anos_funcion(ano_actual,ano_cualq)
FinAlgoritmo
