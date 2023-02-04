Algoritmo aprobar
	Definir cal1, cal2, cal3, cal4, cal5, cal_final Como Entero
	Definir promedio Como Real
	
	Escribir "Ingrese las 5 calificaciones: "
	Leer cal1, cal2, cal3, cal4, cal5
	
	cal_final <- cal1+cal2+cal3+cal4+cal5
	promedio <- cal_final/5
	
	Si promedio <= 13 Entonces
		Escribir "Aprueba"
	Sino 
		Escribir "Reprueba"
	FinSi
FinAlgoritmo
