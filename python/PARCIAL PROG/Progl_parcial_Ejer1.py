import random

def fnAltaNuevoAlumno(Pnombre):
    idAlumno = random.randint(1,200)
    print(idAlumno)
    edad = int(input("Ingrese su edad: "))
    while (edad<0) and (edad>90):
        edad = int(input("Ingrese su edad: "))
        print("No puede registrarse esa edad, vuelva a intentar")
    diccMaterias = {1: {}, 2: {}, 3: {} }
    for i in range(1,4):
        nombreMateria = input("Ingrese el nombre de la materia: ")
        nota = input(f"Ingrese la nota de la materia {nombreMateria} : ")
        diccMaterias[i] = {"idMateria": i, "nombreMateria": nombreMateria, "Nota": nota}
    listadoAlumnos.append({"idAlumno": idAlumno, "nombre": Pnombre, "edad": edad, "notas":diccMaterias})

def fnAltaAlumnos():
    salir=True
    while salir == True:
        nombre = input("Ingrese su nombre: ")
        fnAltaNuevoAlumno(nombre)
        nuevoAlum= int(input("¿Desea ingresar un nuevo alumno? 1)NO 2)SI: "))
        if nuevoAlum==1:
            salir=False

#listadoAlumnos.append({"idAlumno": idAlumno, "nombre": Pnombre, "edad": edad, "notas":diccMaterias})
def fnDatosAlumnoPorID(pIDAlumno):
    for unAlumno in listadoAlumnos:
        for k, v in unAlumno.items():
            if v == pIDAlumno:
                print(unAlumno["idAlumno"], unAlumno["nombre"], unAlumno["edad"])
                break
            else:
                print("No se encuentra esta ID")

def fnMateriasAlumnoPorID(pIDAlumno):
    for unAlumno in listadoAlumnos:
        for k,v in unAlumno.items():
            if k == "notas":
                print(v)

def fnAlumnosPorID(pIDAlumno):
    for unAlumno in listadoAlumnos:
        for k,v in unAlumno.items():
            print(k,v)


def fnMenuSistema():
    print("""
    1- Alta de Alumnos.
    2- Consulta por Alumno.
    3- Listado de Notas.
    4- Listado de Aprobados.
    5- Salir""")

listadoAlumnos = []
c=0
salida=True
while salida == True:
    fnMenuSistema()
    opcion = int(input("Ingrese una opción"))
    if opcion==1:
        fnAltaAlumnos()
    elif opcion==2:
        idAlumno = int(input("Ingrese el ID del alumno: "))
        fnDatosAlumnoPorID(idAlumno)
    elif opcion==3:
        idAlumno = int(input("Ingrese el ID del alumno: "))
        fnMateriasAlumnoPorID(idAlumno)
    elif opcion==4:
        pass
    elif opcion==5:
        salida=False
    else:
        print("Ingrese una opción correcta")
        