Algoritmo sueldo_empleados
	Definir cantidad Como Entero                                                 //PRECONDICIONES:
	Definir acumuladorSueldo Como Entero;                                        //Nombre de los trabajadores.
	Escribir "Ingrese la cantidad de empleados de la empresa"                     //Ingreso mensual de los trabajadores.
	Leer cantidad
	Dimension empleados[cantidad]
	Dimension sueldo[cantidad]
	Si cantidad <= 200 Entonces
		Para i<-1 Hasta cantidad Con Paso 1 Hacer   
			Escribir "Nombre del empleado"   
			Leer empleados[i]
			Escribir "Ingresar sueldo" 
			Leer sueldo[i]
			acumuladorSueldo<-acumuladorSueldo+sueldo[i];
		Fin Para
		promedioSueldo<-acumuladorSueldo/cantidad
		Escribir "El promedio del sueldo de los trabajadores es $", promedioSueldo
		Definir sueldoMinimo Como Entero;
		Definir indiceEmpleadoMenorSueldo Como Entero;
		Definir indiceSueldoMenor Como Entero;
		sueldoMinimo <- 0
		indiceEmpleadoMenorSueldo <- 0
		indiceSueldoMenor <-0
		Para i<-1 Hasta cantidad Con Paso 1 Hacer
			Si sueldo[i]>promedioSueldo Entonces
				Si sueldoMinimo == 0 Entonces
					sueldoMinimo <- sueldo[i]
					indiceEmpleadoMenorSueldo <- i
					indiceSueldoMenor <- i
				FinSi
				Escribir "El empleado: ", empleados[i], " posee un sueldo de $", sueldo[i]," el cual es mayor al promedio";
				Si sueldo[i] < sueldoMinimo Entonces                                      
					indiceEmpleadoMenorSueldo <- i
					indiceSueldoMenor <- i
					sueldoMinimo <- sueldo[i]
				FinSi
			FinSi
		FinPara
		//Escribir indiceEmpleadoMenorSueldo
		//Escribir indiceSueldoMenor
		Escribir "El empleado con el menor sueldo, pero mayor al promedio es ", empleados[indiceEmpleadoMenorSueldo], " con un salario de $", sueldo[indiceSueldoMenor]
	SiNo
		Escribir "Ingrese una cantidad menor de empleados"
	FinSi
	//POSTCONDICIONES
	//Mostrar los ingresos de los trabajadores que sean mayores al promedio con sus nombres.
	//Mostrar el mínimo ingreso (entre los trabajadores, en los cuales su salario sea mayor al promedio) 
	//con el respectivo nombre del trabajador.
FinAlgoritmo