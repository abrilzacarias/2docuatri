SubProceso temp_media(max,min)
	Definir media Como Real
	Si max<min Entonces
		Escribir "La temperatura máxima no es correcta"
	SiNo
		media<-(max+min)/2
		Si media<>100 Entonces
			Escribir "La media es: " ,media
		FinSi		
	FinSi
	
FinSubProceso


Algoritmo sin_titulo
	Definir max, min Como Real
	
	Repetir
		Escribir "Ingrese la temperatura máxima"
		Leer max
		Escribir "Ingrese la temperatura mínima (Ingrese 100 para salir del programa)"
		Leer min
		temp_media(max,min)
	Hasta Que min=100
	
	Escribir "Ha salido del programa."
FinAlgoritmo
