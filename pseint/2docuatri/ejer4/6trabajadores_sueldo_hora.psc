Algoritmo sin_titulo
	Definir trabajadores, dias_trabajados, horas_trabajadas, sueldo_hora, total_empleados, sueldo_dia, sueldo_semanal, cont, nro_trabajador Como Real
	
	Escribir "¿Cuántos trabajadores son?"
	Leer trabajadores
	
	Escribir "Ingrese el sueldo por hora"
	Leer sueldo_hora
	
	cont<-0
	total_empleados<-0
	Repetir
		Escribir "Ingrese la cantidad de días trabajados por el empleado"
		Leer dias_trabajados
		
		Escribir "Ingrese la cantidad de horas trabajadas cada día por los empleado"
		Leer horas_trabajadas
		
		sueldo_dia<-sueldo_hora*horas_trabajadas
		sueldo_semanal<-sueldo_dia*dias_trabajados
		
		Escribir "El sueldo semanal del empleado es de: $" , sueldo_semanal
		cont<-cont+1
		total_empleados<-total_empleados+sueldo_semanal
	Hasta Que cont=trabajadores
	

	Escribir "La empresa pagó a los " , trabajadores " empleados un total de: $" , total_empleados " por esa semana."
	
FinAlgoritmo
