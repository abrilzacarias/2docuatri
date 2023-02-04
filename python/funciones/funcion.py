'''def saludar():
    print("Hola mundo")

saludar()'''

def sumarDosNumeros(pNum1,pNum2 = 0): #parametros, se puede definir por default sino se pasa un valor, está configurado así
    resultado = 0
    resultado = pNum1+pNum2
    print(f"Resultado = {resultado} ")
    return
#parametros en la funcion, cuando se invoca se le llaman argumentos

sumarDosNumeros(10, 20) #argumentos