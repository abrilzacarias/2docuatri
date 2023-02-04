import json
import requests

URL = "https://api-dolar-argentina.herokuapp.com/api/dolaroficial"
cuentas = []

data = requests.get(URL)
data = data.json()

compra = data["compra"]
print(float(compra))