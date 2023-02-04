Algoritmo sin_titulo
	Definir resta_citas, tratamiento, costo, monto_obra_social, nro_cita, obra_social, tres_citas, citas45, citas678, citas9_, citas, precio_finalc_obra Como Entero
	
	Escribir "Ingrese el número de su cita: "
	Leer nro_cita
	
	Escribir "¿Usted cuenta con obra social?: 1: SI | 2: NO"
	Leer obra_social
	
	tres_citas<-2000
	citas45<-1500
	citas678<-1000
	citas9_<-500
	citas<-0
	
	Si nro_cita<=3
		costo<-tres_citas
		tratamiento<-tres_citas*nro_cita
	SiNo	
		Si nro_cita<=5
			costo<-citas45
			resta_citas<-(nro_cita-3)//1-2
			tratamiento<-6000+resta_citas*citas45
		SiNo
			Si nro_cita<=8 Entonces
				costo<-citas678
				resta_citas<-(nro_cita-5)//1,2,3
				tratamiento<-9000+resta_citas*citas678
			SiNo
				costo<-citas9_
				resta_citas<-(nro_cita-8)
				tratamiento<-12000+resta_citas*citas9_
			FinSi
		FinSi
	FinSi
	
	monto_obra_social<-1000
	Segun obra_social Hacer
		1:
			Escribir "El costo de la cita es de: $", costo
			Escribir "Se ha gastado en el tratamiento un total de: $" , tratamiento
		2:
			costo<-costo+monto_obra_social
			precio_finalc_obra<-tratamiento+monto_obra_social*nro_cita
			Escribir "El costo de la cita es de: $", costo " con un recargo de: $" monto_obra_social
			Escribir "Se ha gastado en el tratamiento un total de: $" , precio_finalc_obra
	Fin Segun
FinAlgoritmo
