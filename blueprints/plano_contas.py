from flask import Blueprint, request, jsonify
from models import db, PlanoContas
from schemas import PlanoContasSchema
from datetime import datetime

plano_contas_bp = Blueprint('plano_contas', __name__, template_folder='plano_contas')
schema = PlanoContasSchema()
schema_many = PlanoContasSchema(many=True)

@plano_contas_bp.route('/')
def index():
    planocontas = planocontas.query.all()
    return render_template("crud_plano_contas.html", plano_contas=planocontas)


@plano_contas_bp.route('/plano_contas', methods=['GET'])
def get_all_plano_contas():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    query = PlanoContas.query.filter_by(dtdeleted=None).paginate(page=page, per_page=per_page, error_out=False)
    return jsonify({
        'items': schema_many.dump(query.items),
        'total': query.total,
        'pages': query.pages,
        'current_page': query.page
    })

@plano_contas_bp.route('/plano_contas/<int:id>', methods=['GET'])
def get_plano_contas(id):
    item = PlanoContas.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    return jsonify(schema.dump(item))

@plano_contas_bp.route('/plano_contas', methods=['POST'])
def create_plano_contas():
    data = request.get_json()
    obj = schema.load(data)
    novo = PlanoContas(**obj)
    db.session.add(novo)
    db.session.commit()
    return jsonify(schema.dump(novo)), 201

@plano_contas_bp.route('/plano_contas/<int:id>', methods=['PUT'])
def update_plano_contas(id):
    item = PlanoContas.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    data = request.get_json()
    obj = schema.load(data, partial=True)
    for key, value in obj.items():
        setattr(item, key, value)
    db.session.commit()
    return jsonify(schema.dump(item))

@plano_contas_bp.route('/plano_contas/<int:id>', methods=['DELETE'])
def delete_plano_contas(id):
    item = PlanoContas.query.filter_by(id=id, dtdeleted=None).first()
    if not item:
        return jsonify({'message': 'Registro não encontrado'}), 404
    item.dtdeleted = datetime.utcnow()
    db.session.commit()
    return jsonify({'message': 'Registro excluído (soft delete)'})
