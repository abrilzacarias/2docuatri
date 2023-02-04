""" Desarrolle una función que recibe una lista de palabras y una letra, tal que retorne en una lista
todas las palabras que inicien con esa letra.
"""

def x(plistaPalabras, pLetra):
    for i in plistaPalabras:
        if i.startswith(letra):
            print(i)

listaPalabras = ["juan", "taylor", "river", "mora", "tambor", "junta", "risa", "morado"]

letra = input("Ingrese una letra: ")
x(listaPalabras, letra)
