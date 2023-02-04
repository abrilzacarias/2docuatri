//Algoritmo para calcular el salario semanal de un trabajador
Algoritmo salarioo
	Escribir "Ingrese horas trabajadas por semana"
	Leer HT;                                                   //ingresa por teclado las horas_trabajadas_semana
	Escribir "Ingresar el salario $/horas";                     //ingresa por teclado el salario $/hora
	Leer SH;
	SalEX es numero
	Si HT>40 Entonces
		salario = SH*40                                           //cálculo que corresponde al salario sin horas extras
		HEX = HT-40                                               //cálculo de la cantidad de horas extras
		SalEX = SH*HEX                                            //cálculo del salario que corresponde a las horas extras
		SalEX = SaLEX *1.5                                        //incremento el 50% al salario extra
		salario = salario+SalEX                                 //suma el salario más el salario extra
	SiNo
		salario=HT*SH
	Fin Si
	Escribir "el salario semanal ganado es: $"," ", Salario,",$",salex, " corresponden a salario extra";
FinAlgoritmo
