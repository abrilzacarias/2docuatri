SubProceso nros(nro1,nro2)
	Si nro1>nro2 Entonces
		Escribir "Entre " , nro1 " y " , nro2 " el mayor es: " , nro1
	SiNo
		Si nro2>nro1 Entonces
			Escribir "Entre " , nro1 " y " , nro2 " el mayor es: " , nro2
		SiNo
			Escribir "Los n�meros ingresados son iguales."
		FinSi
	FinSi
	
FinSubProceso
Algoritmo sin_titulo
	Definir nro1,nro2 Como Entero
	
	Escribir "Ingrese el primer n�mero:"
	Leer nro1
	Escribir "Ingrese el segundo n�mero:"
	Leer nro2
	
	nros(nro1,nro2)
	
FinAlgoritmo