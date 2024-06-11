# importa a class Flask do módulo flask
from flask import Flask

# Instancia um objeto flask que representa a
# aplicação
app = Flask("Minha Aplicação")

# rota + função
# rota: definição de um padrão de url
# função: função python com retorno (string, template, outro)

# página home - /
@app.route("/")
def home():
    return "<h1>Home page</h1>"

# página contato - /contato
@app.route("/contato")
def contato():
    return "<h1>Contato</h1>"

# página produtos - /produtos
@app.route("/produtos")
def produtos():
    return "<h1>Produtos</h1>"

