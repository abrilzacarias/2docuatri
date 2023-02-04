SubProceso nros_iguales(nro1,nro2,nro3)
	Si nro1==nro2 Y nro1==nro3 Entonces
		Escribir "Los tres números son iguales."
	SiNo
		Si nro1==nro2 O nro1==nro3 O nro2==nro3 Entonces
			Escribir "Hay dos números iguales."
		SiNo
			Escribir "Los tres números son distintos."
		FinSi
	FinSi
FinSubProceso
Algoritmo sin_titulo
	Definir nro1,nro2,nro3 Como Real
	
	Escribir "Ingrese el primer número:"
	Leer nro1
	Escribir "Ingrese el segundo número:"
	Leer nro2
	Escribir "Ingrese el tercer número:"
	Leer nro3
	nros_iguales(nro1,nro2,nro3)
FinAlgoritmo
