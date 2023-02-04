Algoritmo ubicacionkesima
	Dimensión nros[100]
	Para i<-1 Hasta 100 Con Paso 1 Hacer
		//ciclo pra escribir automaticamente en cada posicion (i) el número k
		nros[i] <- k
		k <- azar(100)
		//función que devuelve números al azar hasta el número entre parentesis, es decir que serán todos menores a 100
		//		Si k == 0
		//			k = 0+1
		//		FinSi
		//Estos escribir eran para verificar si se ejecuta correctamente la función azar
//		Escribir k " elemento"
//		Escribir i " posición"
	FinPara
	
	Escribir "Ingrese un número para buscar en el arreglo:"
	//Este es el número que se buscará en el arreglo
	Leer elemento_buscar
	
	no_numero=falso
	
	Para i<-1 Hasta 100 Con Paso 1 Hacer
		
		Si elemento_buscar = nros(i) Entonces
			Escribir "Se ha encontrado el número ",elemento_buscar," en la posición ", i
			// para que no se ejecute después el Si de abajo
			no_numero=Verdadero
		FinSi
		
	FinPara
		//se lo coloca fuera del para para que no se ejecute innecesariamente más veces
	Si 	no_numero=Falso Entonces
		Escribir "0"
	FinSi
FinAlgoritmo
