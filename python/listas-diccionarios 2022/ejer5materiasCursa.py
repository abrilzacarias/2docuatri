dicCursado = {'Programación': ["brenda", "paula"], 'Ingles': ["paula", "marianela"], 'Matemática': ["marianela"], 'Portugues': ["abril"]}
def matriculados(pNombre):
    for k, v in dicCursado.items():
        if pNombre in v:
            print(f"El alumno {pNombre} está matriculado en: {k} ")
        else:
            print (f"El alumno {pNombre} no cursa ninguna materia")
            


nombre = input("Ingrese el nombre del alumno: ")
matriculados(nombre)
