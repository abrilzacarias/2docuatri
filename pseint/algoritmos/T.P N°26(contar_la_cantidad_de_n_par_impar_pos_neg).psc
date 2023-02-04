Algoritmo contar_la_cantidad_de_n_par_impar_pos_neg
	Definir par, impar, pos, neg, x, n, num Como Real;
	par<-0
	impar<-0
    pos<-0
	neg<-0
	Para x<-1 Hasta 6 Hacer
		Leer n
		Si n%2= 0  Entonces
			par = par+1
		SiNo
			impar = impar+1
		Fin Si
		Si n>0 Entonces
			pos=pos+1
		SiNo
			neg=neg+1
		Fin Si
	Fin Para
	Escribir "Hay: ",par," números pares";
	Escribir "Hay: ",impar," números impares";
	Escribir "Hay: ",pos, "números positivos";
	Escribir "Hay: ",neg, "números negativos";
FinAlgoritmo

