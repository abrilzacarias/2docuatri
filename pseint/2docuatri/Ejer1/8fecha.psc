Algoritmo fecha
	Definir dia, mes, ano Como Entero
	
	Escribir "Ingrese un d�a"
	Leer dia
	Escribir "Ingrese un mes"
	Leer mes
	Escribir "Ingrese un a�o"
	Leer ano
	
	Si dia < 1 o dia > 31 Entonces
		Escribir "El d�a no es v�lido"
	SiNo
		Si mes < 1 o mes > 12 Entonces
			Escribir "El mes no es v�lido"
		SiNo
			Segun mes Hacer
				4,6,9,11:
					Si dia > 30
						Escribir "Este mes s�lo cuenca con 30 d�as."
					FinSi
				2:
					Si dia > 28
						Escribir "Este mes s�lo cuenta con 28 d�as."
					FinSi
			Fin Segun
			Si ano > 0 Entonces
				Escribir dia , "/" , mes "/" , ano 
				
			SiNo
				Escribir "El a�o no es v�lido"
			FinSi
		FinSi
	FinSi
FinAlgoritmo
