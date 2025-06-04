

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# ----------------- Models -----------------

class TipoColaborador(db.Model):
    __tablename__ = 'tipo_colaborador'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    dtdeleted = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<TipoColaborador {self.descricao}>"


class Colaborador(db.Model):
    __tablename__ = 'colaborador'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    salario = db.Column(db.Float, nullable=False)
    extensao_equipe = db.Column(db.Boolean, default=False)
    projeto = db.Column(db.String(100), nullable=True)
    funcao = db.Column(db.String(100), nullable=False)
    tipo_colaborador_id = db.Column(db.Integer, db.ForeignKey('tipo_colaborador.id'), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    dtdeleted = db.Column(db.DateTime, nullable=True)
    dtcreation = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self):
        return f"<Colaborador {self.nome}, Salario: {self.salario}>"


class ColaboradorCentroCusto(db.Model):
    __tablename__ = 'colaborador_centrocusto'
    id = db.Column(db.Integer, primary_key=True)
    competencia = db.Column(db.Date, nullable=False)
    colaborador_id = db.Column(db.Integer, db.ForeignKey('colaborador.id'), nullable=False)
    centro_custo_id = db.Column(db.Integer, db.ForeignKey('centro_custo.id'), nullable=False)
    alocacao = db.Column(db.Integer)
    status = db.Column(db.Boolean, nullable=True, default=True)
    dtcreation = db.Column(db.DateTime, default=db.func.current_timestamp())
    dtdeleted = db.Column(db.DateTime, nullable=True)


class TipoCentroCusto(db.Model):
    __tablename__ = 'tipo_centro_custo'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Boolean, nullable=True, default=True)
    dtcreation = db.Column(db.DateTime, default=db.func.current_timestamp())
    dtdeleted = db.Column(db.DateTime, nullable=True)


class CentroCusto(db.Model):
    __tablename__ = 'centro_custo'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    codigo = db.Column(db.String(20), nullable=False, unique=True)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipo_centro_custo.id'), nullable=False)
    status = db.Column(db.Boolean, default=True)
    dtcreation = db.Column(db.DateTime, default=db.func.current_timestamp())
    dtdeleted = db.Column(db.DateTime, nullable=True)


class TipoConta(db.Model):
    __tablename__ = 'tipo_conta'
    id = db.Column(db.Integer, primary_key=True)
    tipo_conta = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    dtdeleted = db.Column(db.DateTime, nullable=True)
    dtcreation = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())


class PlanoContas(db.Model):
    __tablename__ = 'planocontas'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    codigo_contabil = db.Column(db.String(50), unique=True, nullable=False)
    codigo_interno = db.Column(db.String(50), nullable=True)
    formula = db.Column(db.String(50), nullable=True)
    tipo_conta_id = db.Column(db.Integer, db.ForeignKey('tipo_conta.id'), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    dtdeleted = db.Column(db.DateTime, nullable=True)


class PlanoContasCentroCusto(db.Model):
    __tablename__ = 'planocontas_centrocusto'
    id = db.Column(db.Integer, primary_key=True)
    competencia = db.Column(db.Date, nullable=False)
    plano_contas_id = db.Column(db.Integer, db.ForeignKey('planocontas.id'), nullable=False)
    valor_orcado = db.Column(db.Float, nullable=False)
    valor_realizado = db.Column(db.Float, nullable=False)
    centro_custo_id = db.Column(db.Integer, db.ForeignKey('centro_custo.id'), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    dtdeleted = db.Column(db.DateTime, nullable=True)
    dtcreation = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())


class ProjetoCentroCustoIndiretos(db.Model):
    __tablename__ = 'projeto_centrocusto_indiretos'
    id = db.Column(db.Integer, primary_key=True)
    competencia = db.Column(db.Date, nullable=False)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projetos.id'), nullable=False)
    centro_custo_id = db.Column(db.Integer, db.ForeignKey('centro_custo.id'), nullable=False)
    alocacao_orcado = db.Column(db.Float)
    alocacao_realizado = db.Column(db.Float)
    status = db.Column(db.Boolean, default=True)
    dtcreation = db.Column(db.DateTime, default=datetime.utcnow)
    dtdeleted = db.Column(db.DateTime, nullable=True)


class TipoProdutoServico(db.Model):
    __tablename__ = 'tipo_produto_servico'
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Boolean, default=True)
    dtcreation = db.Column(db.DateTime, default=db.func.current_timestamp())
    dtdeleted = db.Column(db.DateTime, nullable=True)


class ProdutoServico(db.Model):
    __tablename__ = 'produto_servico'
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipo_produto_servico.id'), nullable=False)
    unidade = db.Column(db.String(10))
    preco_custo = db.Column(db.Float)
    preco_venda = db.Column(db.Float)
    qtd_minima = db.Column(db.Integer)
    status = db.Column(db.Boolean, default=True)
    dtcreation = db.Column(db.DateTime, default=db.func.current_timestamp())
    dtdeleted = db.Column(db.DateTime, nullable=True)


class Projetos(db.Model):
    __tablename__ = 'projetos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    cliente = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, default=True)
    dtcreation = db.Column(db.DateTime, default=db.func.current_timestamp())
    dtdeleted = db.Column(db.DateTime, nullable=True)


class ProjetosReceita(db.Model):
    __tablename__ = 'projetos_receita'
    id = db.Column(db.Integer, primary_key=True)
    competencia = db.Column(db.Date, nullable=False)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projetos.id'), nullable=False)
    receita_orcada = db.Column(db.Float)
    receita_realizado = db.Column(db.Float)
    item_id = db.Column(db.Integer, db.ForeignKey('produto_servico.id'), nullable=False)
    status = db.Column(db.Boolean, default=True)
    dtcreation = db.Column(db.DateTime, default=db.func.current_timestamp())
    dtdeleted = db.Column(db.DateTime, nullable=True)


class ProjetosEsforco(db.Model):
    __tablename__ = 'projetos_esforco'
    id = db.Column(db.Integer, primary_key=True)
    competencia = db.Column(db.Date, nullable=False)
    projeto_id = db.Column(db.Integer, db.ForeignKey('projetos.id'), nullable=False)
    centro_custo_id = db.Column(db.Integer, db.ForeignKey('centro_custo.id'), nullable=False)
    horas_orcadas = db.Column(db.Integer)
    horas_realizadas = db.Column(db.Integer)
    status = db.Column(db.Boolean, default=True)
    dtcreation = db.Column(db.DateTime, default=db.func.current_timestamp())
    dtdeleted = db.Column(db.DateTime, nullable=True)

# ----------------- Entidade Usuário ----------------- 
class Usuario(db.Model): 
    __tablename__ = 'usuarios' 
    id = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(100), nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False) 
    senha = db.Column(db.String(128), nullable=False) 
    role = db.Column(db.String(50), default='usuario', nullable=False) 
    # Armazene a senha já hasheada 
    reset_token = db.Column(db.String(128), nullable=True) 
    dtcreation = db.Column(db.DateTime, default=db.func.current_timestamp())



