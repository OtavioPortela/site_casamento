from app import app, db
from flask import render_template, request, redirect, url_for, session
from app.models import Present, Confirm, Contribution
import os

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/presentes')
def presentes():
    presentes = Present.query.all()
    return render_template('presentes.html', presentes=presentes)

@app.route('/presenca')
def presenca():
    return render_template('presenca.html')

@app.route('/confirmar_presenca', methods=['POST'])
def confirmar_presenca():
    nome = request.form['nome']
    telefone = request.form['telefone']
    endereco = request.form['endereco']
    confirm = Confirm(nome=nome, telefone=telefone, endereco=endereco)
    db.session.add(confirm)
    db.session.commit()
    return redirect(url_for('presenca'))

@app.route('/confirmacoes')
def confirmacoes():
    confirmacoes = Confirm.query.all()
    return render_template('confirmacoes.html', confirmacoes=confirmacoes)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'otavio' and password == '1206':
            session['logged_in'] = True
            return redirect(url_for('admin'))
    return render_template('login.html')

@app.route('/admin')
def admin():
    if 'logged_in' in session:
        return render_template('admin.html')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/adicionar_presente', methods=['GET', 'POST'])
def adicionar_presente():
    if 'logged_in' in session:
        if request.method == 'POST':
            name = request.form['name']
            description = request.form['description']
            image_file = request.files['image_file']
            image_filename = image_file.filename
            
            # Verifique e crie o diretório se não existir
            upload_path = os.path.join('app/static/uploads')
            if not os.path.exists(upload_path):
                os.makedirs(upload_path)
            
            image_path = os.path.join(upload_path, image_filename)
            image_file.save(image_path)
            
            present = Present(name=name, description=description, image_file=image_filename)
            db.session.add(present)
            db.session.commit()
            return redirect(url_for('adicionar_presente'))
        presentes = Present.query.all()
        return render_template('adicionar_presente.html', presentes=presentes)
    return redirect(url_for('login'))

@app.route('/excluir_presente/<int:id>', methods=['POST'])
def excluir_presente(id):
    if 'logged_in' in session:
        present = Present.query.get(id)
        if present:
            db.session.delete(present)
            db.session.commit()
        return redirect(url_for('adicionar_presente'))
    return redirect(url_for('login'))

@app.route('/contribuicoes', methods=['POST'])
def contribuicoes():
    nome = request.form['nome']
    mensagem = request.form['mensagem']
    contribution = Contribution(nome=nome, mensagem=mensagem)
    db.session.add(contribution)
    db.session.commit()
    return redirect(url_for('presentes'))

@app.route('/ver_contribuicoes')
def ver_contribuicoes():
    if 'logged_in' in session:
        contribuicoes = Contribution.query.all()
        return render_template('ver_contribuicoes.html', contribuicoes=contribuicoes)
    return redirect(url_for('login'))
