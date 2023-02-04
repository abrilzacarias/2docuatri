
Algoritmo area_perimetro
	Definir opcion_selec, radio_circulo, area_circulo, perimetro_circulo Como Real
	
	Definir lado_pent, apotema_pent, perimetro_pentagono, area_pentagono Como Real
	
	Definir lado_h_rec, lado_v_rec, perimetro_rectangulo, area_rectangulo Como Real
	
	Escribir "Ingrese el número de la opción que desee obtener: "
	Escribir "opción 1: El perímetro y área de un círculo dado su radio."
	Escribir "opción 2: Escribir un programa que calcule el área y perímetro de un pentágono."
	Escribir "opción 3: Escribir un programa que calcule el perímetro y área de un rectángulo."
	Leer opcion_selec 
	
	Segun opcion_selec Hacer
		1:
			Escribir "Ingrese el radio del círculo"
			Leer radio_circulo
			area_circulo <- PI * radio_circulo^2
			perimetro_circulo <- 2 * PI * radio_circulo
			Escribir "El área del círculo es " , area_circulo " y el perìmetro del cìrculo es " , perimetro_circulo
		2:
			Escribir "Ingrese el tamaño de un lado del pentágono"
			Leer lado_pent
			Escribir "Ingrese el apotema del pentágono"
			Leer apotema_pent
			perimetro_pentagono <- lado_pent * 5
			area_pentagono <- (perimetro_pentagono * apotema_pent) / 2
			Escribir "El perímetro del pentágono es " , perimetro_pentagono " y el área del pentágono es " , area_pentagono
		3:
			Escribir "Ingrese el tamaño de los lados paralelos horizontales del rectángulo"
			Leer lado_h_rec
			Escribir "Ingrese el tamaño de los lados paralelos verticales del rectángulo"
			Leer lado_v_rec
			perimetro_rectangulo <- 2*lado_h_rec + 2*lado_v_rec
			area_rectangulo <- lado_h_rec*lado_v_rec
			Escribir "El perímetro del rectángulo es " , perimetro_rectangulo " y el área del rectángulo es " , area_rectangulo
		De Otro Modo:
			Escribir "El número ingresado es incorrecto"
	Fin Segun
	
FinAlgoritmo
