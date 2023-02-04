Algoritmo Prog_TP1_EJER1
	Definir triangulo_area, rectangulo_area, area_final, lado_a, lado_b, lado_c Como Real
	
	Escribir "Ingrese el lado A del lote: "
	Leer lado_a
	Escribir "Ingrese el lado B del lote: "
	Leer lado_b
	Escribir "Ingrese el lado C del lote: "
	Leer lado_c
	
	triangulo_area<-lado_b*(lado_a-lado_c)/2
	rectangulo_area<-lado_b*(lado_a-lado_c)
	//rectangulo_area<-lado_b*lado_c
	area_final<- rectangulo_area+triangulo_area
	
	Escribir "El valor del área calculada es de: " , area_final
	
	Si area_final<=10000 Entonces
		Escribir "El lote es un lote rural pequeño"
	SiNo
		Si area_final>10000 Y area_final<=20000 Entonces
			Escribir "El lote es un lote rural medio"
		SiNo
			Escribir "El lote es un lote rural grande"
		FinSi
	FinSi
FinAlgoritmo
