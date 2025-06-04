from flask import Blueprint, request, jsonify
from models import db, ProjetoCentroCustoIndiretos
from schemas import ProjetoCentroCustoIndiretosSchema
from datetime import datetime

projeto_centro_custo_indiretos_bp = Blueprint('projeto_centro_custo_indiretos_bp', __name__)
schema = ProjetoCentroCustoIndiretosSchema()
schema_many = ProjetoCentroCustoIndiretosSchema(many=True)

@projeto_centro_custo_indiretos_bp.route('/projeto_centro_custo_indiretos', methods=['GET'])
def get_all_projeto_centro_custo_indiretos():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    query = ProjetoCentroCustoIndiretos.query.filter_by(dtdeleted=None).paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        'items': schema_many.dump(query.items),
        'total': query.total,
        'pages': query.pages,
        'current_page': query.page
    })

@projeto_centro_custo_indiretos_bp.route('/projeto_centro_custo_indiretos/<int:id>', methods=['GET'])
def get_projeto_centro_custo_indiretos(id):
    item = ProjetoCentroCustoIndiretos.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    return jsonify(schema.dump(item))

@projeto_centro_custo_indiretos_bp.route('/projeto_centro_custo_indiretos', methods=['POST'])
def create_projeto_centro_custo_indiretos():
    data = request.get_json()
    obj = schema.load(data)
    novo = ProjetoCentroCustoIndiretos(**obj)
    db.session.add(novo)
    db.session.commit()
    return jsonify(schema.dump(novo)), 201

@projeto_centro_custo_indiretos_bp.route('/projeto_centro_custo_indiretos/<int:id>', methods=['PUT'])
def update_projeto_centro_custo_indiretos(id):
    item = ProjetoCentroCustoIndiretos.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    data = request.get_json()
    obj = schema.load(data, partial=True)
    for key, value in obj.items():
        setattr(item, key, value)
    db.session.commit()
    return jsonify(schema.dump(item))

@projeto_centro_custo_indiretos_bp.route('/projeto_centro_custo_indiretos/<int:id>', methods=['DELETE'])
def delete_projeto_centro_custo_indiretos(id):
    item = ProjetoCentroCustoIndiretos.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    item.dtdeleted = datetime.utcnow()
    db.session.commit()
    return jsonify({'message': 'Registro excluído (soft delete)'})
