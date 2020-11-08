from flask import Flask
from flask import render_template, url_for, redirect



fut = Flask(__name__)
#Criando as Rotas
@fut.route("/teste")
def teste():
    return 'EEEE Beleza, funcionou!'

@fut.route("/")
@fut.route("/index")
def index():
    return render_template("index.html")

@fut.route("/serie_a")
def serie_a():
    return render_template("serie_a.html")

@fut.route("/pontuacao")
def pontuacao():
    return render_template("pontuacao.html")

@fut.route("/administrador")
def adm():
    return render_template("administrador.html")

if __name__ =="__main__":
    fut.run(debug=True)

