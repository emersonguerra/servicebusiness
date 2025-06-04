from flask import Blueprint, request, jsonify
from models import db, Projetos
from schemas import ProjetosSchema
from datetime import datetime

projetos_bp = Blueprint('projetos_bp', __name__)
schema = ProjetosSchema()
schema_many = ProjetosSchema(many=True)

@projetos_bp.route('/projetos', methods=['GET'])
def get_all_projetos():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    query = Projetos.query.filter_by(dtdeleted=None).paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        'items': schema_many.dump(query.items),
        'total': query.total,
        'pages': query.pages,
        'current_page': query.page
    })

@projetos_bp.route('/projetos/<int:id>', methods=['GET'])
def get_projetos(id):
    item = Projetos.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    return jsonify(schema.dump(item))

@projetos_bp.route('/projetos', methods=['POST'])
def create_projetos():
    data = request.get_json()
    obj = schema.load(data)
    novo = Projetos(**obj)
    db.session.add(novo)
    db.session.commit()
    return jsonify(schema.dump(novo)), 201

@projetos_bp.route('/projetos/<int:id>', methods=['PUT'])
def update_projetos(id):
    item = Projetos.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    data = request.get_json()
    obj = schema.load(data, partial=True)
    for key, value in obj.items():
        setattr(item, key, value)
    db.session.commit()
    return jsonify(schema.dump(item))

@projetos_bp.route('/projetos/<int:id>', methods=['DELETE'])
def delete_projetos(id):
    item = Projetos.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    item.dtdeleted = datetime.utcnow()
    db.session.commit()
    return jsonify({'message': 'Registro excluído (soft delete)'})
