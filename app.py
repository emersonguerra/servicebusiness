from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

# Instância global do SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Inicializa o banco de dados
    db.init_app(app)
    
    # Configuração do Flask-Login
    login_manager = LoginManager(app)
    login_manager.login_view = 'usuario.login'  # Ajuste conforme sua rota de login
    
    # Registro dos Blueprints para cada entidade

    # 1. TipoColaborador
    from blueprints.tipo_colaborador import tipo_colaborador_bp
    app.register_blueprint(tipo_colaborador_bp, url_prefix='/tipo_colaborador')
    
    # 2. Colaborador
    from blueprints.colaborador import colaborador_bp
    app.register_blueprint(colaborador_bp, url_prefix='/colaborador')
    
    # 3. ColaboradorCentroCusto
    from blueprints.colaborador_centrocusto import colaborador_centrocusto_bp
    app.register_blueprint(colaborador_centrocusto_bp, url_prefix='/colaborador_centrocusto')
    
    # 4. TipoCentroCusto
    from blueprints.tipo_centrocusto import tipo_centrocusto_bp
    app.register_blueprint(tipo_centrocusto_bp, url_prefix='/tipo_centrocusto')
    
    # 5. CentroCusto
    from blueprints.centro_custo import centro_custo_bp
    app.register_blueprint(centro_custo_bp, url_prefix='/centro_custo')
    
    # 6. TipoConta
    from blueprints.tipo_conta import tipo_conta_bp
    app.register_blueprint(tipo_conta_bp, url_prefix='/tipo_conta')
    
    # 7. PlanoContas
    from blueprints.plano_contas import plano_contas_bp
    app.register_blueprint(plano_contas_bp, url_prefix='/plano_contas')
    
    # 8. PlanoContasCentroCusto
    from blueprints.plano_contas_centrocusto import plano_contas_centrocusto_bp
    app.register_blueprint(plano_contas_centrocusto_bp, url_prefix='/plano_contas_centrocusto')
    
    # 9. ProjetoCentroCustoIndiretos
    from blueprints.projeto_centrocusto_indiretos import projeto_centrocusto_indiretos_bp
    app.register_blueprint(projeto_centrocusto_indiretos_bp, url_prefix='/projeto_centrocusto_indiretos')
    
    # 10. TipoProdutoServico
    from blueprints.tipo_produto_servico import tipo_produto_servico_bp
    app.register_blueprint(tipo_produto_servico_bp, url_prefix='/tipo_produto_servico')
    
    # 11. ProdutoServico
    from blueprints.produto_servico import produto_servico_bp
    app.register_blueprint(produto_servico_bp, url_prefix='/produto_servico')
    
    # 12. Projetos
    from blueprints.projetos import projetos_bp
    app.register_blueprint(projetos_bp, url_prefix='/projetos')
    
    # 13. ProjetosReceita
    from blueprints.projetos_receita import projetos_receita_bp
    app.register_blueprint(projetos_receita_bp, url_prefix='/projetos_receita')
    
    # 14. ProjetosEsforco
    from blueprints.projetos_esforco import projetos_esforco_bp
    app.register_blueprint(projetos_esforco_bp, url_prefix='/projetos_esforco')
    
    # 15. Usuário
    from blueprints.usuario import usuario_bp
    app.register_blueprint(usuario_bp, url_prefix='/usuario')
    
    # Blueprint Principal (dashboard, menu, etc.)
    from blueprints.main import main_bp
    app.register_blueprint(main_bp)

    # banco criacao
    @app.route('/initdb')
    def initdb():
        db.create_all()
        return 'Tabelas criadas com sucesso!'
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
