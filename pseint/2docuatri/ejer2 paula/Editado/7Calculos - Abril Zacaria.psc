Algoritmo calculos
//Estaba identado
	//No defini�
	Definir op Como Entero
	
	
	Escribir "opci�n 1 - calculo del per�metro y �rea de un c�rculo dado su radio."
	Escribir "opci�n 2 - calculo del �rea y per�metro de un pent�gono."
	Escribir "opcion 3 - calculo del per�metro y �rea de un rect�ngulo."
	Escribir "ingrese una opci�n: "
	Leer op

	Si op=1 Entonces 
		Definir radio, per, ar Como Real
		
		Escribir "ingrese el radio:"
		Leer radio
		
		per = 2*PI*radio
		ar = PI*radio^2
		
		Escribir "perimetro: " per
		Escribir "�rea: " ar 
		
	FinSi

	Si op=2 Entonces
		Definir lado, perimetro, apotema, area Como Real
		Escribir "ingrese el valor de uno de los lados: "
		Leer lado
		Escribir "ingrese el valor del apotema: "
		Leer apotema
		
		perimetro = lado*5
		area = (perimetro * apotema)/2 //dec�a (perimetro*area) y tiraba error
		
		Escribir "�rea: " area
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
		
		Escribir "�rea: " area
		Escribir "perimetro: " perimetro
		
		
	FinSi

FinAlgoritmo
