Algoritmo sueldo_empleados
	//se define variable para almacenar cantidad de personas a cargar
	Definir cantidad Como Entero
	
	//se define variable para almacenar el total del sueldo
	Definir acumuladorSueldo Como Entero;
	
	Escribir "Ingrese la cantidad de empleados de la empresa"
	Leer cantidad
	
	// se define vector para almacenar los nombres de los empleados
	Dimension empleados[cantidad]
	
	//se define vector para almacenar los sueldos de los empleados
	Dimension sueldo[cantidad]
	
	//condicion de si la cantidad a cargar es menor a 200
	Si cantidad <= 200 Entonces
		// se empieza a cargar el sueldo y el nombre del empleado
		Para i<-1 Hasta cantidad Con Paso 1 Hacer   
			//se carga el nombre del empleado
			Escribir "Nombre del empleado"   
			Leer empleados[i]
			//se carga el sueldo del empleado
			Escribir "Ingresar sueldo" 
			Leer sueldo[i]
			acumuladorSueldo<-acumuladorSueldo+sueldo[i];
		Fin Para
		
		// se obtiene el promedio
		promedioSueldo<-acumuladorSueldo/cantidad
		Escribir "El promedio del sueldo de los trabajadores es $ ", promedioSueldo
		
		// se declara varaible para almacenar el sueldo minimo
		Definir sueldoMinimo Como Entero;
		//variable para almacenar el indice del empleado con menor sueldo pero mayor al promedio
		Definir indiceEmpleadoMenorSueldo Como Entero;
		//variable para almacenar el indice del sueldo del empleado que tiene menor sueldo pero mayor al promedio
		Definir indiceSueldoMenor Como Entero;
		
		// se inicializan las variables
		sueldoMinimo <- 0
		indiceEmpleadoMenorSueldo <- 0
		indiceSueldoMenor <-0
		//obtener sueldos y nombres mayores al promedio
		Para i<-1 Hasta cantidad Con Paso 1 Hacer
			
			//Escribir sueldoMinimo;
			Si sueldo[i]>promedioSueldo Entonces
				
				//para que se cargue el sueldo por lo menos una vez
				si sueldoMinimo == 0 Entonces
					sueldoMinimo <- sueldo[i]
					indiceEmpleadoMenorSueldo <- i
					indiceSueldoMenor <- i
				FinSi
				
				
				Escribir "El empleado: ", empleados[i], " posee un sueldo: ", sueldo[i], " $", " el cual es mayor al promedio";
				
				//Escribir sueldo[i];
				//Escribir sueldoMinimo
				//Escribir indiceEmpleadoMenorSueldo
				// si el sueldo actual es menor al sueldo minimo guardado se reemplaza el sueldo y el indice de sueldo y del empleado
				si sueldo[i] < sueldoMinimo Entonces
					indiceEmpleadoMenorSueldo <- i
					indiceSueldoMenor <- i
					sueldoMinimo <- sueldo[i]
				FinSi
			FinSi
		FinPara
		//se imprime indice del sueldo y el nombre del empleado con con el sueldo mas bajo pero mayor al promedio
		
		Escribir "El empleado con el menor sueldo pero mayor al promedio es: ", empleados[indiceEmpleadoMenorSueldo], " con un sueldo de: ", sueldo[indiceSueldoMenor]
		
	SiNo
		Escribir "Ingrese una cantidad menor de empleados"
	FinSi
FinAlgoritmo
