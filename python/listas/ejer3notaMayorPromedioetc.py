notas, notaSuma, notaMenor, notaMayor = 5, 0.0, 0.0, 0.0
listaNotas= []
for nota in range(1,notas+1):
    notaObtenida = float(input(f"Ingrese su nota N° {nota}: "))
    notaSuma+=notaObtenida
    
    listaNotas.append(notaObtenida)

notaMedia=notaSuma/notas
notaMayor=max(listaNotas)
notaMenor=min(listaNotas)
print(f"Las notas son: {listaNotas}")
print(f"""La nota media es de: {notaMedia} 
La nota mayor es de: {notaMayor} 
La nota menor es de: {notaMenor} """)

#.pop borra el último de la lista, y si se le pasa parámetro borra el indicado
