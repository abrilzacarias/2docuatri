SubProceso diasemana(dia)
	Segun dia Hacer
	1:
		Escribir "Lunes"
	2:
		Escribir "Martes"
	3:
		Escribir "Mi�rcoles"
	4:
		Escribir "Jueves"
	5:
		Escribir "Viernes"
	6:
		Escribir "S�bado"
	7:
		Escribir "Domingo"
	De Otro Modo:
		Escribir "N�mero de d�a ingresado incorrecto"
Fin Segun
FinSubProceso
Algoritmo sub1
	definir dia Como Entero
	Escribir "Ingrese un n�mero del d�a de la semana:"
	leer dia
	diasemana(dia)
FinAlgoritmo
