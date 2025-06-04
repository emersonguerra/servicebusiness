from flask import Blueprint, request, jsonify
from models import db, CentroCusto
from schemas import CentroCustoSchema
from datetime import datetime

centro_custo_bp = Blueprint('centro_custo_bp', __name__)
schema = CentroCustoSchema()
schema_many = CentroCustoSchema(many=True)

@centro_custo_bp.route('/centro_custo', methods=['GET'])
def get_all_centro_custo():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    query = CentroCusto.query.filter_by(dtdeleted=None).paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        'items': schema_many.dump(query.items),
        'total': query.total,
        'pages': query.pages,
        'current_page': query.page
    })

@centro_custo_bp.route('/centro_custo/<int:id>', methods=['GET'])
def get_centro_custo(id):
    item = CentroCusto.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    return jsonify(schema.dump(item))

@centro_custo_bp.route('/centro_custo', methods=['POST'])
def create_centro_custo():
    data = request.get_json()
    obj = schema.load(data)
    novo = CentroCusto(**obj)
    db.session.add(novo)
    db.session.commit()
    return jsonify(schema.dump(novo)), 201

@centro_custo_bp.route('/centro_custo/<int:id>', methods=['PUT'])
def update_centro_custo(id):
    item = CentroCusto.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    data = request.get_json()
    obj = schema.load(data, partial=True)
    for key, value in obj.items():
        setattr(item, key, value)
    db.session.commit()
    return jsonify(schema.dump(item))

@centro_custo_bp.route('/centro_custo/<int:id>', methods=['DELETE'])
def delete_centro_custo(id):
    item = CentroCusto.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    item.dtdeleted = datetime.utcnow()
    db.session.commit()
    return jsonify({'message': 'Registro excluído (soft delete)'})
