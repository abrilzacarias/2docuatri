SubProceso suma(nro1,nro2)
	Definir suma_nros Como Real
	suma_nros<-nro1+nro2
	Escribir suma_nros
FinSubProceso

SubProceso multipl(nro1,nro2)
	Definir multipl_nros Como Real
	multipl_nros<-nro1*nro2
	Escribir multipl_nros
FinSubProceso

SubProceso resta(nro1,nro2)
	Definir resta_nros Como Real
	resta_nros<-nro1-nro2
	Escribir resta_nros
FinSubProceso

SubProceso div(nro1,nro2)
	Si nro1>nro2 Y nro2<>0 Entonces
		Definir div_nros Como Real
		div_nros<-nro1/nro2
		Escribir div_nros
	SiNo
		Escribir"No se puede realizar la división de estos números"
	FinSi
FinSubProceso

SubProceso concat(nro1,nro2)
	Definir nro1_nuevo, nro2_nuevo, concat_nros Como Caracter
	nro1_nuevo<-ConvertirATexto(nro1)
	nro2_nuevo<-ConvertirATexto(nro2)
	concat_nros<-Concatenar(nro1_nuevo,nro2_nuevo)
	Escribir concat_nros
FinSubProceso

SubProceso menu_mostrar()
	Escribir "Seleccione una opción"
	Escribir "1)Sumar 2)Multiplicar 3)Dividir 4)Restar 5)Concatenar 6)Salir"
FinSubProceso

Algoritmo sin_titulo
	Definir opc Como Entero
	Definir nro1, nro2 Como Real
	opc<-0
	Mientras opc<>6 Hacer
		menu_mostrar()
		Leer opc
		Si opc<6 Entonces
			Escribir "Ingrese el primer número:"
			Leer nro1
			Escribir "Ingrese el segundo número:"
			Leer nro2
		FinSi
		
		Segun opc Hacer
			1:
				suma(nro1,nro2)
			2:
				multipl(nro1,nro2)
			3:
				div(nro1,nro2)
			4:
				resta(nro1,nro2)
			5:
				concat(nro1,nro2)
			6:
				opc<-6
			De Otro Modo:
				Escribir "ERROR: Ingrese un número de la lista."
		Fin Segun
	FinMientras
	
	Escribir "Ha salido del programa."
FinAlgoritmo
