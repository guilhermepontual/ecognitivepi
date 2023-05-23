import requests

url = "https://api.thingspeak.com/channels/2121478/fields/1.json"
headers = {"Authorization": "Bearer YOUR_TOKEN_HERE"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Faça algo com os dados recebidos
    print(data)
else:
    print("A requisição falhou com o código de status:", response.status_code)
