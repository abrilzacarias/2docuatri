Algoritmo fecha
	Definir dia, mes, ano Como Entero
	
	Escribir "Ingrese un día"
	Leer dia
	Escribir "Ingrese un mes"
	Leer mes
	Escribir "Ingrese un año"
	Leer ano
	
	Si dia < 1 o dia > 31 Entonces
		Escribir "El día no es válido"
	SiNo
		Si mes < 1 o mes > 12 Entonces
			Escribir "El mes no es válido"
		SiNo
			Segun mes Hacer
				4,6,9,11:
					Si dia > 30
						Escribir "Este mes sólo cuenca con 30 días."
					FinSi
				2:
					Si dia > 28
						Escribir "Este mes sólo cuenta con 28 días."
					FinSi
			Fin Segun
			Si ano > 0 Entonces
				Escribir dia , "/" , mes "/" , ano 
				
			SiNo
				Escribir "El año no es válido"
			FinSi
		FinSi
	FinSi
FinAlgoritmo
