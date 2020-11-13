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

@fut.route("/mensagem")
def mensagem():
    return render_template("mensagem.html")

@fut.route("/cadastrar")
def cadastro():
    return render_template("cadastro.html")

@fut.route("/cadastrar", methods=['GET','POST'])
def cadastrar():
    if request.method=="POST":
        time=(request.form.get("time"))
        ponto=(request.form.get("ponto"))
        jogos=(request.form.get("jogos"))
        vitorias=(request.form.get("vitorias"))
        empates=(request.form.get("empates"))
        derrotas=(request.form.get("derrotas"))
        gols_pro=(request.form.get("gols_pro"))
        gols_contra=(request.form.get("gols_contra"))
        saldo_gols=(request.form.get("saldo_gols"))
        if time:
            f = brasileirao(time, ponto, jogos, vitorias, empates,
            derrotas, gols_pro, gols_contra, saldo_gols)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("mensagem"))

@fut.route("/consultar")
def consultar():
   return render_template("consulta.html")

@fut.route("/listar")
def listar():
    f = brasileirao.query.filter_by("consulta.html",name="time").first()
    brasileirao.id
    brasileirao.time
    brasileirao.ponto
    brasileirao.jogos
    brasileirao.vitorias
    brasileirao.empates
    brasileirao.derrotas
    brasileirao.gols_pro
    brasileirao.gols_contra
    brasileirao.saldo_gols

    return render_template("consulta.html",brasileirao=f)

 




if __name__ =="__main__":
    fut.run(debug=True)

