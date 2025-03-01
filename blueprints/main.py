from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__, template_folder='main')

@main_bp.route('/dashboard')
@login_required
def dashboard():
    # Lista de entidades conforme seu back; adicione ou remova conforme necessário.
    entidades = [
        'Tipo Colaborador',
        'Colaborador',
        'Colaborador Centro Custo',
        'Tipo Centro Custo',
        'Centro Custo',
        'Tipo Conta',
        'Plano Contas',
        'Plano Contas Centro Custo',
        'Projeto Centro Custo Indiretos',
        'Tipo Produto Serviço',
        'Produto Serviço',
        'Projetos',
        'Projetos Receita',
        'Projetos Esforço',
        'Usuário'
    ]
    return render_template('dashboard.html', entidades=entidades)
