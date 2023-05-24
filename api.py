import requests

url = "https://api.thingspeak.com/channels/2121478/fields/1.json"
headers = {"Authorization": "Bearer YOUR_TOKEN_HERE"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    feeds = data["feeds"]
    field1_values = [feed["field1"] for feed in feeds if feed["field1"] is not None]
    print("Valores do field1:", field1_values)
else:
    print("A requisição falhou com o código de status:", response.status_code)
