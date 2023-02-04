salario = 150000.00
anosN= int(input("Ingrese el año del que quiera saber el salario: "))

for anoN in range(1, anosN):
    print(f"En el año {anoN} su salario era de: {salario} ")
    incremento=(salario/100)*10
    salario = (salario+incremento)

print(f"Al cabo de {anosN} años el sueldo es de: {salario} ")


