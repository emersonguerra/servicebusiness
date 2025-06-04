from flask import Blueprint, request, jsonify
from models import db, Usuario
from schemas import UsuarioSchema
from datetime import datetime

usuario_bp = Blueprint('usuario_bp', __name__)
schema = UsuarioSchema()
schema_many = UsuarioSchema(many=True)

@usuario_bp.route('/usuario', methods=['GET'])
def get_all_usuario():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    query = Usuario.query.filter_by(dtdeleted=None).paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        'items': schema_many.dump(query.items),
        'total': query.total,
        'pages': query.pages,
        'current_page': query.page
    })

@usuario_bp.route('/usuario/<int:id>', methods=['GET'])
def get_usuario(id):
    item = Usuario.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    return jsonify(schema.dump(item))

@usuario_bp.route('/usuario', methods=['POST'])
def create_usuario():
    data = request.get_json()
    obj = schema.load(data)
    novo = Usuario(**obj)
    db.session.add(novo)
    db.session.commit()
    return jsonify(schema.dump(novo)), 201

@usuario_bp.route('/usuario/<int:id>', methods=['PUT'])
def update_usuario(id):
    item = Usuario.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    data = request.get_json()
    obj = schema.load(data, partial=True)
    for key, value in obj.items():
        setattr(item, key, value)
    db.session.commit()
    return jsonify(schema.dump(item))

@usuario_bp.route('/usuario/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    item = Usuario.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    item.dtdeleted = datetime.utcnow()
    db.session.commit()
    return jsonify({'message': 'Registro excluído (soft delete)'})
