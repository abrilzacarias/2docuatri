"""Escriba una función que reciba como parámetros un diccionario con las materias y las notas
obtenidas por un alumno y las clasifique en desaprobada, regularizada y promocionada, teniendo en cuenta
los siguientes criterios según su prom:
● 1-5: Desaprobada.
● 6-7: Regularizada.
● 8-10: Promocionada."""

dictMaterias = {"Matematica": [9,10,10,7], "Programación": [7,6,6,8], "Inglés": [5,5,4,6], "Arquitectura": [6,6,7,7]}

def promMaterias(pDict):
    for k,v in dictMaterias.items():
        #se suman los valores de cada llave, y estas se dividen por el largo (4)
        prom = sum(v)/len(v)
        if (prom>=1) & (prom<6):
            con = "Desaprobado"
        elif (prom>=6) & (prom<8):
            con = "Regularizado"
        elif (prom>=8) & (prom<=10):
            con = "Promocionado"
        print (f"El alumno que cursa {k}, ha obtenido un promedio de {prom}, por lo tanto ha {con}")

promMaterias(dictMaterias)
