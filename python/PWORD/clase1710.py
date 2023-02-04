# Cuando hablo de parametros tengo que mirar la definicion

#El entero no es iterable, pero si pasamos un numero en forma de textose puede recorrer letra a letar

# CLASE LISTAS 17/10
# a veces en vez de tener un dato, tengo un listado no conocida de elementos

#Accedo a un elemento de la lista a traves de una lista (con la posicion del elemento). 
# Lunes, Mar, M, J, V, S, D = 1, 2, 3, 4, 5, 6, 7
#PERO EN PROGRAAMACION LE INDICE COMIENZA EN 0 !!!!!!
#L, M, M, J, V, S, D= 0, 1, 2, 3, 4, 5, 6

#Tengo 2 opciones para definir una lista, 1 es por palabra reservada

#listaSemana = list()
#print(listaSemana)
# aca cree una lista vacia

#la otra forma es
listaSemana = ["Lunes", "Martes", "Miercoles"]
print(listaSemana)

# a la lista puedo agregarle mas datos 
listaSemana.append("Viernes")
print(listaSemana)
#append agrega un elemento a la lista

# Accedo al elemento a traves del indice
print(f"Dia {listaSemana[0]}")
#Accedo al primer elemento con el indice  0 

#Si quiero mas de un elemento:
print(f"Dia {listaSemana[0:2]}")


#PARA MODIFICAR
listaSemana[0] = "Domingo"
print(listaSemana)

#Si quiero borrar
listaSemana.pop()
print(listaSemana)
#SI NO LE PASO EL INDICE, ELIMINA EL ULTIMO ELEMENTO 

listaSemana.pop(0)
print(listaSemana)
#Si le paso, borra el elemento de esa posicion


#Tambien puedo recorrer las listas 
for unDia in listaSemana:
    print(f"Dia {unDia}")
    
# La otra forma de recorrer es usando un range
for indice in range(2):
    print (f"dia {listaSemana[indice]}") #A veces no cierra la cantidad del range, por eso necesito pasarle la cantidad de elementos del range

for indice in range(len(listaSemana)):
    print(f"Dia {listaSemana[indice]}")
    if listaSemana[indice] == "Lunes":
        listaSemana[indice] == "Martes"

#listaBuscaVocales!!
listaPalabras = ["all", "arbol", "unananan", "love", "and", "get", "educated", "by", "gfg", "isla", "oso"]
extraidos = []
vocales = "aeiouAEIOU"
for palabra in listaPalabras:
    for ele in vocales:
        if palabra.startswith(ele):
            extraidos.append(palabra)
print("The extracted words : " + str(extraidos))

    
listaSemana.clear() #ESTE BORRA TODOO

#.sum suma los valores y .len devuelve la longitud de un elemento
promedio = sum(notas)/len(notas)

#.copy retorna una copia de una lista
# por ejemplo guarda todas las notas del alumno en una lista y las guarda en nombre del alumno(key)
clase[nombre] = listaNotas.copy()

#.count devuelve la cantidad de veces q se repite un elemento especificado
#count con string
s = "Hola mundo"
s.count("Hola")

#.startswith() para buscar un string que empiece con las letras ingresadas.
if k.startswith(busqueda):
    #imprimir k directamente para imprimir la clave, y agenda[k] para imprimir su valor
    print(f"Nombre: {k} Número: {agenda[k]}") 

#ZIP SUPER IMPORTANTE
clave= ['diez', 'veinte','treinta']
valores= [10, 20, 30]
dictc = dict(zip(clave, valores))
#convierte las listas en diccionarios

#funcion MIN
numeros = [9, 34, 11, -4, 27]
# find the smallest number
numeroMinimo= min(numeros)
print(numeroMinimo) #Output: -4

#funcion MAX
numeros = [9, 34, 11, -4, 27]
# find the smallest number
numeroMaximo= min(numeros)
print(numeroMaximo) #Output: 34


saludo = 'hola mundo'
saludo.upper() #muestra la misma cadena de texto pero con todos sus caracteres convertidos a letra mayuscula

presentacion = 'MI NOMBRE ES GABRIEL'
presentacion.lower() #muestra el string con todos sus caracteres en minuscula.

presentacion.islower() #devuelve True si y solo si todos los caracteres estan en mayuscula.

presentacion.isupper() #devuelve True si y solo si todos los caracteres estan en minuscula

saludo.startswith('hola') #devuelve True si y solo si la cadena de texto comienza con el valor del argumento (hola en este caso).

presentacion.endswith('RIEL') #devuelve True si y solo si la cadena de texto termine con el valor del argumento.

vacio = '          ' #devuelve True si y solo si todos los caracteres son espacios vacios.
vacio.isspace() 

titulo = 'Mi Planta De Naranja Lima'
titulo.istitle() #devuelve True si y solo si la primera letra de cada palabra comienza con mayuscula y el resto en minuscula.

dni = str(45092341)
dni.isdecimal() #devuelve True si y solo si todos los caracteres son numeros.

password = 'admin1234' 
password.isalpha() #devuelve True si y solo si todos los caracteres son letras del alfabeto.
password.isalnum() #devuelve True si y solo si todos los caracteres son letras del alfabeto O numeros.

cadena = "bienvenido a mi aplicacion".capitalize() #devuelve la cadena con todas las palabras con su letra inicial en mayúscula.

#find buscar el indice de una subcadena o caracter en una cadena, si no se encuentra lanza -1
cadena = "Hola, mundo. Tengo un poco de texto sin sentido."
subcadena = "mundo"
indice = cadena.find(subcadena)
print("La subcadena '{}' esta en el indice {}".format(subcadena, indice))

#index si no se encuentra una subcadena, se lanza una excepcion en lugar de devolver -1.
subcadena = ","
indice = cadena.index(subcadena)
print("La subcadena '{}' esta en el indice {}".format(subcadena, indice))
# La subcadena ',' esta en el indice 4


"Hola Mundo!".swapcase() #por su parte, cambia las mayusculas por minusculas y viceversa.

# replace() reemplaza una cadena por otra
s = "Hola mundo"
s.replace("mundo", "world") # s.replace(palabra a reemplazar, por la cual se la quiere reemplazar)

#join() debe ser llamado desde una cadena que actua como separador para unir dentro de 
#una misma cadena resultante los elementos de una lista.
listaCursa = ["lengua", "matematica"]
nombre = "Abril"
print (f"La alumna {nombre} cursa " + ", ".join(listaCursa))

#verificar si algo essta en una lista incluye un else
correoVerifica = ["abrilz@gmail.com", "brendahotmail"]

for elementos in (correoVerifica):
    #print(elementos)
    caracterEspecial = False
    for letra in elementos:
        if letra == "@":
            caracterEspecial= True
    if caracterEspecial == True:
        print("Ingreso su correo con exito!.")
    else:
        print("Falto el '@' del correo electronico...")

def validarCorreo (correoP):
    #también se puede utilizar in para encontrar un caracter
    if ("@") in correoP:
        print("Es valido")
    else:
        print("No es valido")

correo = input("Ingrese su correo electronico: ")
validarCorreo(correo)

#también
correoVerifica = ["abrilz@gmail.com", "brendahotmail"]

for i in range(len(correoVerifica)):
    #print(elementos)
    caracterEspecial = correoVerifica[i].find("@")
    if caracterEspecial != -1:
        print("Ingreso su correo con exito!.")
    else:
        print("Falto el '@' del correo electronico...")

def validarCorreo (listaCorreoP):
    for elementos in (listaCorreoP):
        if ("@") in elementos:
            print("Es valido")
        else:
            print("No es valido")
            
    
correoVerifica = ["abrilz@gmail.com", "brendahotmail"]
validarCorreo(correoVerifica)
# ---------- DICCIONARIOS --------------------------------------------------------------------
#para operar con los valores que están dentro de una lista, dentro de un diccionario
for claves, valores in pdicCuentas.items(): #recorre el diccionario
        saldoTotal = valores [1] #se asigna el valor necesitado a una variable
        negativoSaldo = valores[2] #se asigna el valor necesitado a una variable
    if (negativoSaldo == "S"): #comparacion
        saldoRestante = saldoTotal - pdineroRetirado #operacion
        valores[1] = saldoRestante #de ésta manera se sobreescribe el valor en la posicion
        print (f"Ha retirado ${pdineroRetirado} y su saldo actual es ${saldoRestante}.")

numeroCuenta = int(input("Ingrese el número para ingresar/crear una cuenta (ingrese 0 para salir del sistema): "))
if numeroCuenta in dictCuentas.keys(): #buscar el dato ingresado en las llaves 
    
# -----------------------------------------------------------------------------------------------

# CTRL H PARA BUSCAR UNA VARIABLE Y REEMPLAZARLAS TODAS AL MISMO TIEMPO