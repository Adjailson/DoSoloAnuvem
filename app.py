from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///phenoglad.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret_key'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

@app.route('/', methods=["GET", "POST"])
def home():
    return render_template('index.html')

@app.route('/registro', methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form.get('nome', '').strip()
        email = request.form.get('email', '').strip()
        senha_raw = request.form.get('senha', '')
        confirmar = request.form.get('confirmar', '')

        if senha_raw != confirmar:
            flash('As senhas não coincidem.')
            return redirect(url_for('registro'))

        if User.query.filter_by(email=email).first():
            flash('E-mail já cadastrado.')
            return redirect(url_for('registro'))

        senha = generate_password_hash(senha_raw)
        novo_usuario = User(nome=nome, email=email, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()

        flash('Cadastro realizado com sucesso. Faça login.')
        return redirect(url_for('loginpage'))

    return render_template('registro.html')

@app.route('/loginpage', methods=["GET", "POST"])
def loginpage():
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']
        usuario = User.query.filter_by(email=email).first()
        if usuario and check_password_hash(usuario.senha, senha):
            return redirect(url_for('inicio'))
        else:
            flash('Email ou senha incorretos.')
    return render_template('login.html')

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)