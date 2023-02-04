Algoritmo SalariosxMesxPersona "Salarios por persona por mes"
   Dimension Empleados[10]
   Dimension SalarioEmp[10]
   Dimension HT[10]//Horas trabajadas por empleado
   Dimension ACSalario[10]//Acumulador que guarda el total de los salarios por empleado
   Escribir "Ingresar Nombre del Empleado y su salario"
   STxMes es numero //Acumulador que guarda el total de los salarios de los empleados por mes
para i = 1 hasta 3
	Escribir  "Nombre:"
	leer Empleados[i]//Se ingresa en un vector los nombres de los empleados
	Escribir  "Horas Trabajadas por día:"
	Leer HT[i] //Se ingresa en un vector las horas que trabaja un empleado 
	Escribir  "Salario por Hora:"
	leer SalarioEmp[i] // Se ingresa en un vector el monto de los salarios por empleados, ya que algunos ganan mas que otros
	ACSalario[i] = ACSalario[i] + SalarioEmp[i]	* HT[i]*26 // Multiplico el acumulador general por la cantidad de dias (26 porque los domingos no trabaja)	
	STxMes = STxMes+ACSalario[i]
FinPara
   Escribir "Salario total mensual es: $", STxMes
   i = 0
para i = 1 hasta 3
	escribir "El salario de: ", empleados[i], " en un mes es de: $", ACSalario[i], ". Trabajando: ", ht[i], "hs por día."
FinPara
FinAlgoritmo