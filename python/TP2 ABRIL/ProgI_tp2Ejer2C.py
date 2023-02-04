impuestoAc = 0
catCont=3

for c in range(1, catCont+1):
    categoria=int(input(f"Ingrese la categoria de autos: "))
    cant=int(input(f"Ingrese la cantidad de autos de la categoria {c}: "))
    precio=float(input(f"Ingrese el precio de los autos de la categoria {c}: "))
    if categoria==1:
        impuesto=(precio*0.03)
        impTotal=impuesto*cant
    elif categoria==2:
        impuesto=(precio*0.015)
        impTotal=impuesto*cant
    elif categoria==3:
        impuesto=(precio*0.012)
        impTotal=impuesto*cant
    impuestoAc+=impTotal

print(f"El impuesto total que debe abonar es de: ${impuestoAc} ")
#$4207.5 