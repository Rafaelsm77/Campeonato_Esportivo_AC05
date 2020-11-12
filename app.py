from flask import Flask
from flask import render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy




fut = Flask(__name__)
#Criando banco de dados

        
fut.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@1902535@localhost/brasileirao'
db = SQLAlchemy(fut)

class brasileirao(db.Model):
    __tablename__ = 'time'
    id_ = db.Column(db.Integer,primary_key=True,autoincrement=True)
    time = db.Column(db.String(50))
    ponto = db.Column(db.Integer,nullable=True)
    jogos = db.Column(db.Integer,nullable=True)
    vitorias = db.Column(db.Integer,nullable=True)
    empates = db.Column(db.Integer,nullable=True)
    derrotas = db.Column(db.Integer,nullable=True)
    gols_pro = db.Column(db.Integer,nullable=True)
    gols_contra = db.Column(db.Integer,nullable=True)
    saldo_gols = db.Column(db.Integer,nullable=True)
    def __init__(self, time, ponto, jogos, vitorias, empates,
    derrotas, gols_pro, gols_contra, saldo_gols):
        self.time = time
        self.ponto = ponto
        self.jogos = jogos
        self.vitorias = vitorias
        self.empates = empates
        self.derrotas = derrotas
        self.gols_pro = gols_pro
        self.gols_contra = gols_contra
        self.saldo_gols = saldo_gols

db.create_all()      
    

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

@fut.route("/cadastrar", methods=['GET','POST'])
def cadastrar():
    return render_template("cadastro.html")




if __name__ =="__main__":
    fut.run(debug=True)

