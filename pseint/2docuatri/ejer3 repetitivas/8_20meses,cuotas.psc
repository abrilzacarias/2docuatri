Algoritmo cuotas
	Definir cuota, cont, suma_total Como Real
	
	suma_total<-0

	cuota<-1000
	Para cont<-1 Hasta 20 Hacer
		suma_total<-suma_total+cuota
		Escribir "En el mes " , cont " debe pagar $" ,cuota
		cuota<-cuota+1000

	FinPara
	
	Escribir "El total de lo que pagó después de los 20 meses es de: $" ,suma_total
FinAlgoritmo
