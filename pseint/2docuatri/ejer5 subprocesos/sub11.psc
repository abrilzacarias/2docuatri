SubProceso area_triangulo(base,altura)
	Definir areaT Como Real
	areaT<-(base*altura)/2
	Escribir "El �rea del tri�ngulo es de: " , areaT
FinSubProceso

SubProceso area_rectangulo(base,altura)
	Definir areaR Como Real
	areaR<-(base*altura)
	Escribir "El �rea del rect�ngulo es de: " , areaR
FinSubProceso

SubProceso menu()
	Escribir "Seleccione una opci�n:"
	Escribir "1) Calcular �rea de un tri�ngulo"
	Escribir "2) Calcular �rea de un rect�ngulo"
	Escribir "3) Salir"
FinSubProceso
Algoritmo sin_titulo
	Definir base,altura,opc Como Real
	
	Repetir
		menu()
		Leer opc
		Si opc==1 O opc==2 Entonces
			Escribir "Ingrese la base: "
			Leer base
			Escribir "Ingrese la altura: "
			Leer altura
			
			Si opc==1 Entonces
				area_triangulo(base,altura)
			SiNo
				area_rectangulo(base,altura)
			FinSi
		SiNo
			Si opc<>3 Entonces
				Escribir "Ha ingresado una opci�n que no est� en el men�."
			FinSi
		FinSi
	Hasta Que opc=3
	
	Escribir "Ha salido del programa."
	
FinAlgoritmo
