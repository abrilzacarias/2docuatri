Funcion promedio_final<-promedio(tp1,tp2,parcial,tpi)
	Definir suma_notas,promedio_final Como Real
	suma_notas<-tp1+tp2+parcial+tpi
	promedio_final<-suma_notas/4
FinFuncion

Funcion promocion<-calculo_promocionar(cuota,biblioteca,asistencia,promedio_final)
	Si (cuota=1) Y (biblioteca=1) Y (asistencia=1) Y (promedio_final>=7.5) Entonces
		Escribir "El alumno ha promocionado"
	SiNo
		Escribir "El alumno no ha promocionado"
	FinSi
FinFuncion

Algoritmo sin_titulo
	Definir cuota, biblioteca, asistencia, tp1,tp2,parcial,tpi Como Real
	
	Escribir "Ingrese: 1) Si se encuentra al día con el pago de la matrícula y cuotas o 2) Caso contrario."
	Leer cuota
	Escribir "Ingrese: 1) Si no debe libros ni posee multas en la biblioteca o 2) Caso contrario."
	Leer biblioteca
	Escribir "Ingrese: 1) Si cumple con el 75% de asistencia o 2) Caso contrario."
	Leer asistencia
	Escribir "Ingrese su nota en el Trabajo Practico Evaluativo Nº1:"
	leer tp1
	Escribir "Ingrese su nota en el Trabajo Practico Evaluativo Nº2:"
	leer tp2
	Escribir "Ingrese su nota en el Parcial:"
	leer parcial
	Escribir "Ingrese su nota en el Trabajo Practico Integrador:"
	leer tpi
	
	Escribir calculo_promocionar(cuota,biblioteca,asistencia,promedio(tp1,tp2,parcial,tpi))
FinAlgoritmo