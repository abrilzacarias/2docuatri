Proceso Calculadora_De_Edad
	Definir DiaActual como numero;
	Definir MesActual como numero;
	Definir AnioActual como numero;
	Definir DiaNac como numero;
	Definir MesNac como numero;
	Definir AnioNac como numero;
	Definir Edad como numero;
	Esmayordeedad es logico
	
	
	DiaActual = 02;
	MesActual = 08;
	AnioActual = 2018;
	
	Escribir "ingresar Dia, Fecha y Año de Nacimiento ";
	leer DiaNac;
	leer MesNac;
	leer AnioNac;
	
	Edad = AnioActual - AnioNac
	
	Si MesActual < MesNac entonces
		edad = AnioActual - AnioNac -1
	FinSi
	Si MesActual = MesNac 
		si DiaActual < diaNac Entonces
			edad = AnioActual - AnioNac -1
		FinSi
	FinSi
FinProceso
