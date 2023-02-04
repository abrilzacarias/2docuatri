Algoritmo sin_titulo
	Definir duracion, minutos_ac, dia, turno, min, min10, min5, min6_8, min8_9, turno_matutino, turno_ves, pago, domingo Como Real
	
	
	Escribir "Ingrese la duración de su llamada (en minutos): "
	Leer duracion
	
	Escribir "Ingrese la opción del día que desea realizar la llamada: 1: Lunes a sábado | 2: Domingo"
	Leer dia
	
	min5<-1.00
	min6_8<-0.80
	min8_9<-0.70
	min10<-0.50
	
	Si duracion<=5
		pago<-duracion*min5
	SiNo
		Si duracion<=8 Entonces
			minutos_ac<-min5*5
			duracion<-(duracion-5)
			pago<-minutos_ac+duracion*min6_8
		SiNo
			Si duracion<=10 Entonces
				minutos_ac<-minutos_ac+0.80*3
				duracion<-(duracion-8)
				pago<-minutos_ac+duracion*min8_9
			SiNo
				minutos_ac<-minutos_ac+0.70*2
				duracion<-(duracion-10)
				pago<-minutos_ac+duracion*min10
			FinSi
		FinSi
	FinSi
	
	Segun dia Hacer
		1://habil
			Escribir "Ingrese la opción del turno en el que desea realizar la llamada: 1: Matutino | 2: Vespertino"
			Leer turno
			Segun turno Hacer
				1://matutino
					turno_matutino<-pago/100*15
					Escribir "El precio de la llamada es de: $",pago " y con los impuestos incluidos es de: " ,turno_matutino+pago
				De Otro Modo://vespertino
					turno_ves<-pago/100*10
					Escribir "El precio de la llamada es de: $",pago " y con los impuestos incluidos es de: " ,turno_ves+pago
			Fin Segun
		2:
			domingo<-pago/100*3
			Escribir "El precio de la llamada es de: $",pago " y con los impuestos incluidos es de: " ,domingo+pago
	Fin Segun
	
FinAlgoritmo
