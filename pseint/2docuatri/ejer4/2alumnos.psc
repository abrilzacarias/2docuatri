Algoritmo alumnos_
	Definir costo_alumnos, renta, pago_autobus, renta_c_alumno, alumnos Como Real
	
	Escribir "¿Cuántos alumnos son? "
	Leer alumnos
	
	Si alumnos>=100 Entonces
		costo_alumnos<-650
		pago_autobus<-alumnos*costo_alumnos
		Escribir "El pago para la compañía de autobuses con " , alumnos " alumnos es de: $" , pago_autobus 
		Escribir "Cada alumno debe pagar por el viaje un total de: $" ,costo_alumnos
	SiNo
		Si alumnos>=50 Y alumnos<=99
			costo_alumnos<-700
			pago_autobus<-alumnos*costo_alumnos
			Escribir "El pago para la compañía de autobuses con " , alumnos " alumnos es de: $" , pago_autobus 
			Escribir "Cada alumno debe pagar por el viaje un total de: $" ,costo_alumnos
		SiNo
			Si alumnos<=49 Y alumnos>=30 Entonces
				costo_alumnos<-950
				pago_autobus<-alumnos*costo_alumnos
				Escribir "El pago para la compañía de autobuses con " , alumnos " alumnos es de: $" , pago_autobus 
				Escribir "Cada alumno debe pagar por el viaje un total de: $" ,costo_alumnos
			SiNo
					renta<-300000
					renta_c_alumno<-renta/alumnos
					Escribir "El pago para la compañía de autobuses con " , alumnos " alumnos es de: $" , renta 
					Escribir "Cada alumno debe pagar por el viaje un total de: $" ,redon(renta_c_alumno)
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo
