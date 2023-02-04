Algoritmo arreglos
	
	//pedimos el numero de filas
	Escribir "Digite el numero de filas";
	Leer f;
	
	//pedimos el numero de columnas
	Escribir "Digite el numero de columnas";
	Leer c;
	
	//creamos la matriz y le pasamos el numero de filas y el numero de columnas
	Dimension matriz[f,c];
	
	//llenamos la matriz con dos ciclos PARA, uno para las filas y otro para las columnas
	Para i<-1 Hasta f Con Paso 1 Hacer
		Para j<-1 Hasta c Con Paso 1 Hacer
			
			//pedimos los datos
			Escribir "Digite datos para la fila ",i ," columna ", j;
			Leer numer;
			
			//llenamos la matriz con los numeros ingresados
			matriz[i,j]<-numer;
		FinPara
		
	Fin Para
	
	//mostramos todos los datos que hay en la matriz con dos ciclos PARA 
    Para i<-1 Hasta f Con Paso 1 Hacer
	    Para j<-1 Hasta c Con Paso 1 Hacer
			Escribir "Los datos que hay en la matriz son ", matriz[i,j];
		FinPara
		
	FinPara
	

	
	
FinAlgoritmo
