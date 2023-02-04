Algoritmo aula
	Definir alumnos, banco, bancos_faltantes Como Entero
	Escribir "ingrese la cantidad de alumnos:"
	Leer alumnos
	Escribir "ingrese la cantidad de bancos:"
	Leer banco
	
	Si alumnos > banco
		bancos_faltantes = alumnos-banco
		Escribir "faltan bancos"
		Escribir "bancos faltantes: " bancos_faltantes
	SiNo
		Escribir "bancos suficientes"
	FinSi
	
FinAlgoritmo
