from flask import Blueprint, request, jsonify
from models import db, ColaboradorCentroCusto
from schema import ColaboradorCentroCustoSchema
from datetime import datetime

colaborador_centro_custo_bp = Blueprint('colaborador_centro_custo_bp', __name__)
schema = ColaboradorCentroCustoSchema()
schema_many = ColaboradorCentroCustoSchema(many=True)

@colaborador_centro_custo_bp.route('/colaborador_centro_custo', methods=['GET'])
def get_all_colaborador_centro_custo():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    query = ColaboradorCentroCusto.query.filter_by(dtdeleted=None).paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        'items': schema_many.dump(query.items),
        'total': query.total,
        'pages': query.pages,
        'current_page': query.page
    })

@colaborador_centro_custo_bp.route('/colaborador_centro_custo/<int:id>', methods=['GET'])
def get_colaborador_centro_custo(id):
    item = ColaboradorCentroCusto.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    return jsonify(schema.dump(item))

@colaborador_centro_custo_bp.route('/colaborador_centro_custo', methods=['POST'])
def create_colaborador_centro_custo():
    data = request.get_json()
    obj = schema.load(data)
    novo = ColaboradorCentroCusto(**obj)
    db.session.add(novo)
    db.session.commit()
    return jsonify(schema.dump(novo)), 201

@colaborador_centro_custo_bp.route('/colaborador_centro_custo/<int:id>', methods=['PUT'])
def update_colaborador_centro_custo(id):
    item = ColaboradorCentroCusto.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    data = request.get_json()
    obj = schema.load(data, partial=True)
    for key, value in obj.items():
        setattr(item, key, value)
    db.session.commit()
    return jsonify(schema.dump(item))

@colaborador_centro_custo_bp.route('/colaborador_centro_custo/<int:id>', methods=['DELETE'])
def delete_colaborador_centro_custo(id):
    item = ColaboradorCentroCusto.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    item.dtdeleted = datetime.utcnow()
    db.session.commit()
    return jsonify({'message': 'Registro excluído (soft delete)'})
