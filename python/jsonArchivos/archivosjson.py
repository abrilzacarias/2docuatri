import json
#importar la libreria

contactos = [ #la tupla se establece como una lista con parentesis
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

datos = []

#hace una lectura
for nombre, empleo, email in contactos:
    datos.append({"nombre":nombre, "empleo":empleo, "email":email})

#Se abre el archivo en modo escritura, entre parentesis el nombre del archivo
with open("contactos.json", "w") as jsonfile:
    json.dump(datos, jsonfile)
    #dump guarda en ese archivo el primero parametro pasado

with open("contactos.json") as jsonfile:
    datos = json.load(jsonfile)
    for contacto in datos:
        print(contacto["nombre"], contacto["empleo"], contacto["email"])
