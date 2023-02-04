//Algoritmo que determina el mayor de dos números 'a' y 'b'. Desarrollado por RPC
Algoritmo mayor_que                                                              //proceso mayor_que
	Escribir "algoritmo para calcular cual número de a y b es mayor";              
	Escribir "introduzca el valor de a";                                         //muestra en pantalla la instrucción
	Leer a;                                                                      //ingresa por teclado el valor de 'a'
	Escribir "introduzca el valor de b";
	Leer b;
	a<-a;                                                                  // a=a; si escribieramos a=0, la comparación sería entre ceros (error)
	b<-b;                                                                  // idem al anterior
	Si a>b Entonces                                                        //Condicional Si (If) a>b Entonces que?
		Escribir "el número a="," ",a,"es mayor que b="," ",b;  
	SiNo
		Escribir "el número a="," ",a,"es menor que b="," ",b;
	Fin Si                                                                //Fin de la condicional                                                           
FinAlgoritmo                                                              //Fin del proceso
