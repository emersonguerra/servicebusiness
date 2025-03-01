from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Colaborador, TipoColaborador

colaborador_bp = Blueprint('colaborador', __name__, template_folder='colaborador')

@colaborador_bp.route('/')
def index():
    colaboradores = Colaborador.query.all()
    return render_template('colaborador/crud_colaborador.html', colaboradores=colaboradores)

@colaborador_bp.route('/add', methods=['GET', 'POST'])
def add():
    # Busca os tipos para preencher o select no formulário
    tipos = TipoColaborador.query.all()
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        cpf = request.form.get('cpf')
        telefone = request.form.get('telefone')
        cargo = request.form.get('cargo')
        data_admissao = request.form.get('data_admissao')
        salario = request.form.get('salario')
        tipo_colaborador_id = request.form.get('tipo_colaborador_id')
        dtcreation = request.form.get('dtcreation')
        dtdeleted = request.form.get('dtdeleted')
        projeto = request.form.get('projeto')
        extensao_equipe = request.form.get('extensao_equipe')
        
        novo = Colaborador(
            nome=nome,
            email=email,
            cpf=cpf,
            telefone=telefone,
            cargo=cargo,
            data_admissao=data_admissao,
            salario=salario,
            tipo_colaborador_id=tipo_colaborador_id,
            dtcreation=dtcreation,
            dtdeleted=dtdeleted,
            projeto=projeto,
            extensao_equipe=extensao_equipe
        )
        db.session.add(novo)
        db.session.commit()
        flash('Colaborador adicionado com sucesso!', 'success')
        return redirect(url_for('colaborador.index'))
    return render_template('colaborador/form_colaborador.html', colaborador=None, tipos_colaborador=tipos)

@colaborador_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    colaborador = Colaborador.query.get_or_404(id)
    tipos = TipoColaborador.query.all()
    if request.method == 'POST':
        colaborador.nome = request.form.get('nome')
        colaborador.email = request.form.get('email')
        colaborador.cpf = request.form.get('cpf')
        colaborador.telefone = request.form.get('telefone')
        colaborador.cargo = request.form.get('cargo')
        colaborador.data_admissao = request.form.get('data_admissao')
        colaborador.salario = request.form.get('salario')
        colaborador.tipo_colaborador_id = request.form.get('tipo_colaborador_id')
        colaborador.dtcreation = request.form.get('dtcreation')
        colaborador.dtdeleted = request.form.get('dtdeleted')
        colaborador.projeto = request.form.get('projeto')
        colaborador.extensao_equipe = request.form.get('extensao_equipe')
        db.session.commit()
        flash('Colaborador atualizado com sucesso!', 'success')
        return redirect(url_for('colaborador.index'))
    return render_template('colaborador/form_colaborador.html', colaborador=colaborador, tipos_colaborador=tipos)

@colaborador_bp.route('/delete/<int:id>')
def delete(id):
    colaborador = Colaborador.query.get_or_404(id)
    db.session.delete(colaborador)
    db.session.commit()
    flash('Colaborador excluído com sucesso!', 'success')
    return redirect(url_for('colaborador.index'))
