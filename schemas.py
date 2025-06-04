from marshmallow import Schema, fields, validate

# ----------------- Schemas -----------------

class TipoColaboradorSchema(Schema):
    id = fields.Int(dump_only=True)
    descricao = fields.Str(required=True, validate=validate.Length(max=100))
    status = fields.Bool(missing=True)
    dtdeleted = fields.DateTime(allow_none=True)


class ColaboradorSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True, validate=validate.Length(max=100))
    salario = fields.Float(required=True)
    extensao_equipe = fields.Bool(missing=False)
    projeto = fields.Str(allow_none=True, validate=validate.Length(max=100))
    funcao = fields.Str(required=True, validate=validate.Length(max=100))
    tipo_colaborador_id = fields.Int(required=True)
    status = fields.Bool(missing=True)
    dtdeleted = fields.DateTime(allow_none=True)
    dtcreation = fields.DateTime(dump_only=True)


class ColaboradorCentroCustoSchema(Schema):
    id = fields.Int(dump_only=True)
    competencia = fields.Date(required=True, format="%m/%y")
    colaborador_id = fields.Int(required=True)
    centro_custo_id = fields.Int(required=True)
    alocacao = fields.Int()
    status = fields.Bool(missing=True)
    dtcreation = fields.DateTime(dump_only=True)
    dtdeleted = fields.DateTime(allow_none=True)


class TipoCentroCustoSchema(Schema):
    id = fields.Int(dump_only=True)
    tipo = fields.Str(required=True, validate=validate.Length(max=50))
    status = fields.Bool(missing=True)
    dtcreation = fields.DateTime(dump_only=True)
    dtdeleted = fields.DateTime(allow_none=True)


class CentroCustoSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True, validate=validate.Length(max=100))
    codigo = fields.Str(required=True, validate=validate.Length(max=20))
    tipo_id = fields.Int(required=True)
    status = fields.Bool(missing=True)
    dtcreation = fields.DateTime(dump_only=True)
    dtdeleted = fields.DateTime(allow_none=True)


class TipoContaSchema(Schema):
    id = fields.Int(dump_only=True)
    tipo_conta = fields.Str(required=True, validate=validate.Length(max=100))
    status = fields.Bool(missing=True)
    dtcreation = fields.DateTime(dump_only=True)
    dtdeleted = fields.DateTime(allow_none=True)


class PlanoContasSchema(Schema):
    id = fields.Int(dump_only=True)
    descricao = fields.Str(required=True, validate=validate.Length(max=200))
    codigo_contabil = fields.Str(required=True, validate=validate.Length(max=50))
    codigo_interno = fields.Str(allow_none=True)
    formula = fields.Str(allow_none=True)
    tipo_conta_id = fields.Int(required=True)
    status = fields.Bool(missing=True)
    dtdeleted = fields.DateTime(allow_none=True)


class PlanoContasCentroCustoSchema(Schema):
    id = fields.Int(dump_only=True)
    competencia = fields.Date(required=True, format="%m/%y")
    plano_contas_id = fields.Int(required=True)
    valor_orcado = fields.Float(required=True)
    valor_realizado = fields.Float(required=True)
    centro_custo_id = fields.Int(required=True)
    status = fields.Bool(missing=True)
    dtcreation = fields.DateTime(dump_only=True)
    dtdeleted = fields.DateTime(allow_none=True)


class ProjetoCentroCustoIndiretosSchema(Schema):
    id = fields.Int(dump_only=True)
    competencia = fields.Date(required=True, format="%m/%y")
    projeto_id = fields.Int(required=True)
    centro_custo_id = fields.Int(required=True)
    alocacao_orcado = fields.Float()
    alocacao_realizado = fields.Float()
    status = fields.Bool(missing=True)
    dtcreation = fields.DateTime(dump_only=True)
    dtdeleted = fields.DateTime(allow_none=True)


class TipoProdutoServicoSchema(Schema):
    id = fields.Int(dump_only=True)
    tipo = fields.Str(required=True, validate=validate.Length(max=50))
    status = fields.Bool(missing=True)
    dtcreation = fields.DateTime(dump_only=True)
    dtdeleted = fields.DateTime(allow_none=True)


class ProdutoServicoSchema(Schema):
    id = fields.Int(dump_only=True)
    codigo = fields.Str(required=True, validate=validate.Length(max=50))
    descricao = fields.Str(required=True, validate=validate.Length(max=100))
    tipo_id = fields.Int(required=True)
    unidade = fields.Str(validate=validate.Length(max=10))
    preco_custo = fields.Float()
    preco_venda = fields.Float()
    qtd_minima = fields.Int()
    status = fields.Bool(missing=True)
    dtcreation = fields.DateTime(dump_only=True)
    dtdeleted = fields.DateTime(allow_none=True)


class ProjetosSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True, validate=validate.Length(max=100))
    cliente = fields.Str(required=True, validate=validate.Length(max=100))
    status = fields.Bool(missing=True)
    dtcreation = fields.DateTime(dump_only=True)
    dtdeleted = fields.DateTime(allow_none=True)


class ProjetosReceitaSchema(Schema):
    id = fields.Int(dump_only=True)
    competencia = fields.Date(required=True, format="%m/%y")
    projeto_id = fields.Int(required=True)
    receita_orcada = fields.Float()
    receita_realizado = fields.Float()
    item_id = fields.Int(required=True)
    status = fields.Bool(missing=True)
    dtcreation = fields.DateTime(dump_only=True)
    dtdeleted = fields.DateTime(allow_none=True)


class ProjetosEsforcoSchema(Schema):
    id = fields.Int(dump_only=True)
    competencia = fields.Date(required=True, format="%m/%y")
    projeto_id = fields.Int(required=True)
    centro_custo_id = fields.Int(required=True)
    horas_orcadas = fields.Int()
    horas_realizadas = fields.Int()
    status = fields.Bool(missing=True)
    dtcreation = fields.DateTime(dump_only=True)
    dtdeleted = fields.DateTime(allow_none=True)

# ----------------- Schema para Usuário -----------------
class UsuarioSchema(Schema):
    id = fields.Int(dump_only=True)
    nome = fields.Str(required=True, validate=validate.Length(max=100))
    email = fields.Email(required=True, validate=validate.Length(max=120))
    role = fields.Str(missing='usuario')
    # O campo 'senha' não deve ser exposto em operações de leitura; utilize-o apenas no carregamento para criação.
    senha = fields.Str(load_only=True, required=True, validate=validate.Length(min=6))
    # O campo reset_token pode ser utilizado internamente para recuperação/redefinição de senha, mas geralmente não é exposto.
