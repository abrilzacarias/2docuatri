Proceso Tienda
	//Precondiciones: códigos, precios, descuentos
	Escribir "Ingrese producto (101,102,103): ";
	Leer Codigo;
	//Leer guarda un Escribir como variable
	Escribir "Ingrese cantidad de productos a comprar: ";
	Leer Cantidad;
	Segun Codigo Hacer
	//En Opciones de Segun sólo van números
		101:
			C101 <- 17.5;
			//Se usa < y - para asignar una variable o constante
			Preciof <- C101 * Cantidad;
			Escribir "Precio del producto: " ,C101;
			//Escribir muestra en pantalla y se pone una coma , antes
			//de la variable a mostrar
		102:
			C102 <- 25.0
			Preciof <- C102 * Cantidad;
			Escribir "Precio del producto: " ,C102;
		103:
			C103 <- 15.5
			Preciof <- C103 * Cantidad;
			Escribir "Precio del producto: " ,C103;
		De Otro Modo:
			Escribir "No se encontró el producto"
	Fin Segun
	Escribir "Importe de la compra: " ,Preciof;
	Segun Cantidad Hacer
	//Varios números en una opción se separan por coma
		1,2,3,4,5,6,7,8,9,10:
			Descuento <- 5/100
			PreciocDesc <- (Preciof * Descuento)
		11,12,13,14,15,16,17,18,19,20:
			Descuento <- 7.5/100
			PreciocDesc <- (Preciof * Descuento)
		De Otro Modo:
			Descuento <- 10/100
			PreciocDesc <- (Preciof * Descuento)
	FinSegun
	Escribir "Importe del descuento: " ,REDON(PreciocDesc);
	Escribir "Importe a pagar: " ,Preciof - PreciocDesc;
FinProceso
//4 salidas, precios, importe de la compra, importe del Descuento
//Importe a pagar con descuento
