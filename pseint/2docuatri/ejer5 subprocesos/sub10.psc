SubProceso tres_n(nro1,nro2,nro3)
	Definir val_final Como Real
	
	val_final<-nro1*nro2
	Escribir "El resultado de " ,nro1 " incrementado su valor en " ,nro2 " es de: " , val_final
	
FinSubProceso

Algoritmo sin_titulo
	Definir nro1,nro2,nro3 Como Real
	
	Escribir "Ingrese el primer número"
	Leer nro1
	Escribir "Ingrese el segundo número"
	Leer nro2
	Escribir "Ingrese el tercer número"
	Leer nro3
	
	tres_n(nro1,nro2,nro3)
FinAlgoritmo
