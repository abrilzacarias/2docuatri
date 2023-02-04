Algoritmo Quienes_Limpian_El_Curso
	Dimension Alumno[34];
	definir i Como Entero;
	definir NumAleatorio como entero
	Definir Resp Como caracter
	Definir Presente Como Logico
	
	Alumno[1]= "Aguayo, Fabricio"
	Alumno[2]= "Arzamendia, Marcos"
	Alumno[3]= "Avila, Fabian"
	Alumno[4]= "Barrios, Cristian"
	Alumno[5]= "Britos, Sergio"
	Alumno[6]= "Cano, Brenda"
	Alumno[7]= "Cespedes, Melani"
	Alumno[8]= "Chavez, Evelin"
	Alumno[9]= "Chavez, Ingrid"
	Alumno[10]= "Diaz, Rodrigo"
	Alumno[11]= "Esquivel, Milagros"
	Alumno[12]= "Fleitas, Camilo"
	Alumno[13]= "Galeano, Santiago"
	Alumno[14]= "Garcia, Lucas"
	Alumno[15]= "Gomez, Fabricio"
	Alumno[16]= "Gomez, Marisa"
	Alumno[17]= "Gomez, Miguel"
	Alumno[18]= "Gonzalez, Guillermo"
	Alumno[19]= "Gonzalez, Ludmila"
	Alumno[20]= "Gonzalez, Natalia"
	Alumno[21]= "Ledesma, Jorge"
	Alumno[22]= "Lopez, Gabriel"
	Alumno[23]= "Martinez, Carla"
	Alumno[24]= "Ortiz, Sheila"
	Alumno[25]= "Pujol, Catriel"
	Alumno[26]= "Resquin, Agustina"
	Alumno[27]= "Rivero, Pablo"
	Alumno[28]= "Rodriguez, Mariano"
	Alumno[29]= "Rodriguez, Marisol"
	Alumno[30]= "Salinas, Amanda"
	Alumno[31]= "Sinsig, Sofia"
	Alumno[32]= "Vera, Iron"
	Alumno[33]= "Villalba, Florencia"
	Alumno[34]= "Franco, Pedro"
	
	Escribir  "¿Desea empezar el sistema para elegir quienes limpian el curso hoy?. Ingrese S o N"
	leer Resp
	si resp = "S" entonces
		Mientras i <3 Hacer
			NumAleatorio = 1 +azar (34)
			Escribir  "El elegido es: ", alumno[numaleatorio]
			Escribir "¿Está ausente?. Ingresar S o N según corresponda"
			leer Resp
			Si Resp = "S" Entonces
				Presente = Falso
			Sino
				Presente = Verdadero
				i = i +1
			Fin Si
		Fin Mientras
		//Escribir  "Desarrollado por Matías Aveiro"
	fin si
	
	//Repetir
		//NumAleatorio = 1+ azar (34)
		//Escribir  "El elegido es: ", alumno[numaleatorio]
	//Hasta Que numaleatorio = 1
		
FinAlgoritmo
