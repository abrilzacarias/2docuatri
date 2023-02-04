Algoritmo Prog1_TP1_EJER2
	Definir menu, personas, plato, presupuesto Como Real
	
	
	Escribir "Ingrese la cantidad de personas" 
	Leer personas
	
	Escribir "Seleccione el menú: 1) Económico 2) Ejecutivo"
	Leer menu
	
	Si menu==1 Entonces
		Si personas>150 Y personas<=300 Entonces
			plato<-200
		SiNo
			Si personas>300
				plato<-150
			SiNo
				plato<-290
			FinSi
		FinSi
	SiNo
		Si menu==2
			plato<-500
			Si personas>150 Y personas<=300
				plato<-420
			SiNo
				Si personas>=300 Entonces
					plato<-350
				FinSi
			FinSi
		FinSi
		Si menu<>1 Y menu<>2 Entonces
			plato<-0
			Escribir "El menú ingresado es incorrecto"
		FinSi
	FinSi
	
	Si menu==1 O menu==2 Entonces
		presupuesto<-plato*personas
		Escribir "El presupuesto para contratar a la empresa con el menú " , menu " y la cantidad de " , personas " personas es de: " , presupuesto
	FinSi

FinAlgoritmo
