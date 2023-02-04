Algoritmo triangulos
	Definir long1, long2, long3, suma2_lados, suma2_lados2, suma2_lados3 Como Entero
	Definir lados_iguales, lados_iguales2, lados_iguales3 Como Logico
	
	Escribir "Ingrese las 3 longitudes:"
	Leer long1, long2, long3
	
	//long_mayor1 <- long1>long2 Y long1>long3
	//long_mayor2 <- long2>long1 Y long2>long3
	//long_mayor3 <- long3>long2 Y long3>long2
	
	Si long1>long2 Y long1>long3 Entonces
		suma2_lados <- long2+long3
		Si long1 < long2+long3 Entonces
			//si es triangulo
			lados_iguales<- long2=long3
			Si lados_iguales=Verdadero Entonces
				Escribir "Se trata de un triángulo isósceles"
			SiNo
				Escribir "Se trata de un triángulo escaleno"
			FinSi
		SiNo
			Escribir "No se trata de un triángulo"
		FinSi
	FinSi
	Si long2>long1 Y long2>long3 Entonces
		suma2_lados2 <- long1+long3
		Si long2 < long1+long3 Entonces
			//si es triangulo
			lados_iguales2<- long1=long3
			Si lados_iguales2=Verdadero Entonces
				Escribir "Se trata de un triángulo isósceles"
			SiNo
				Escribir "Se trata de un triángulo escaleno"
			FinSi
		SiNo
			Escribir "No se trata de un triángulo"
		FinSi
	FinSi
	Si long3>long1 Y long3>long2 Entonces
		suma2_lados3 <- long1+long2
		Si long3 < long1+long2 Entonces
			//si es triangulo
			lados_iguales3<- long1=long2
			Si lados_iguales3=Verdadero Entonces
				Escribir "Se trata de un triángulo isósceles"
			SiNo
				Escribir "Se trata de un triángulo escaleno"
			FinSi
		SiNo
			Escribir "No se trata de un triángulo"
		FinSi
	FinSi
	Si long1=long2 Y long2=long3 Entonces
		Escribir "Se trata de un triángulo equilátero"
	FinSi
FinAlgoritmo
