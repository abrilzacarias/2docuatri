import json

mov = []
with open("movimientos.json") as jsonfile:
    mov = json.load(jsonfile)

"""usuario = input("ingrese su usuario: ")
fecha = input("Ingrese fecha: ")
movimiento = float(input("Ingrese mov: "))
transacciones = input("Ingrese a quien: ")

m = {"cvu": usuario,
    "fecha": fecha,
"movimientos": [-200, 400, -800, 200, 1000, -800],
"destino": transacciones
}"""


m["movimientos"].insert(0, movimiento)
mov.append(m)

with open("movimientos.json", "w") as jsonfile:
    json.dump(mov, jsonfile)

print(m["movimientos"][0:3])
