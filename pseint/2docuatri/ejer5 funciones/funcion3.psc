SubProceso nros_iguales(nro1,nro2,nro3)
	Si nro1==nro2 Y nro1==nro3 Entonces
		Escribir "Los tres n�meros son iguales."
	SiNo
		Si nro1==nro2 O nro1==nro3 O nro2==nro3 Entonces
			Escribir "Hay dos n�meros iguales."
		SiNo
			Escribir "Los tres n�meros son distintos."
		FinSi
	FinSi
FinSubProceso
Algoritmo sin_titulo
	Definir nro1,nro2,nro3 Como Real
	
	Escribir "Ingrese el primer n�mero:"
	Leer nro1
	Escribir "Ingrese el segundo n�mero:"
	Leer nro2
	Escribir "Ingrese el tercer n�mero:"
	Leer nro3
	nros_iguales(nro1,nro2,nro3)
FinAlgoritmo
