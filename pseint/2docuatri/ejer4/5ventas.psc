Algoritmo hnos_sbaderdella
	Definir nro_ventas, c, precio, contador1, contador2, contador3 Como Entero
	Definir monto1, monto2, monto3, monto_total Como Real
	
	Escribir "Ingrese la cantidad de ventas que desea realizar: "
	Leer nro_ventas
	c<-0
	contador1<-0
	monto1<-0
	contador2<-0
	monto2<-0
	contador3<-0
	monto3<-0
	
	Repetir
		Escribir "Ingrese el precio de los " , nro_ventas " productos que desea comprar:"
		Leer precio
		c<-c+1
		Si precio<=500 Entonces
			contador1<-contador1+1
			monto1<-monto1+precio
		SiNo
			Si precio>500 Y precio<=1000 Entonces
				contador2<-contador2+1
				monto2<-monto2+precio
			SiNo
				contador3<-contador3+1
				monto3<-monto3+precio
			FinSi
		FinSi
	Hasta Que c=nro_ventas
	
	Escribir "Las ventas con un costo menor a 500 fueron: " contador1 " y su monto fue de: $" monto1
	Escribir "Las ventas con un costo entre 500 y 1000 fueron: " contador2 " y su monto fue de: $" monto2
	Escribir "Las ventas con un costo mayor a 1000 fueron: " contador3 " y su monto fue de: $" monto3
	monto_total<-monto1+monto2+monto3
	Escribir "Las ventas totales fueron: " ,nro_ventas " con un monto de: $" , monto_total
FinAlgoritmo
