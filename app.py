from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Rota para realizar pesquisa a partir de um titulo que se envia desde o cliente.
@app.route('/pesquisar', methods=['POST'])
def pesquisar():
    titulo = request.form.get('title')
    dados = {
        'status': 'ok',
        'tirulo': titulo,
        'id': 1,
    }
    return jsonify(dados)