clase = {}
a=True

while (a == True):
    alumno = input("Nombre del alumno (ok para salir): ")
    if (alumno == "ok"):
        a=False
    else:
        notas=[]
        nota = 1
        while nota > 0:
            nota = int(input("Dame una nota del alumno (negativo para terminar):"))
            if nota > 0:
                notas.append(nota)
    
        clase[alumno]=notas
        #alumno = input("Nombre del alumno (ok para salir): ")

print(clase)

for alumno, notas in clase.items():
    print(f"{alumno} ha sacado de nota media de {(sum(notas)/len(notas))}")