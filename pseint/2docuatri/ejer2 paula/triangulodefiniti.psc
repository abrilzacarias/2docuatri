Algoritmo sin_titulo
	Definir lado1,lado2,lado3, ladoMayor, sumaLados Como Entero
	Definir tipoTriang Como Caracter
	
	Escribir "Lados:"
	Leer lado1,lado2,lado3
	
	ladoMayor <- lado1
	Si (lado2>ladoMayor) Entonces
		ladoMayor<-lado2
		
	FinSi
	Si (lado3>ladoMayor) Entonces
		ladoMayor<-lado3
	FinSi
	sumaLados<- (lado1+lado2+lado3)-ladoMayor
	
	Si (ladoMayor<sumaLados) Entonces
		Escribir "Es triángulo"
		Si ((lado1=lado2) Y (lado2=lado3) Y (lado1=lado3)) Entonces
			tipoTriang <- "Equilátero"
		SiNo
			Si ((lado1<>lado2) Y (lado1<>lado3) Y (lado2<>ado3)) Entonces
				tipoTriang <- "Escaleno"
			SiNo
				tipoTriang <- "Isósceles"
			FinSi
		FinSi
	SiNo
		Escribir "No es un triángulo"
	FinSi
FinAlgoritmo
