from flask import Blueprint, request, jsonify
from models import db, TipoConta
from schemas import TipoContaSchema
from datetime import datetime

tipo_conta_bp = Blueprint('tipo_conta_bp', __name__)
schema = TipoContaSchema()
schema_many = TipoContaSchema(many=True)

@tipo_conta_bp.route('/tipo_conta', methods=['GET'])
def get_all_tipo_conta():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    query = TipoConta.query.filter_by(dtdeleted=None).paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        'items': schema_many.dump(query.items),
        'total': query.total,
        'pages': query.pages,
        'current_page': query.page
    })

@tipo_conta_bp.route('/tipo_conta/<int:id>', methods=['GET'])
def get_tipo_conta(id):
    item = TipoConta.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    return jsonify(schema.dump(item))

@tipo_conta_bp.route('/tipo_conta', methods=['POST'])
def create_tipo_conta():
    data = request.get_json()
    obj = schema.load(data)
    novo = TipoConta(**obj)
    db.session.add(novo)
    db.session.commit()
    return jsonify(schema.dump(novo)), 201

@tipo_conta_bp.route('/tipo_conta/<int:id>', methods=['PUT'])
def update_tipo_conta(id):
    item = TipoConta.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    data = request.get_json()
    obj = schema.load(data, partial=True)
    for key, value in obj.items():
        setattr(item, key, value)
    db.session.commit()
    return jsonify(schema.dump(item))

@tipo_conta_bp.route('/tipo_conta/<int:id>', methods=['DELETE'])
def delete_tipo_conta(id):
    item = TipoConta.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    item.dtdeleted = datetime.utcnow()
    db.session.commit()
    return jsonify({'message': 'Registro excluído (soft delete)'})
