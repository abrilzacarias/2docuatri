def averiguarCondicion (dictP):
    for materia, notas in dictP.items():
        promedio = sum(notas)/len(notas)
        if (promedio>=1) and (promedio<=5):
            tipoCondicion = "DESAPROBADO"
        elif (promedio>=6) and (promedio<=7):
            tipoCondicion = "REGULARIZADO"
        elif (promedio>=8) and (promedio<=10):
            tipoCondicion = "PROMOCIONADO"
        print (f"El alumno que cursa {materia}, ha obtenido una promedio de {promedio}, por lo tanto ha {tipoCondicion}")

dictMaterias = {"Algebra": [7, 8, 6, 7], "Introducción": [5, 5, 4, 5],"Programacion": [9, 9, 10, 10]}
averiguarCondicion (dictMaterias)
