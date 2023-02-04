Algoritmo bancosalumnos
	Definir bancos, alumnos, bancos_faltantes Como Entero

	Escribir "¿Cuántos bancos hay?"
	Leer bancos
	Escribir "¿Cuántos alumnos hay?"
	Leer alumnos
	Si bancos >= alumnos Entonces
		Escribir "Alcanza la cantidad de bancos para todos los alumnos"
	SiNo
		bancos_faltantes <- alumnos - bancos
		Escribir "No alcanza la cantidad de bancos para los alumnos, faltan " , bancos_faltantes
		
	FinSi
	
FinAlgoritmo
