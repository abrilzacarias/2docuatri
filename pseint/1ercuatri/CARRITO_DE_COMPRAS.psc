Algoritmo matriz
	
	//creamos la matriz y le damos un numero de filas y columnas
	Dimension matr[11,3];
	
	//le damos valores a la matriz 
	matr[1,1]<-"1";      
	matr[1,2]<-"Left 4 Dead 2";  
    matr[1,3]<-"129";  
	matr[2,1]<-"2";     
	matr[2,2]<-"Rust";  
    matr[2,3]<-"2440";  
	matr[3,1]<-"3";      
	matr[3,2]<-"Resident Evil 3";  
    matr[3,3]<-"2499";  
	matr[4,1]<-"4";     
	matr[4,2]<-"FIFA 22";  
    matr[4,3]<-"5499";  
	matr[5,1]<-"5";      
	matr[5,2]<-"Red Dead Redemption 2";  
    matr[5,3]<-"2499";  
	matr[6,1]<-"6";     
	matr[6,2]<-"Grand Thef Auto IV: The Complete Edition";  
    matr[6,3]<-"1299";
	matr[7,1]<-"7";      
	matr[7,2]<-"Call of Duty: Black Ops III-Zombies Choronicles Edition";  
    matr[7,3]<-"999";  
	matr[8,1]<-"8";     
	matr[8,2]<-"NBA 2K22";  
    matr[8,3]<-"5999.00"; 
	matr[9,1]<-"9";      
	matr[9,2]<-"Phasmphobia";  
    matr[9,3]<-"169";  
	matr[10,1]<-"10";     
	matr[10,2]<-"Prince of Persia";  
    matr[10,3]<-"499.99";
	matr[10,1]<-"11";
	matr[10,2]<-"Escriba un juego que no esté en la lista";
	matr[10,3]<-"0";
	
	//imprimimos los datos para su visualizacion
	
	//mostramos todos los datos que hay en la matriz con dos ciclos PARA 
    Para i<-1 Hasta 10 Con Paso 1 Hacer
	    Para j<-1 Hasta 3 Con Paso 1 Hacer
			Escribir Sin Saltar matr[i,j] "|"
		FinPara
		Escribir " "
	FinPara
	
	Para i<-1 Hasta 10 Con Paso 1 Hacer
		Para j<-1 Hasta 3 Con Paso 2 Hacer
			num<-ConvertirANumero(matr[i,j]);
			//Escribir num;
		FinPara
	FinPara
	
	Escribir "Elija el numero de juego que desea comprar"
	Leer num
	
	Si num>=1 Y num<=10 Entonces
		Escribir "el nombre del juego es ", matr[num,2], " y su precio es " , matr[num,3]
	SiNo
		Si num==11 Entonces
			Escribir "Ingrese el nombre del juego"
			Leer nombre
			Escribir "Y su precio"
			Leer precio
			matr[10,2]<-nombre;
			matr[10,3]<-precio;
		SiNo
				Escribir "El número de juego esta fuera del rango"
		FinSi
	FinSi
	
FinAlgoritmo