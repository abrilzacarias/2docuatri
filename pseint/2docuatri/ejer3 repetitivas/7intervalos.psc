Algoritmo intervalos
	Definir inferior, superior, nro, contador, suma_nros Como Real
	
	inferior<-0
	superior<-0
	
	Repetir
		Escribir "Ingrese el l�mite inferior del intervalo"
		Leer inferior
		
		Escribir "Ingrese el l�mite superior del intervalo"
		Leer superior
		Si inferior>superior
			Escribir "Error: El limite inferior debe ser menor que el l�mite superior. "
		FinSi
	Hasta Que inferior<superior
	
	nro<-1
	suma_nros<-0
	contador<-0
	Mientras nro <> 0
		Escribir "Introduce un n�mero (Introduzca 0 para salir):"
		Leer nro
		Si nro > inferior Y nro < superior Entonces
			suma_nros<-suma_nros+nro
		SiNo
			contador<-contador+1
		FinSi
	FinMientras
	
	Escribir "La suma de los n�meros que est�n dentro del intervalo es de: " , suma_nros
	Escribir "Cantidad de n�meros fuera del intervalo: " , contador-1
FinAlgoritmo
