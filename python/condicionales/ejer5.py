nroCita = int(input("Ingrese el número de cita: "))

citas123 = 150.0
citas45 = 360.0
citas678 = 120.0
citasSig = 50.0

if nroCita<=3:
    costoCita = citas123
    tratamiento = citas123*nroCita
elif nroCita<=5:
    costoCita =citas45
    restaCita = (nroCita-3)
    tratamiento = 450+(restaCita*citas45)
elif nroCita<=8:
    costoCita=citas678
    restaCita = (nroCita-5)
    tratamiento = 1170+(restaCita*citas678)
else:
    costoCita=citasSig
    restaCita = (nroCita-8)
    tratamiento = 1530+(restaCita*citasSig)

print(f'El paciente pagará por la cita ${costoCita} y pagará por el tratamiento un total de ${tratamiento} ')