Algoritmo sin_titulo
	Definir contrasena, usuario, contrasena_ingresada, usuario_ingresado Como Caracter
	
	usuario<-"admin"
	contrasena<-"admin123"
	
	Repetir
		Escribir "Ingrese el usuario: "
		Leer usuario_ingresado
		
		Escribir "Ingrese la contraseña: "
		Leer contrasena_ingresada
		Si usuario_ingresado=usuario Y contrasena_ingresada=contrasena Entonces
			Escribir "Ha ingresado correctamente"
		SiNo
			Escribir "Contraseña o usuario incorrecto"
		FinSi
		
	Hasta Que usuario_ingresado=usuario Y contrasena_ingresada=contrasena
	
FinAlgoritmo
