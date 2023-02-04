SubProceso anos_funcion(ano_actual,ano_cualq)
	Definir anos como Entero
	
	Si ano_actual>ano_cualq Entonces
		anos<-ano_actual-ano_cualq
		Escribir "Desde el año " , ano_cualq " han pasado " , anos " años."
	SiNo
		Si ano_cualq>ano_actual Entonces
			anos<-ano_cualq-ano_actual
			Escribir "Para llegar al año " , ano_cualq " faltan " , anos " años."
		SiNo
			Escribir "Son el mismo año."
		FinSi
	FinSi
FinSubProceso

Algoritmo sin_titulo
	Definir ano_actual,ano_cualq Como Entero
	
	Escribir Sin Saltar "¿En qué año estamos?: "
	Leer ano_actual
	Escribir Sin Saltar "Escriba un año cualquiera: "
	Leer ano_cualq
	anos_funcion(ano_actual,ano_cualq)
FinAlgoritmo
