SubProceso orden_nros(nro1,nro2,nro3)
	Si nro1>=nro2 Y nro1>=nro3 Entonces
		Si nro2>=nro3 Entonces
			Escribir nro1, " " , nro2 " ", nro3
		SiNo
			Escribir nro1, " " , nro3 " ", nro2
		FinSi
	SiNo
		Si nro2>=nro1 Y nro2>=nro3 Entonces
			Si nro1>=nro3 Entonces
				Escribir nro2, " " , nro1 " ", nro3
			SiNo
				Escribir nro2, " " , nro3 " ", nro1
			FinSi
		SiNo
			Si nro3>=nro1 Y nro3>=nro2 Entonces
				Si nro1>=nro2 Entonces
					Escribir nro3, " " , nro1 " ", nro2
				SiNo
					Escribir nro3, " " , nro2 " ", nro1
				FinSi
		FinSi
	FinSi
FinSi

FinSubProceso

Algoritmo sin_titulo
	Definir nro1,nro2,nro3 Como Real
	
	Repetir
		Escribir "Ingrese el primer número (Ingrese 0 para salir)"
		Leer nro1
		Si nro1<>0 Entonces
			Escribir "Ingrese el segundo número"
			Leer nro2
			Escribir "Ingrese el tercer número"
			Leer nro3
			
			orden_nros(nro1,nro2,nro3)
		FinSi
	Hasta Que nro1==0
	
	Escribir "Ha salido del programa."
FinAlgoritmo
