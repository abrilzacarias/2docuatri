SubProceso menuGrupoEdad()
	
	Escribir "Ingrese la edad del paciente:"
	Escribir "1) RN: Nacimiento - 6 semanas"
	Escribir "2) Infante: 7 semanas - 1 año"
	Escribir "3) Lactante mayor: 1 - 2 años"
	Escribir "4) Pre-escolar: 2 - 6 años"
	Escribir "5) Escolar: 6 - 13 años"
	Escribir "6) Adolescente: 13 - 16 años"
	Escribir "7) Adulto: 16 años y más"
FinSubProceso

SubProceso presionArterial(opcionGrupoEdad)
	Segun opcionGrupoEdad Hacer
		1:
			Si (presionSistolica>70 Y presionSistolica<100) Y (presionDiastolica>50 y presionDiastolica<68) Entonces
				Escribir "La presión de la persona es normal"
			SiNo
				Escribir "La presión de la persona es anormal"
			FinSi
		2:
			Si (presionSistolica>84 Y presionSistolica<106) Y (presionDiastolica>56 y presionDiastolica<70) Entonces
				Escribir "La presión de la persona es normal"
			SiNo
				Escribir "La presión de la persona es anormal"
			FinSi
		3:
			Si (presionSistolica>98 Y presionSistolica<106) Y (presionDiastolica>58 y presionDiastolica<70) Entonces
				Escribir "La presión de la persona es normal"
			SiNo
				Escribir "La presión de la persona es anormal"
			FinSi
		4:
			Si (presionSistolica>99 Y presionSistolica<112) Y (presionDiastolica>64 y presionDiastolica<70) Entonces
				Escribir "La presión de la persona es normal"
			SiNo
				Escribir "La presión de la persona es anormal"
			FinSi
		5:
			Si (presionSistolica>104 Y presionSistolica<124) Y (presionDiastolica>64 y presionDiastolica<86) Entonces
				Escribir "La presión de la persona es normal"
			SiNo
				Escribir "La presión de la persona es anormal"
				hipoHipertension(presionDiastolica,presionSistolica)
				FinSi
		6: 
			Si (presionSistolica>118 Y presionSistolica<132) Y (presionDiastolica>70 y presionDiastolica<82) Entonces
				Escribir "La presión de la persona es normal"
			SiNo
				Escribir "La presión de la persona es anormal"
				hipoHipertension(presionDiastolica,presionSistolica)
			FinSi
		7:
			Si (presionSistolica>110 Y presionSistolica<140) Y (presionDiastolica>70 y presionDiastolica<90) Entonces
				Escribir "La presión de la persona es normal"
			SiNo
				Escribir "La presión de la persona es anormal"
				hipoHipertension(presionDiastolica,presionSistolica)
			FinSi
	Fin Segun
FinSubProceso 

SubProceso hipoHipertension(presionDiastolica,presionSistolica)
	Si presionSistolica<100 Y presionDiastolica<60 Entonces
		Escribir "Y el paciente presenta hipotensión"
	SiNo
		Si presionSistolica>140 Y presionDiastolica>90 Entonces
			Escribir "El paciente presenta hipertensión"
		FinSi
	FinSi
FinSubProceso

Algoritmo sin_titulo
	Definir opcionGrupoEdad Como Entero
 
	 menuGrupoEdad()
	 Leer opcionGrupoEdad
	 
	 Definir presionDiastolica, presionSistolica Como Real
	 
	 Escribir "Ingrese la presión sistólica:"
	 Leer presionSistolica
	 Escribir "Ingrese la presión diastólica:"
	 Leer presionDiastolica
FinAlgoritmo