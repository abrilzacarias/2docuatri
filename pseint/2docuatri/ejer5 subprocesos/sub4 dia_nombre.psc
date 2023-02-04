SubProceso diasemana(dia)
	Segun dia Hacer
		1:
			Escribir "Buen día, hoy es Lunes"
		2:
			Escribir "Buen día, hoy es Martes"
		3:
			Escribir "Buen día, hoy es Miércoles"
		4:
			Escribir "Buen día, hoy es Jueves"
		5:
			Escribir "Buen día, hoy es Viernes"
		6:
			Escribir "Buen día, hoy es Sábado"
		7:
			Escribir "Buen día, hoy es Domingo"
		De Otro Modo:
			Escribir "Número de día ingresado incorrecto"
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

	Escribir "Ingrese un número del día de la semana:"
	leer dia
	
	hola_mundo(nombre)
	diasemana(dia)
FinAlgoritmo
