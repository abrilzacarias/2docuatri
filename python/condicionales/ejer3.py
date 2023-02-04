alumnos = int(input("Ingrese la cantidad de alumnos: "))
if (alumnos>=100):
    costoAlumno=65
elif (alumnos>=50) & (alumnos<=99):
    costoAlumno=70
elif (alumnos<=49) & (alumnos>=30):
    costoAlumno=95
else:
    pagoAutobus=4000
    costoAlumno=pagoAutobus/alumnos

pagoAutobus=alumnos*costoAlumno
print(f'El pago para la compañía de autobuses con {alumnos} alumnos es de: ${pagoAutobus} ')
print(f'Cada alumno debe pagar por el viaje un total de: ${costoAlumno} ')