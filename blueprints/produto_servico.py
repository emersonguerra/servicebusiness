from flask import Blueprint, request, jsonify
from models import db, ProdutoServico
from schemas import ProdutoServicoSchema
from datetime import datetime

produto_servico_bp = Blueprint('produto_servico_bp', __name__)
schema = ProdutoServicoSchema()
schema_many = ProdutoServicoSchema(many=True)

@produto_servico_bp.route('/produto_servico', methods=['GET'])
def get_all_produto_servico():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    query = ProdutoServico.query.filter_by(dtdeleted=None).paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        'items': schema_many.dump(query.items),
        'total': query.total,
        'pages': query.pages,
        'current_page': query.page
    })

@produto_servico_bp.route('/produto_servico/<int:id>', methods=['GET'])
def get_produto_servico(id):
    item = ProdutoServico.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    return jsonify(schema.dump(item))

@produto_servico_bp.route('/produto_servico', methods=['POST'])
def create_produto_servico():
    data = request.get_json()
    obj = schema.load(data)
    novo = ProdutoServico(**obj)
    db.session.add(novo)
    db.session.commit()
    return jsonify(schema.dump(novo)), 201

@produto_servico_bp.route('/produto_servico/<int:id>', methods=['PUT'])
def update_produto_servico(id):
    item = ProdutoServico.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    data = request.get_json()
    obj = schema.load(data, partial=True)
    for key, value in obj.items():
        setattr(item, key, value)
    db.session.commit()
    return jsonify(schema.dump(item))

@produto_servico_bp.route('/produto_servico/<int:id>', methods=['DELETE'])
def delete_produto_servico(id):
    item = ProdutoServico.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    item.dtdeleted = datetime.utcnow()
    db.session.commit()
    return jsonify({'message': 'Registro excluído (soft delete)'})
