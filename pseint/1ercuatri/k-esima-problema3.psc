Algoritmo ubicacionkesima
	Dimensi�n nros[100]
	Para i<-1 Hasta 100 Con Paso 1 Hacer
		//ciclo pra escribir automaticamente en cada posicion (i) el n�mero k
		nros[i] <- k
		k <- azar(100)
		//funci�n que devuelve n�meros al azar hasta el n�mero entre parentesis, es decir que ser�n todos menores a 100
		//		Si k == 0
		//			k = 0+1
		//		FinSi
		//Estos escribir eran para verificar si se ejecuta correctamente la funci�n azar
//		Escribir k " elemento"
//		Escribir i " posici�n"
	FinPara
	
	Escribir "Ingrese un n�mero para buscar en el arreglo:"
	//Este es el n�mero que se buscar� en el arreglo
	Leer elemento_buscar
	
	no_numero=falso
	
	Para i<-1 Hasta 100 Con Paso 1 Hacer
		
		Si elemento_buscar = nros(i) Entonces
			Escribir "Se ha encontrado el n�mero ",elemento_buscar," en la posici�n ", i
			// para que no se ejecute despu�s el Si de abajo
			no_numero=Verdadero
		FinSi
		
	FinPara
		//se lo coloca fuera del para para que no se ejecute innecesariamente m�s veces
	Si 	no_numero=Falso Entonces
		Escribir "0"
	FinSi
FinAlgoritmo
