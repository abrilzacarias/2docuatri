alumnos= [{"idAlumno": 12, "nombre": "abril", "edad": 17, "notas":{1: 1, 2: 2, 3: 3}}]

def fnDatosAlumnoPorID(pIDAlumno):
    for unAlumno in alumnos:
        for k, v in unAlumno.items():
            
            if v == pIDAlumno:
                print(unAlumno["idAlumno"])
                print(unAlumno["nombre"])
                print(unAlumno["edad"])
                break
            else:
                print("No se encuentra esta ID")

id=int(input("ingrese id: "))
fnDatosAlumnoPorID(id)
