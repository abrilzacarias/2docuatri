Algoritmo sin_titulo
	Definir cant,c,nro,cont1, cont2, cont3 Como Real
	
	Escribir "Cantidad de n�meros a introducir: "
	Leer cant
	
	cont1<-0
	cont2<-0
	cont3<-0
	c<-0
	
	Mientras c<cant Hacer
		c<-c+1
		Escribir "Ingrese un n�mero: "
		Leer nro
		Si nro<0
			cont1<-cont1+1
		SiNo
			Si nro>0
				cont2<-cont2+1
			SiNo
				cont3<-cont3+1
			FinSi
		FinSi
	FinMientras
	Escribir "N�meros menores a 0: " ,cont1
	Escribir "N�meros mayores a 0: " ,cont2
	Escribir "N�meros iguales a 0: " ,cont3
	
FinAlgoritmo
