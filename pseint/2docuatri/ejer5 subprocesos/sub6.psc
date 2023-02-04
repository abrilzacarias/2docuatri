SubProceso validarIngreso(usuario,contrasena)
	Si usuario="admin" Y contrasena="admin123" Entonces
		Escribir "Ha ingresado correctamente."
	SiNo
		Escribir "Usuario o contraseña inválido"
	FinSi
	
FinSubProceso
Algoritmo sin_titulo
	Definir usuario, contrasena Como Caracter
	Definir c Como Entero
	c<-0
	Repetir
		c<-c+1
		Escribir "Ingrese el usuario: "
		Leer usuario
		Escribir "Ingrese la contraseña:"
		Leer contrasena
		validarIngreso(usuario,contrasena)
	Hasta Que usuario="admin" Y contrasena="admin123" O c=3
	
	Si c=3 Entonces
		Escribir "Se han realizado los 3 intentos correspondientes"
	FinSi
	
FinAlgoritmo
