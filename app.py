from flask import Flask, render_template, request, jsonify, redirect, session

app = Flask(__name__, static_folder='static')
app.secret_key = 'pi'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/menu', methods=['GET', 'POST'])
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True)