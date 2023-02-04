Algoritmo Problema7
	Escribir "Ingresar el nombre del alumno: "
	Leer estudiante
	Escribir "¿A cuántas horas de clases asistió el alumno?"
	Leer horas_de_clase
	horas <- 90/100*75
	Si horas_de_clase >= horas Entonces
		Escribir ,estudiante " si tiene derecho al examen  de la materia Introducción a la Informática"
	FinSi
	Si horas_de_clase < horas
		Escribir ,estudiante " no tiene derecho al examen  de la materia Introducción a la Informática, "
		Escribir "ya que no tiene el 75% de la asistencia"
	SiNo
		Escribir "No pudo haber asistido tantas horas"
	FinSi

FinAlgoritmo
