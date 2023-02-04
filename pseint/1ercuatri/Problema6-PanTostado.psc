Algoritmo PanTostado
	Escribir "Tomar el pan"
	Escribir "Colocarlo en la tostadora"
	Escribir "Prender la tostadora"
	pan_tostado <- Falso
	Mientras pan_tostado = Falso Hacer
			Repetir 		
				tostar <- "El pan se está tostando"
				i = i+1
				Escribir tostar
			Hasta Que i == 3
			pan_tostado <- Verdadero
	Fin Mientras
	Escribir "El pan terminó de tostarse"
FinAlgoritmo
