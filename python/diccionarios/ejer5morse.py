def traductor(pPalabra):
    morse=" "
    for letra in pPalabra:
        morse+=f"{cgMorse[letra]} "
    
    return morse

cgMorse= {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", 
"g": "--.", "h": "....", "i": "..", "j": "·---", "k": "-.-", "l": ".-..", 
"m": "--", "n": "-.", "ñ": "--.--", "o": "---", "p": ".__.", "q": "--.-",
"r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--",
"x": "-..-", "y": "-.--", "z": "--.."}

palabra=input("Ingrese una palabra: ").lower()
print(traductor(palabra))