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
    nome = db.Column(db.String(50))
    ponto = db.Column(db.Integer,nullable=True)
    jogos = db.Column(db.Integer,nullable=True)
    vitorias = db.Column(db.Integer,nullable=True)
    empates = db.Column(db.Integer,nullable=True)
    derrotas = db.Column(db.Integer,nullable=True)
    gols_pro = db.Column(db.Integer,nullable=True)
    gols_contra = db.Column(db.Integer,nullable=True)
    saldo_gols = db.Column(db.Integer,nullable=True)
    def __init__(self, nome, ponto, jogos, vitorias, empates,
    derrotas, gols_pro, gols_contra, saldo_gols):
        self.nome = nome
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

@fut.route("/mensagem")
def mensagem():
    return render_template("mensagem.html")

@fut.route("/cadastrar")
def cadastro():
    return render_template("cadastro.html")

@fut.route("/cadastrar", methods=['GET','POST'])
def cadastrar():
    if request.method=="POST":
        nome=(request.form.get("nome"))
        ponto=(request.form.get("ponto"))
        jogos=(request.form.get("jogos"))
        vitorias=(request.form.get("vitorias"))
        empates=(request.form.get("empates"))
        derrotas=(request.form.get("derrotas"))
        gols_pro=(request.form.get("gols_pro"))
        gols_contra=(request.form.get("gols_contra"))
        saldo_gols=(request.form.get("saldo_gols"))
        if nome:
            f = brasileirao(nome, ponto, jogos, vitorias, empates,
            derrotas, gols_pro, gols_contra, saldo_gols)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("mensagem"))

@fut.route("/consultar",methods=['GET','POST'])
def consultar():
    return render_template("consulta.html")

@fut.route("/listar")
def listar():
     
    cons = brasileirao.query.filter_by((request.form.get("nome"))).first()
    cons.id_
    cons.nome
    cons.ponto
    cons.jogos
    cons.vitorias
    cons.empates
    cons.derrotas
    cons.gols_pro
    cons.gols_contra
    cons.saldo_gols

    return render_template("consulta.html",time=cons)

 




if __name__ =="__main__":
    fut.run(debug=True)

