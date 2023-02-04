potencia3 = input("Ingrese un número positivo para saber si es potencia de 3: ")
i = 0

for i in range(400):
    potencia = 3**i
    i+1
    if potencia == int(potencia3):
        print(potencia3 + " es potencia de 3")
        break
    elif potencia != int(potencia3) and potencia > 10000:
        print(potencia3 + " NO es potencia de 3")
        break
