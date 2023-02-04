Algoritmo salario_obreros
	Definir horas, sueldo, horas_extras, horas_sueldo, salarioextra, imp, salariofinal, imp_extra Como Real
	
	Escribir "¿Cuántas horas trabajó el obrero?"
	Leer horas
	Escribir "¿Cuánto es el sueldo por hora?"
	Leer sueldo

	horas_sueldo <- horas*sueldo
	horas_extras <- horas_sueldo*1.5
	imp <- horas_sueldo*(20/100)
	salariofinal <- horas_sueldo-imp
	imp_extra <- horas_extras*(20/100)
	salarioextra <- horas_extras-imp_extra
	
	Si horas <= 35 Entonces
		Si horas_sueldo > 20000 Entonces
			Escribir "Su salario final, con los impuestos aplicados es de: $" , salariofinal
		SiNo
			Escribir "Su salario es de: $" , horas_sueldo
		FinSi
	Sino 
		Si horas_extras > 20000 Entonces
			Escribir "Su salario con horas extras y aplicados los impuestos es de: $" , salarioextra
		Sino 
			Escribir "Su salario es de: $" , horas_extras
		FinSi
	FinSi
FinAlgoritmo
