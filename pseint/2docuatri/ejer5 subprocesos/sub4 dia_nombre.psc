SubProceso diasemana(dia)
	Segun dia Hacer
		1:
			Escribir "Buen d�a, hoy es Lunes"
		2:
			Escribir "Buen d�a, hoy es Martes"
		3:
			Escribir "Buen d�a, hoy es Mi�rcoles"
		4:
			Escribir "Buen d�a, hoy es Jueves"
		5:
			Escribir "Buen d�a, hoy es Viernes"
		6:
			Escribir "Buen d�a, hoy es S�bado"
		7:
			Escribir "Buen d�a, hoy es Domingo"
		De Otro Modo:
			Escribir "N�mero de d�a ingresado incorrecto"
	Fin Segun
FinSubProceso

SubProceso hola_mundo(nombre)
	Escribir "Hola Mundo soy " , nombre
FinSubProceso

Algoritmo sub1
	definir dia Como Entero
	Definir nombre Como Caracter
	Escribir "Ingrese su nombre: "
	Leer nombre

	Escribir "Ingrese un n�mero del d�a de la semana:"
	leer dia
	
	hola_mundo(nombre)
	diasemana(dia)
FinAlgoritmo
