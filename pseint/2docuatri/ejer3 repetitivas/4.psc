Algoritmo sin_titulo
	Definir c, nro, calculo, suma,n Como Real
	c<-0
	suma<-0
	n<-0
	Repetir
		c<-c+1
		Escribir "Escriba un número (0 para finalizar)"
		Leer nro
		suma<- suma+nro
		calculo<- suma/c
		Escribir "Suma:" , suma
		Escribir "Media: " ,calculo
	Hasta Que nro==0
FinAlgoritmo
