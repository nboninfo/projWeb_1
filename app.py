from flask import Flask, jsonify, render_template, request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Rota para realizar pesquisa a partir de um titulo que se envia desde o cliente.
@app.route('/pesquisar', methods=['POST'])
def pesquisar():
    titulo = request.form.get('title')

    driver = criar_driver()

    dados = {
        'status': 'ok',
        'tirulo': titulo,
        'pesq-centesima': livraria_centesima(driver),
    }
    return jsonify(dados)

def criar_driver():
    driver = webdriver.Firefox()
    return driver

def livraria_centesima(driver, titulo):
    driver.get('https://centesima.com/')

    # Encontra el input da pesquisa
    pesquisa = driver.find_element_by_name('Pesquisa')
    pesquisa.send_keys(titulo)
    pesquisa.send_keys(keys.ENTER)

    return driver.page_source

'''
def livraria_devagar(driver):
    driver.get('https://lerdevagar.com/')
    driver.find_elementy_by_id('search-autocomplete-input').send_key('livros')
    driver.find_elementy_by_id('search-autocomplete-input').sumit()
    return driver

def livraria_ferin(driver):
    driver.get('https://ferin.pt/')
    driver.find_elementy_by_id('search-autocomplete-input').send_key('livros')
    driver.find_elementy_by_id('search-autocomplete-input').sumit()
    return driver

def livraria_bertrand(driver):
    driver.get('https://www.bertrand.pt/')
    driver.find_elementy_by_id('search-autocomplete-input').send_key('livros')
    driver.find_elementy_by_id('search-autocomplete-input').sumit()
    return driver

def livraria_santiago(driver):
    driver.get('https://livrariasantiago.com/')
    driver.find_elementy_by_id('search-autocomplete-input').send_key('livros')
    driver.find_elementy_by_id('search-autocomplete-input').sumit()
    return driver

def livraria_lello(driver):
    driver.get('https://www.livrarialello.pt/')
    driver.find_elementy_by_id('search-autocomplete-input').send_key('livros')
    driver.find_elementy_by_id('search-autocomplete-input').sumit()
    return driver
    '''