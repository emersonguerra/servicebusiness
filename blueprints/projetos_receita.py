from flask import Blueprint, request, jsonify
from models import db, ProjetosReceita
from schemas import ProjetosReceitaSchema
from datetime import datetime

projetos_receita_bp = Blueprint('projetos_receita_bp', __name__)
schema = ProjetosReceitaSchema()
schema_many = ProjetosReceitaSchema(many=True)

@projetos_receita_bp.route('/projetos_receita', methods=['GET'])
def get_all_projetos_receita():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    query = ProjetosReceita.query.filter_by(dtdeleted=None).paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        'items': schema_many.dump(query.items),
        'total': query.total,
        'pages': query.pages,
        'current_page': query.page
    })

@projetos_receita_bp.route('/projetos_receita/<int:id>', methods=['GET'])
def get_projetos_receita(id):
    item = ProjetosReceita.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    return jsonify(schema.dump(item))

@projetos_receita_bp.route('/projetos_receita', methods=['POST'])
def create_projetos_receita():
    data = request.get_json()
    obj = schema.load(data)
    novo = ProjetosReceita(**obj)
    db.session.add(novo)
    db.session.commit()
    return jsonify(schema.dump(novo)), 201

@projetos_receita_bp.route('/projetos_receita/<int:id>', methods=['PUT'])
def update_projetos_receita(id):
    item = ProjetosReceita.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    data = request.get_json()
    obj = schema.load(data, partial=True)
    for key, value in obj.items():
        setattr(item, key, value)
    db.session.commit()
    return jsonify(schema.dump(item))

@projetos_receita_bp.route('/projetos_receita/<int:id>', methods=['DELETE'])
def delete_projetos_receita(id):
    item = ProjetosReceita.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    item.dtdeleted = datetime.utcnow()
    db.session.commit()
    return jsonify({'message': 'Registro excluído (soft delete)'})
