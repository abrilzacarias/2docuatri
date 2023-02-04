

lista = [{'Nombre':'NUCLEO', 'Id':20, 'Tipo':'MP', 'Fuente':2},{'Nombre':'PVC de mexichem', 'Id':19, 'Tipo':'MP', 'Fuente':2}]

for elem in lista:      #accedemos a cada elemento de la lista (en este caso cada elemento es un dictionario)
    for k,v in elem.items():        #acedemos a cada llave(k), valor(v) de cada diccionario
        print(k, v)