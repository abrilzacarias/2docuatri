
Algoritmo area_perimetro
	Definir opcion_selec, radio_circulo, area_circulo, perimetro_circulo Como Real
	
	Definir lado_pent, apotema_pent, perimetro_pentagono, area_pentagono Como Real
	
	Definir lado_h_rec, lado_v_rec, perimetro_rectangulo, area_rectangulo Como Real
	
	Escribir "Ingrese el n�mero de la opci�n que desee obtener: "
	Escribir "opci�n 1: El per�metro y �rea de un c�rculo dado su radio."
	Escribir "opci�n 2: Escribir un programa que calcule el �rea y per�metro de un pent�gono."
	Escribir "opci�n 3: Escribir un programa que calcule el per�metro y �rea de un rect�ngulo."
	Leer opcion_selec 
	
	Segun opcion_selec Hacer
		1:
			Escribir "Ingrese el radio del c�rculo"
			Leer radio_circulo
			area_circulo <- PI * radio_circulo^2
			perimetro_circulo <- 2 * PI * radio_circulo
			Escribir "El �rea del c�rculo es " , area_circulo " y el per�metro del c�rculo es " , perimetro_circulo
		2:
			Escribir "Ingrese el tama�o de un lado del pent�gono"
			Leer lado_pent
			Escribir "Ingrese el apotema del pent�gono"
			Leer apotema_pent
			perimetro_pentagono <- lado_pent * 5
			area_pentagono <- (perimetro_pentagono * apotema_pent) / 2
			Escribir "El per�metro del pent�gono es " , perimetro_pentagono " y el �rea del pent�gono es " , area_pentagono
		3:
			Escribir "Ingrese el tama�o de los lados paralelos horizontales del rect�ngulo"
			Leer lado_h_rec
			Escribir "Ingrese el tama�o de los lados paralelos verticales del rect�ngulo"
			Leer lado_v_rec
			perimetro_rectangulo <- 2*lado_h_rec + 2*lado_v_rec
			area_rectangulo <- lado_h_rec*lado_v_rec
			Escribir "El per�metro del rect�ngulo es " , perimetro_rectangulo " y el �rea del rect�ngulo es " , area_rectangulo
		De Otro Modo:
			Escribir "El n�mero ingresado es incorrecto"
	Fin Segun
	
FinAlgoritmo
