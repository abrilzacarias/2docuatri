Algoritmo sin_titulo
	Definir duracion, dia, turno Como Real
	
	
	Escribir "Ingrese la duraci�n de su llamada (en minutos): "
	Leer duracion
	
	Escribir "Ingrese la opci�n del d�a que desea realizar la llamada: 1: Lunes a s�bado | 2: Domingo"
	Leer dia
	
	Escribir "Ingrese la opci�n del turno en el que desea realizar la llamada: 1: Matutino | 2: Vespertino"
	Leer turno
	
	min5<-1.00
	min6_7<-0.80
	min8_9<-0.70
	min10<-0.50
	
	Si duracion<=5
		pago<-duracion*min5
	SiNo
		Si duracion<=7 Entonces
			min5<-min5*5
			duracion<-(duracion-5)
			pago<-min5+duracion*min6_8
		SiNo
			Si duracion<=9 Entonces
				min5<-min5*5
				duracion<-(duracion-5)
				pago<-min5+duracion*min6_8
			FinSi
		FinSi
		
	FinSi
	
	FinSi
FinAlgoritmo
