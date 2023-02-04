Algoritmo edadsexo
	Definir edad Como Entero
	Definir sexo Como Caracter
	
	Escribir "Indique su edad:"
	Leer edad
	Escribir "Indique su sexo (f o m):"
	Leer sexo
	

Si sexo = "f" o sexo = "m"
	Si edad >= 16
		Escribir "Usted es mujer y puede votar."
	SiNo
		Escribir "Usted es mujer y no puede votar."
	FinSi
FinSi

Si sexo = "m"
	Si edad >= 16
		Escribir "Usted es hombre y puede votar."
	SiNo
		Escribir "Usted es hombre y no puede votar."	
	FinSi
SiNo
	Escribir "El género ingresado es incorrecto."	
FinSi



	
FinAlgoritmo
