from flask import Blueprint, request, jsonify
from models import db, TipoProdutoServico
from schemas import TipoProdutoServicoSchema
from datetime import datetime

tipo_produto_servico_bp = Blueprint('tipo_produto_servico_bp', __name__)
schema = TipoProdutoServicoSchema()
schema_many = TipoProdutoServicoSchema(many=True)

@tipo_produto_servico_bp.route('/tipo_produto_servico', methods=['GET'])
def get_all_tipo_produto_servico():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    query = TipoProdutoServico.query.filter_by(dtdeleted=None).paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        'items': schema_many.dump(query.items),
        'total': query.total,
        'pages': query.pages,
        'current_page': query.page
    })

@tipo_produto_servico_bp.route('/tipo_produto_servico/<int:id>', methods=['GET'])
def get_tipo_produto_servico(id):
    item = TipoProdutoServico.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    return jsonify(schema.dump(item))

@tipo_produto_servico_bp.route('/tipo_produto_servico', methods=['POST'])
def create_tipo_produto_servico():
    data = request.get_json()
    obj = schema.load(data)
    novo = TipoProdutoServico(**obj)
    db.session.add(novo)
    db.session.commit()
    return jsonify(schema.dump(novo)), 201

@tipo_produto_servico_bp.route('/tipo_produto_servico/<int:id>', methods=['PUT'])
def update_tipo_produto_servico(id):
    item = TipoProdutoServico.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    data = request.get_json()
    obj = schema.load(data, partial=True)
    for key, value in obj.items():
        setattr(item, key, value)
    db.session.commit()
    return jsonify(schema.dump(item))

@tipo_produto_servico_bp.route('/tipo_produto_servico/<int:id>', methods=['DELETE'])
def delete_tipo_produto_servico(id):
    item = TipoProdutoServico.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    item.dtdeleted = datetime.utcnow()
    db.session.commit()
    return jsonify({'message': 'Registro excluído (soft delete)'})
