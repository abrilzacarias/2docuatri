Algoritmo aprobar
	Definir tp1, tp2, parcial, tpi, cal_final, alumnos, cont, promocionados, no_promocionados Como Real
	Definir promedio Como Real
	
	Escribir "¿Cuántos alumnos son?"
	Leer alumnos
	
	cont<-0
	promocionados<-0
	no_promocionados<-0
	
	Repetir
		cont<-cont+1
		Escribir "Ingrese las 4 calificaciones del alumno: "
		Leer tp1, tp2, parcial, tpi
		
		cal_final <- tp1+tp2+parcial+tpi
		promedio <- cal_final/4
		
		Si promedio >= 7.5 Entonces
			//Escribir "Promociona"
			promocionados<-promocionados+1
		Sino 
			//Escribir "No promociona"
			no_promocionados<-no_promocionados+1
		FinSi
	Hasta Que cont=alumnos
	
	Escribir "El número total de alumnos promocionados es de: " promocionados
	Escribir "El número total de alumnos no promocionados es de: " no_promocionados
	
FinAlgoritmo
