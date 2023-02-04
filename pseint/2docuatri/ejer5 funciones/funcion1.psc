SubProceso edad_personas(persona1,persona2)
	
	Si persona1>persona2 Entonces
		Escribir "La persona 2 es más joven"
	SiNo
		Si persona2>persona1 Entonces
			Escribir "La persona 1 es más joven"
		SiNo
			Escribir "Las personas tienen la misma edad"
		FinSi
	FinSi
FinSubProceso

Algoritmo sin_titulo
	Definir persona1,persona2 Como Entero
	
	Escribir "Ingrese la edad de la primera persona: "
	Leer persona1
	Escribir "Ingrese la edad de la segunda persona: "
	Leer persona2
	edad_personas(persona1,persona2)
	
FinAlgoritmo
