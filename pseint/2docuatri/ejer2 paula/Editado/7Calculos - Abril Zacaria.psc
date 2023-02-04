Algoritmo calculos
//Estaba identado
	//No definió
	Definir op Como Entero
	
	
	Escribir "opción 1 - calculo del perímetro y área de un círculo dado su radio."
	Escribir "opción 2 - calculo del área y perímetro de un pentágono."
	Escribir "opcion 3 - calculo del perímetro y área de un rectángulo."
	Escribir "ingrese una opción: "
	Leer op

	Si op=1 Entonces 
		Definir radio, per, ar Como Real
		
		Escribir "ingrese el radio:"
		Leer radio
		
		per = 2*PI*radio
		ar = PI*radio^2
		
		Escribir "perimetro: " per
		Escribir "área: " ar 
		
	FinSi

	Si op=2 Entonces
		Definir lado, perimetro, apotema, area Como Real
		Escribir "ingrese el valor de uno de los lados: "
		Leer lado
		Escribir "ingrese el valor del apotema: "
		Leer apotema
		
		perimetro = lado*5
		area = (perimetro * apotema)/2 //decìa (perimetro*area) y tiraba error
		
		Escribir "área: " area
		Escribir "perimetro: " perimetro
		
	FinSi
		
	Si op=3
		Definir base, altura Como Real
		Escribir "ingrese la base: "
		Leer base
		Escribir "ingrese la altura: "
		Leer altura
		
		perimetro = 2*(base+altura)
		area = (base*altura)
		
		Escribir "área: " area
		Escribir "perimetro: " perimetro
		
		
	FinSi

FinAlgoritmo
