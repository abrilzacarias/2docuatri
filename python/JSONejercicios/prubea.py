m = [{"cvu": 4444,
    "mov": [{"fecha": "11-11",
            "monto": 200,
            "persona": 12131}]}]

j = {"fecha": "11-11",
            "monto": 200,
            "persona": 12131}
m[0]["mov"].append(j)

print(m)