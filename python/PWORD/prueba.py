listaPalabras = ["all", "arbol", "unananan", "love", "and", "get", "educated", "by", "gfg", "isla", "oso"]
  
''''extraidos = []
vocales = "aeiouAEIOU"
for palabra in listaPalabras:
    #flag = False
    for ele in vocales:
        if palabra.startswith(ele):
            #flag = True
            extraidos.append(palabra)
    #if flag
# printing result
print("The extracted words : " + str(extraidos))'''

#verificar si algo essta en una lista incluye un else
correoVerifica = ["abrilz@gmail.com", "brendahotmail"]

for i in range(len(correoVerifica)):
    #print(elementos)
    caracterEspecial = correoVerifica[i].find("@")
    if caracterEspecial != -1:
        print("Ingreso su correo con exito!.")
    else:
        print("Falto el '@' del correo electronico...")
    