from flask import Flask, render_template, request, jsonify, redirect, session
import 

app = Flask(__name__, static_folder='static')
app.secret_key = 'pi'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    return render_template('menu.html')

def ObterApi():
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

if __name__ == '__main__':
    app.run(debug=True)