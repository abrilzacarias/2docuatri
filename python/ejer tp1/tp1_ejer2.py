personas = int(input("Ingrese la cantidad de personas: "))
menu= int(input("Seleccione el menú: 1) Económico 2) Ejecutivo: "))

plato = 0
if menu==1:
    if (personas>150) & (personas<=300):
        plato = 200
    elif (personas>300):
        plato=150
    else:
        plato=290
elif menu==2:
    plato=500
    if ((personas>150) & (personas<=300)):
        plato=420
    elif (personas>=300):
        plato=350

if (menu!=1) & (menu!=2):
    plato=0
    print("El menú ingresado es incorrecto")
else: 
    presupuesto=plato*personas
    print(f"El presupuesto para contratar a la empresa con el menú {menu} y la cantidad de {personas} personas es de: {presupuesto} ")
