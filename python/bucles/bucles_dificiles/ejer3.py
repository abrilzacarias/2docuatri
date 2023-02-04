nro=1.0
promedioNros, i, sumaNros= 0.0, 0, 0.0
while nro!=0:
    nro=float(input("Ingrese números para saber su promedio: "))
    i=i+1
    sumaNros=(sumaNros+nro)

    #if nro!=0:
        #print(sumaNros)
        #print(promedioNros)

promedioNros=sumaNros/(i-1)
print(f"Ha salido del programa y el promedio final es de {promedioNros} .")