from flask import Blueprint, render_template, redirect, url_for, request, flash
from models import db, Colaborador

colaborador_bp = Blueprint('colaborador', __name__, template_folder='colaborador')

@colaborador_bp.route('/')
def index():
    colaboradores = Colaborador.query.all()
    return render_template('crud_colaborador.html', colaboradores=colaboradores)

@colaborador_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nome = request.form.get('nome')
        # Adicione aqui outros campos conforme o seu modelo
        novo_colaborador = Colaborador(nome=nome)
        db.session.add(novo_colaborador)
        db.session.commit()
        flash('Colaborador adicionado com sucesso!', 'success')
        return redirect(url_for('colaborador.index'))
    return render_template('form_colaborador.html', colaborador=None)

@colaborador_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    colaborador = Colaborador.query.get_or_404(id)
    if request.method == 'POST':
        colaborador.nome = request.form.get('nome')
        # Atualize outros campos conforme necessário
        db.session.commit()
        flash('Colaborador atualizado com sucesso!', 'success')
        return redirect(url_for('colaborador.index'))
    return render_template('form_colaborador.html', colaborador=colaborador)

@colaborador_bp.route('/delete/<int:id>')
def delete(id):
    colaborador = Colaborador.query.get_or_404(id)
    db.session.delete(colaborador)
    db.session.commit()
    flash('Colaborador excluído com sucesso!', 'success')
    return redirect(url_for('colaborador.index'))
