'''def frecuencia(pNro,pDigito):
    nro, c = 0, 0
    for nro in pNro:
        if (nro==pDigito):
            c+=1
    return f"Frecuencia del digito {pDigito} en el nro: {c} "

nroentero=input("Ingrese un nro entero: ")
digito=input("Ingrese un digito: ")
print(frecuencia(nroentero, digito))

def frecuencia(numero,digito):
    cantidad=0
    while numero!=0:
        ultDigito=numero%10
    if ultDigito==digito:
        cantidad+=1
    numero=numero//10
    return cantidad


num=int(input("Número: "))
un_digito=int(input("Dígito: "))
print("Frecuencia del dígito en el número:",frecuencia(num,un_digito))'''

def frecuencia(numero,digito):
    c, nro=0, 0
    for nro in numero:
        if(nro == digito):
            c+=1
    return f"Frecuencia del digito en el numero: {c}"

 
num=input("Ingresar numero: ")
digitoI=input("Ingresar dígito:")
print(frecuencia(num, digitoI))