SubProceso diasemana(dia)
	Segun dia Hacer
	1:
		Escribir "Lunes"
	2:
		Escribir "Martes"
	3:
		Escribir "Miércoles"
	4:
		Escribir "Jueves"
	5:
		Escribir "Viernes"
	6:
		Escribir "Sábado"
	7:
		Escribir "Domingo"
	De Otro Modo:
		Escribir "Número de día ingresado incorrecto"
Fin Segun
FinSubProceso
Algoritmo sub1
	definir dia Como Entero
	Escribir "Ingrese un número del día de la semana:"
	leer dia
	diasemana(dia)
FinAlgoritmo
