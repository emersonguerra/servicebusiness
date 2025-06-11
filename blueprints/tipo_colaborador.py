from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, TipoColaborador

tipo_colaborador_bp = Blueprint('tipo_colaborador', __name__, template_folder='tipo_colaborador')

@tipo_colaborador_bp.route('/')
def index():
    tipos = TipoColaborador.query.all()
    return render_template("crud_tipo_colaborador.html", tipos_colaborador=tipos)

@tipo_colaborador_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        descricao = request.form.get('descricao')
        status = request.form.get('status')
        dtdeleted = request.form.get('dtdeleted')
        novo = TipoColaborador(
            descricao=descricao,
            status=status,
            dtdeleted=dtdeleted
        )
        db.session.add(novo)
        db.session.commit()
        flash('Tipo de Colaborador adicionado com sucesso!', 'success')
        return redirect(url_for('tipo_colaborador.index'))
    return render_template("form_tipo_colaborador.html", tipo=None)

@tipo_colaborador_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    tipo = TipoColaborador.query.get_or_404(id)
    if request.method == 'POST':
        tipo.nome = request.form.get('nome')
        tipo.descricao = request.form.get('descricao')
        tipo.dtcreation = request.form.get('dtcreation')
        tipo.dtdeleted = request.form.get('dtdeleted')
        db.session.commit()
        flash('Tipo de Colaborador atualizado com sucesso!', 'success')
        return redirect(url_for('tipo_colaborador.index'))
    return render_template("form_tipo_colaborador.html", tipo=tipo)

@tipo_colaborador_bp.route('/delete/<int:id>')
def delete(id):
    tipo = TipoColaborador.query.get_or_404(id)
    db.session.delete(tipo)
    db.session.commit()
    flash('Tipo de Colaborador excluído com sucesso!', 'success')
    return redirect(url_for('tipo_colaborador.index'))
