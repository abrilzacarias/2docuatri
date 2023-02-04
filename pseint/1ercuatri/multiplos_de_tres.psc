Algoritmo  multiplos_de_tres
	Dimension arreglo[500]
	Para i<-1 Hasta 500 Con Paso 1 Hacer 
		arreglo[i]<-3^i;
		//Escribir arreglo[i]
	FinPara
	Escribir "Ingresar un numero positivo para saber si es o no potencia de 3(1-1000): "
	Leer num
	c<-0
	Para i<-1 Hasta 500 Con Paso 1 Hacer 
		Si num==arreglo[i] Entonces
			Escribir "El numero ingresado ", num, " es potencia de 3"
			c<-1
		FinSi
	FinPara
	Si c==0 Entonces
		Escribir "El numero ingresado ", num, " no es potencia de 3"
	FinSi

FinAlgoritmo

