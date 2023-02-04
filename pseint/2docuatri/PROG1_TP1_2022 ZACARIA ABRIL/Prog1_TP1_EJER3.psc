Algoritmo Prog1_TP1_EJER3
	Definir km_recorridos, gasto, recaudado, dias Como Real
	Definir acumulador_gasto, acumulador_km, acumulador_recaudado Como Real
	
	dias<-0
	acumulador_gasto<-0
	acumulador_km<-0
	acumulador_recaudado<-0
	
	Repetir
		
		Escribir "Ingrese la cantidad de kilómetros recorridos: "
		Leer km_recorridos
		acumulador_km<-acumulador_km+km_recorridos
		
		Si km_recorridos<>0 Entonces
			Escribir "Ingrese el gasto en combustible:"
			Leer gasto
			acumulador_gasto<-acumulador_gasto+gasto
			
			Escribir "Ingrese el total recaudado: " 
			Leer recaudado
			acumulador_recaudado<-acumulador_recaudado+recaudado
			dias<-dias+1
		FinSi
		
	Hasta Que km_recorridos==0
	
	Escribir "Usted ha realizado un total de: " , dias " días"
	Escribir "El total de kilómetros recorridos es de: " acumulador_km " km"
	Escribir "El promedio de kilómetros es de: " acumulador_km/dias " km"
	Escribir "eL Total del costo del combustible es de: " acumulador_gasto " pesos"
	Escribir "El total recaudado es de: ", acumulador_recaudado " pesos"
	
	Si acumulador_recaudado>acumulador_gasto Entonces
		Escribir "Resultado positivo (beneficio)" 
	SiNo
		Si acumulador_recaudado<acumulador_gasto Entonces
			Escribir "Resultado negativo (pérdida)"
		SiNo
			Escribir "Resultados igual a equilibrio (ni pérdida ni beneficios)"
	FinSi
FinSi

FinAlgoritmo
