Algoritmo  multiplos_de_tres
	Dimension arreglo[646]
	//646 ya que sale error si se eleva a un número más alto
	Para i<-1 Hasta 646 Con Paso 1 Hacer 
		arreglo[i]<-3^i;
		//Escribir arreglo[i]
	FinPara
	Escribir "Ingresar un numero positivo para saber si es o no potencia de 3"
	//Este es el número que se buscará en el arreglo
	Leer num
	c<-1
	Para i<-1 Hasta 646 Con Paso 1 Hacer 
		Si num==arreglo[i] Entonces
			Escribir "El numero ingresado ", num, " es potencia de 3"
			c<-0
			//Si se ejecuta el si, c pasa a valer 0 para que no se ejecute el si siguiente
		FinSi
	FinPara
	//se coloca fuera del para para que no se repita innecesariamente
	Si c==1 Entonces
		Escribir "El numero ingresado ", num, " no es potencia de 3"
	FinSi
FinAlgoritmo


