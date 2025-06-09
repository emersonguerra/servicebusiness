#@ rotas CRUD


# rotas.py
from flask import Flask, request, jsonify
from flask_login import login_required, current_user
from datetime import datetime

# Importações dos modelos e schemas
from models import (db, TipoColaborador, Colaborador, ColaboradorCentroCusto, 
                    TipoCentroCusto, CentroCusto, TipoConta, PlanoContas, 
                    PlanoContasCentroCusto, ProjetoCentroCustoIndiretos, 
                    TipoProdutoServico, ProdutoServico, Projetos, 
                    ProjetosReceita, ProjetosEsforco)
from schemas import (TipoColaboradorSchema, ColaboradorSchema, ColaboradorCentroCustoSchema, 
                     TipoCentroCustoSchema, CentroCustoSchema, TipoContaSchema, PlanoContasSchema, 
                     PlanoContasCentroCustoSchema, ProjetoCentroCustoIndiretosSchema, 
                     TipoProdutoServicoSchema, ProdutoServicoSchema, ProjetosSchema, 
                     ProjetosReceitaSchema, ProjetosEsforcoSchema)

# Instâncias dos schemas para operações singulares e múltiplas
tipo_colaborador_schema = TipoColaboradorSchema()
tipos_colaborador_schema = TipoColaboradorSchema(many=True)

colaborador_schema = ColaboradorSchema()
colaboradores_schema = ColaboradorSchema(many=True)

colaborador_centrocusto_schema = ColaboradorCentroCustoSchema()
colaborador_centrocustos_schema = ColaboradorCentroCustoSchema(many=True)

tipo_centro_custo_schema = TipoCentroCustoSchema()
tipos_centro_custo_schema = TipoCentroCustoSchema(many=True)

centro_custo_schema = CentroCustoSchema()
centros_custo_schema = CentroCustoSchema(many=True)

tipo_conta_schema = TipoContaSchema()
tipos_conta_schema = TipoContaSchema(many=True)

plano_contas_schema = PlanoContasSchema()
planos_contas_schema = PlanoContasSchema(many=True)

plano_contas_centrocusto_schema = PlanoContasCentroCustoSchema()
planos_contas_centrocusto_schema = PlanoContasCentroCustoSchema(many=True)

projeto_centrocusto_indiretos_schema = ProjetoCentroCustoIndiretosSchema()
projetos_centrocusto_indiretos_schema = ProjetoCentroCustoIndiretosSchema(many=True)

tipo_produto_servico_schema = TipoProdutoServicoSchema()
tipos_produto_servico_schema = TipoProdutoServicoSchema(many=True)

produto_servico_schema = ProdutoServicoSchema()
produtos_servico_schema = ProdutoServicoSchema(many=True)

projetos_schema = ProjetosSchema()
projetos_list_schema = ProjetosSchema(many=True)

projetos_receita_schema = ProjetosReceitaSchema()
projetos_receitas_schema = ProjetosReceitaSchema(many=True)

projetos_esforco_schema = ProjetosEsforcoSchema()
projetos_esforcos_schema = ProjetosEsforcoSchema(many=True)

app = Flask(__name__)

# -------------------------------------------------------------
# 1. TipoColaborador
# -------------------------------------------------------------
@app.route('/tipo_colaboradores', methods=['GET'])
@login_required
def listar_tipo_colaboradores():
    try:
        tipos = TipoColaborador.query.all()
        result = tipos_colaborador_schema.dump(tipos)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tipo_colaboradores/<int:id>', methods=['GET'])
@login_required
def obter_tipo_colaborador(id):
    try:
        tipo = TipoColaborador.query.get_or_404(id)
        result = tipo_colaborador_schema.dump(tipo)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tipo_colaboradores', methods=['POST'])
@login_required
def criar_tipo_colaborador():
    try:
        data = request.get_json()
        novo_tipo = tipo_colaborador_schema.load(data)
        tipo = TipoColaborador(**novo_tipo)
        db.session.add(tipo)
        db.session.commit()
        return jsonify(tipo_colaborador_schema.dump(tipo)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/tipo_colaboradores/<int:id>', methods=['PUT'])
@login_required
def atualizar_tipo_colaborador(id):
    try:
        tipo = TipoColaborador.query.get_or_404(id)
        data = request.get_json()
        updated_data = tipo_colaborador_schema.load(data, partial=True)
        for key, value in updated_data.items():
            setattr(tipo, key, value)
        db.session.commit()
        return jsonify(tipo_colaborador_schema.dump(tipo)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/tipo_colaboradores/<int:id>', methods=['DELETE'])
@login_required
def deletar_tipo_colaborador(id):
    try:
        tipo = TipoColaborador.query.get_or_404(id)
        db.session.delete(tipo)
        db.session.commit()
        return jsonify({'message': 'Excluído com sucesso'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# -------------------------------------------------------------
# 2. Colaborador
# -------------------------------------------------------------
@app.route('/colaboradores', methods=['GET'])
@login_required
def listar_colaboradores():
    try:
        colaboradores = Colaborador.query.all()
        result = colaboradores_schema.dump(colaboradores)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/colaboradores/<int:id>', methods=['GET'])
@login_required
def obter_colaborador(id):
    try:
        colaborador = Colaborador.query.get_or_404(id)
        result = colaborador_schema.dump(colaborador)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/colaboradores', methods=['POST'])
@login_required
def criar_colaborador():
    try:
        data = request.get_json()
        novo = colaborador_schema.load(data)
        colaborador = Colaborador(**novo)
        db.session.add(colaborador)
        db.session.commit()
        return jsonify(colaborador_schema.dump(colaborador)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/colaboradores/<int:id>', methods=['PUT'])
@login_required
def atualizar_colaborador(id):
    try:
        colaborador = Colaborador.query.get_or_404(id)
        data = request.get_json()
        updated_data = colaborador_schema.load(data, partial=True)
        for key, value in updated_data.items():
            setattr(colaborador, key, value)
        db.session.commit()
        return jsonify(colaborador_schema.dump(colaborador)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/colaboradores/<int:id>', methods=['DELETE'])
@login_required
def deletar_colaborador(id):
    try:
        colaborador = Colaborador.query.get_or_404(id)
        db.session.delete(colaborador)
        db.session.commit()
        return jsonify({'message': 'Excluído com sucesso'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# -------------------------------------------------------------
# 3. ColaboradorCentroCusto
# -------------------------------------------------------------
@app.route('/colaborador_centrocustos', methods=['GET'])
@login_required
def listar_colaborador_centrocustos():
    try:
        registros = ColaboradorCentroCusto.query.all()
        result = colaborador_centrocustos_schema.dump(registros)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/colaborador_centrocustos/<int:id>', methods=['GET'])
@login_required
def obter_colaborador_centrocusto(id):
    try:
        registro = ColaboradorCentroCusto.query.get_or_404(id)
        result = colaborador_centrocusto_schema.dump(registro)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/colaborador_centrocustos', methods=['POST'])
@login_required
def criar_colaborador_centrocusto():
    try:
        data = request.get_json()
        novo_registro = colaborador_centrocusto_schema.load(data)
        registro = ColaboradorCentroCusto(**novo_registro)
        db.session.add(registro)
        db.session.commit()
        return jsonify(colaborador_centrocusto_schema.dump(registro)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/colaborador_centrocustos/<int:id>', methods=['PUT'])
@login_required
def atualizar_colaborador_centrocusto(id):
    try:
        registro = ColaboradorCentroCusto.query.get_or_404(id)
        data = request.get_json()
        updated_data = colaborador_centrocusto_schema.load(data, partial=True)
        for key, value in updated_data.items():
            setattr(registro, key, value)
        db.session.commit()
        return jsonify(colaborador_centrocusto_schema.dump(registro)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/colaborador_centrocustos/<int:id>', methods=['DELETE'])
@login_required
def deletar_colaborador_centrocusto(id):
    try:
        registro = ColaboradorCentroCusto.query.get_or_404(id)
        db.session.delete(registro)
        db.session.commit()
        return jsonify({'message': 'Excluído com sucesso'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# -------------------------------------------------------------
# 4. TipoCentroCusto
# -------------------------------------------------------------
@app.route('/tipos_centro_custo', methods=['GET'])
@login_required
def listar_tipos_centro_custo():
    try:
        tipos = TipoCentroCusto.query.all()
        result = tipos_centro_custo_schema.dump(tipos)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tipos_centro_custo/<int:id>', methods=['GET'])
@login_required
def obter_tipo_centro_custo(id):
    try:
        tipo = TipoCentroCusto.query.get_or_404(id)
        result = tipo_centro_custo_schema.dump(tipo)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tipos_centro_custo', methods=['POST'])
@login_required
def criar_tipo_centro_custo():
    try:
        data = request.get_json()
        novo_tipo = tipo_centro_custo_schema.load(data)
        tipo = TipoCentroCusto(**novo_tipo)
        db.session.add(tipo)
        db.session.commit()
        return jsonify(tipo_centro_custo_schema.dump(tipo)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/tipos_centro_custo/<int:id>', methods=['PUT'])
@login_required
def atualizar_tipo_centro_custo(id):
    try:
        tipo = TipoCentroCusto.query.get_or_404(id)
        data = request.get_json()
        updated_data = tipo_centro_custo_schema.load(data, partial=True)
        for key, value in updated_data.items():
            setattr(tipo, key, value)
        db.session.commit()
        return jsonify(tipo_centro_custo_schema.dump(tipo)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/tipos_centro_custo/<int:id>', methods=['DELETE'])
@login_required
def deletar_tipo_centro_custo(id):
    try:
        tipo = TipoCentroCusto.query.get_or_404(id)
        db.session.delete(tipo)
        db.session.commit()
        return jsonify({'message': 'Excluído com sucesso'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# -------------------------------------------------------------
# 5. CentroCusto
# -------------------------------------------------------------
@app.route('/centros_custo', methods=['GET'])
@login_required
def listar_centros_custo():
    try:
        centros = CentroCusto.query.all()
        result = centros_custo_schema.dump(centros)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/centros_custo/<int:id>', methods=['GET'])
@login_required
def obter_centro_custo(id):
    try:
        centro = CentroCusto.query.get_or_404(id)
        result = centro_custo_schema.dump(centro)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/centros_custo', methods=['POST'])
@login_required
def criar_centro_custo():
    try:
        data = request.get_json()
        novo = centro_custo_schema.load(data)
        centro = CentroCusto(**novo)
        db.session.add(centro)
        db.session.commit()
        return jsonify(centro_custo_schema.dump(centro)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/centros_custo/<int:id>', methods=['PUT'])
@login_required
def atualizar_centro_custo(id):
    try:
        centro = CentroCusto.query.get_or_404(id)
        data = request.get_json()
        updated_data = centro_custo_schema.load(data, partial=True)
        for key, value in updated_data.items():
            setattr(centro, key, value)
        db.session.commit()
        return jsonify(centro_custo_schema.dump(centro)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/centros_custo/<int:id>', methods=['DELETE'])
@login_required
def deletar_centro_custo(id):
    try:
        centro = CentroCusto.query.get_or_404(id)
        db.session.delete(centro)
        db.session.commit()
        return jsonify({'message': 'Excluído com sucesso'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# -------------------------------------------------------------
# 6. TipoConta
# -------------------------------------------------------------
@app.route('/tipos_conta', methods=['GET'])
@login_required
def listar_tipos_conta():
    try:
        tipos = TipoConta.query.all()
        result = tipos_conta_schema.dump(tipos)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tipos_conta/<int:id>', methods=['GET'])
@login_required
def obter_tipo_conta(id):
    try:
        tipo = TipoConta.query.get_or_404(id)
        result = tipo_conta_schema.dump(tipo)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tipos_conta', methods=['POST'])
@login_required
def criar_tipo_conta():
    try:
        data = request.get_json()
        novo = tipo_conta_schema.load(data)
        tipo = TipoConta(**novo)
        db.session.add(tipo)
        db.session.commit()
        return jsonify(tipo_conta_schema.dump(tipo)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/tipos_conta/<int:id>', methods=['PUT'])
@login_required
def atualizar_tipo_conta(id):
    try:
        tipo = TipoConta.query.get_or_404(id)
        data = request.get_json()
        updated_data = tipo_conta_schema.load(data, partial=True)
        for key, value in updated_data.items():
            setattr(tipo, key, value)
        db.session.commit()
        return jsonify(tipo_conta_schema.dump(tipo)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/tipos_conta/<int:id>', methods=['DELETE'])
@login_required
def deletar_tipo_conta(id):
    try:
        tipo = TipoConta.query.get_or_404(id)
        db.session.delete(tipo)
        db.session.commit()
        return jsonify({'message': 'Excluído com sucesso'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# -------------------------------------------------------------
# 7. PlanoContas
# -------------------------------------------------------------
@app.route('/planos_contas', methods=['GET'])
@login_required
def listar_planos_contas():
    try:
        planos = PlanoContas.query.all()
        result = planos_contas_schema.dump(planos)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/planos_contas/<int:id>', methods=['GET'])
@login_required
def obter_plano_contas(id):
    try:
        plano = PlanoContas.query.get_or_404(id)
        result = plano_contas_schema.dump(plano)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/planos_contas', methods=['POST'])
@login_required
def criar_plano_contas():
    try:
        data = request.get_json()
        novo = plano_contas_schema.load(data)
        plano = PlanoContas(**novo)
        db.session.add(plano)
        db.session.commit()
        return jsonify(plano_contas_schema.dump(plano)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/planos_contas/<int:id>', methods=['PUT'])
@login_required
def atualizar_plano_contas(id):
    try:
        plano = PlanoContas.query.get_or_404(id)
        data = request.get_json()
        updated_data = plano_contas_schema.load(data, partial=True)
        for key, value in updated_data.items():
            setattr(plano, key, value)
        db.session.commit()
        return jsonify(plano_contas_schema.dump(plano)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/planos_contas/<int:id>', methods=['DELETE'])
@login_required
def deletar_plano_contas(id):
    try:
        plano = PlanoContas.query.get_or_404(id)
        db.session.delete(plano)
        db.session.commit()
        return jsonify({'message': 'Excluído com sucesso'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# -------------------------------------------------------------
# 8. PlanoContasCentroCusto
# -------------------------------------------------------------
@app.route('/planos_contas_centrocusto', methods=['GET'])
@login_required
def listar_planos_contas_centrocusto():
    try:
        registros = PlanoContasCentroCusto.query.all()
        result = planos_contas_centrocusto_schema.dump(registros)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/planos_contas_centrocusto/<int:id>', methods=['GET'])
@login_required
def obter_plano_contas_centrocusto(id):
    try:
        registro = PlanoContasCentroCusto.query.get_or_404(id)
        result = plano_contas_centrocusto_schema.dump(registro)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/planos_contas_centrocusto', methods=['POST'])
@login_required
def criar_plano_contas_centrocusto():
    try:
        data = request.get_json()
        novo = plano_contas_centrocusto_schema.load(data)
        registro = PlanoContasCentroCusto(**novo)
        db.session.add(registro)
        db.session.commit()
        return jsonify(plano_contas_centrocusto_schema.dump(registro)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/planos_contas_centrocusto/<int:id>', methods=['PUT'])
@login_required
def atualizar_plano_contas_centrocusto(id):
    try:
        registro = PlanoContasCentroCusto.query.get_or_404(id)
        data = request.get_json()
        updated_data = plano_contas_centrocusto_schema.load(data, partial=True)
        for key, value in updated_data.items():
            setattr(registro, key, value)
        db.session.commit()
        return jsonify(plano_contas_centrocusto_schema.dump(registro)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/planos_contas_centrocusto/<int:id>', methods=['DELETE'])
@login_required
def deletar_plano_contas_centrocusto(id):
    try:
        registro = PlanoContasCentroCusto.query.get_or_404(id)
        db.session.delete(registro)
        db.session.commit()
        return jsonify({'message': 'Excluído com sucesso'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# -------------------------------------------------------------
# 9. ProjetoCentroCustoIndiretos
# -------------------------------------------------------------
@app.route('/projetos_centrocusto_indiretos', methods=['GET'])
@login_required
def listar_projetos_centrocusto_indiretos():
    try:
        registros = ProjetoCentroCustoIndiretos.query.all()
        result = projetos_centrocusto_indiretos_schema.dump(registros)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projetos_centrocusto_indiretos/<int:id>', methods=['GET'])
@login_required
def obter_projeto_centrocusto_indiretos(id):
    try:
        registro = ProjetoCentroCustoIndiretos.query.get_or_404(id)
        result = projeto_centrocusto_indiretos_schema.dump(registro)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projetos_centrocusto_indiretos', methods=['POST'])
@login_required
def criar_projeto_centrocusto_indiretos():
    try:
        data = request.get_json()
        novo = projeto_centrocusto_indiretos_schema.load(data)
        registro = ProjetoCentroCustoIndiretos(**novo)
        db.session.add(registro)
        db.session.commit()
        return jsonify(projeto_centrocusto_indiretos_schema.dump(registro)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/projetos_centrocusto_indiretos/<int:id>', methods=['PUT'])
@login_required
def atualizar_projeto_centrocusto_indiretos(id):
    try:
        registro = ProjetoCentroCustoIndiretos.query.get_or_404(id)
        data = request.get_json()
        updated_data = projeto_centrocusto_indiretos_schema.load(data, partial=True)
        for key, value in updated_data.items():
            setattr(registro, key, value)
        db.session.commit()
        return jsonify(projeto_centrocusto_indiretos_schema.dump(registro)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/projetos_centrocusto_indiretos/<int:id>', methods=['DELETE'])
@login_required
def deletar_projeto_centrocusto_indiretos(id):
    try:
        registro = ProjetoCentroCustoIndiretos.query.get_or_404(id)
        db.session.delete(registro)
        db.session.commit()
        return jsonify({'message': 'Excluído com sucesso'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# -------------------------------------------------------------
# 10. TipoProdutoServico
# -------------------------------------------------------------
@app.route('/tipos_produto_servico', methods=['GET'])
@login_required
def listar_tipos_produto_servico():
    try:
        tipos = TipoProdutoServico.query.all()
        result = tipos_produto_servico_schema.dump(tipos)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tipos_produto_servico/<int:id>', methods=['GET'])
@login_required
def obter_tipo_produto_servico(id):
    try:
        tipo = TipoProdutoServico.query.get_or_404(id)
        result = tipo_produto_servico_schema.dump(tipo)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/tipos_produto_servico', methods=['POST'])
@login_required
def criar_tipo_produto_servico():
    try:
        data = request.get_json()
        novo = tipo_produto_servico_schema.load(data)
        tipo = TipoProdutoServico(**novo)
        db.session.add(tipo)
        db.session.commit()
        return jsonify(tipo_produto_servico_schema.dump(tipo)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/tipos_produto_servico/<int:id>', methods=['PUT'])
@login_required
def atualizar_tipo_produto_servico(id):
    try:
        tipo = TipoProdutoServico.query.get_or_404(id)
        data = request.get_json()
        updated_data = tipo_produto_servico_schema.load(data, partial=True)
        for key, value in updated_data.items():
            setattr(tipo, key, value)
        db.session.commit()
        return jsonify(tipo_produto_servico_schema.dump(tipo)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/tipos_produto_servico/<int:id>', methods=['DELETE'])
@login_required
def deletar_tipo_produto_servico(id):
    try:
        tipo = TipoProdutoServico.query.get_or_404(id)
        db.session.delete(tipo)
        db.session.commit()
        return jsonify({'message': 'Excluído com sucesso'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# -------------------------------------------------------------
# 11. ProdutoServico
# -------------------------------------------------------------
@app.route('/produtos_servico', methods=['GET'])
@login_required
def listar_produtos_servico():
    try:
        produtos = ProdutoServico.query.all()
        result = produtos_servico_schema.dump(produtos)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/produtos_servico/<int:id>', methods=['GET'])
@login_required
def obter_produto_servico(id):
    try:
        produto = ProdutoServico.query.get_or_404(id)
        result = produto_servico_schema.dump(produto)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/produtos_servico', methods=['POST'])
@login_required
def criar_produto_servico():
    try:
        data = request.get_json()
        novo = produto_servico_schema.load(data)
        produto = ProdutoServico(**novo)
        db.session.add(produto)
        db.session.commit()
        return jsonify(produto_servico_schema.dump(produto)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/produtos_servico/<int:id>', methods=['PUT'])
@login_required
def atualizar_produto_servico(id):
    try:
        produto = ProdutoServico.query.get_or_404(id)
        data = request.get_json()
        updated_data = produto_servico_schema.load(data, partial=True)
        for key, value in updated_data.items():
            setattr(produto, key, value)
        db.session.commit()
        return jsonify(produto_servico_schema.dump(produto)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/produtos_servico/<int:id>', methods=['DELETE'])
@login_required
def deletar_produto_servico(id):
    try:
        produto = ProdutoServico.query.get_or_404(id)
        db.session.delete(produto)
        db.session.commit()
        return jsonify({'message': 'Excluído com sucesso'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# -------------------------------------------------------------
# 12. Projetos
# -------------------------------------------------------------
@app.route('/projetos', methods=['GET'])
@login_required
def listar_projetos():
    try:
        projetos = Projetos.query.all()
        result = projetos_list_schema.dump(projetos)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projetos/<int:id>', methods=['GET'])
@login_required
def obter_projeto(id):
    try:
        projeto = Projetos.query.get_or_404(id)
        result = projetos_schema.dump(projeto)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projetos', methods=['POST'])
@login_required
def criar_projeto():
    try:
        data = request.get_json()
        novo = projetos_schema.load(data)
        projeto = Projetos(**novo)
        db.session.add(projeto)
        db.session.commit()
        return jsonify(projetos_schema.dump(projeto)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/projetos/<int:id>', methods=['PUT'])
@login_required
def atualizar_projeto(id):
    try:
        projeto = Projetos.query.get_or_404(id)
        data = request.get_json()
        updated_data = projetos_schema.load(data, partial=True)
        for key, value in updated_data.items():
            setattr(projeto, key, value)
        db.session.commit()
        return jsonify(projetos_schema.dump(projeto)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/projetos/<int:id>', methods=['DELETE'])
@login_required
def deletar_projeto(id):
    try:
        projeto = Projetos.query.get_or_404(id)
        db.session.delete(projeto)
        db.session.commit()
        return jsonify({'message': 'Excluído com sucesso'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# -------------------------------------------------------------
# 13. ProjetosReceita
# -------------------------------------------------------------
@app.route('/projetos_receita', methods=['GET'])
@login_required
def listar_projetos_receita():
    try:
        receitas = ProjetosReceita.query.all()
        result = projetos_receitas_schema.dump(receitas)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projetos_receita/<int:id>', methods=['GET'])
@login_required
def obter_projetos_receita(id):
    try:
        receita = ProjetosReceita.query.get_or_404(id)
        result = projetos_receita_schema.dump(receita)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projetos_receita', methods=['POST'])
@login_required
def criar_projetos_receita():
    try:
        data = request.get_json()
        novo = projetos_receita_schema.load(data)
        receita = ProjetosReceita(**novo)
        db.session.add(receita)
        db.session.commit()
        return jsonify(projetos_receita_schema.dump(receita)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/projetos_receita/<int:id>', methods=['PUT'])
@login_required
def atualizar_projetos_receita(id):
    try:
        receita = ProjetosReceita.query.get_or_404(id)
        data = request.get_json()
        updated_data = projetos_receita_schema.load(data, partial=True)
        for key, value in updated_data.items():
            setattr(receita, key, value)
        db.session.commit()
        return jsonify(projetos_receita_schema.dump(receita)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/projetos_receita/<int:id>', methods=['DELETE'])
@login_required
def deletar_projetos_receita(id):
    try:
        receita = ProjetosReceita.query.get_or_404(id)
        db.session.delete(receita)
        db.session.commit()
        return jsonify({'message': 'Excluído com sucesso'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# -------------------------------------------------------------
# 14. ProjetosEsforco
# -------------------------------------------------------------
@app.route('/projetos_esforco', methods=['GET'])
@login_required
def listar_projetos_esforco():
    try:
        esforcos = ProjetosEsforco.query.all()
        result = projetos_esforcos_schema.dump(esforcos)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projetos_esforco/<int:id>', methods=['GET'])
@login_required
def obter_projetos_esforco(id):
    try:
        esforco = ProjetosEsforco.query.get_or_404(id)
        result = projetos_esforco_schema.dump(esforco)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/projetos_esforco', methods=['POST'])
@login_required
def criar_projetos_esforco():
    try:
        data = request.get_json()
        novo = projetos_esforco_schema.load(data)
        esforco = ProjetosEsforco(**novo)
        db.session.add(esforco)
        db.session.commit()
        return jsonify(projetos_esforco_schema.dump(esforco)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/projetos_esforco/<int:id>', methods=['PUT'])
@login_required
def atualizar_projetos_esforco(id):
    try:
        esforco = ProjetosEsforco.query.get_or_404(id)
        data = request.get_json()
        updated_data = projetos_esforco_schema.load(data, partial=True)
        for key, value in updated_data.items():
            setattr(esforco, key, value)
        db.session.commit()
        return jsonify(projetos_esforco_schema.dump(esforco)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/projetos_esforco/<int:id>', methods=['DELETE'])
@login_required
def deletar_projetos_esforco(id):
    try:
        esforco = ProjetosEsforco.query.get_or_404(id)
        db.session.delete(esforco)
        db.session.commit()
        return jsonify({'message': 'Excluído com sucesso'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# -------------------------------------------------------------
# 15. Usuário (Gerenciamento de Usuários)
# -------------------------------------------------------------
# Removido import duplicado: from flask_login

@app.route('/usuarios', methods=['GET'])
@login_required
def listar_usuarios():
    if current_user.role != 'admin':
        return jsonify({'message': 'Acesso negado'}), 403
    try:
        usuarios = Usuario.query.all()
        result = usuario_schema.dump(usuarios, many=True)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/usuarios/<int:id>', methods=['GET'])
@login_required
def obter_usuario(id):
    if current_user.role != 'admin':
        return jsonify({'message': 'Acesso negado'}), 403
    try:
        usuario = Usuario.query.get_or_404(id)
        result = usuario_schema.dump(usuario)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/usuarios', methods=['POST'])
@login_required
def criar_usuario():
    if current_user.role != 'admin':
        return jsonify({'message': 'Acesso negado'}), 403
    try:
        data = request.get_json()
        novo = usuario_schema.load(data)
        usuario = Usuario(**novo)
        db.session.add(usuario)
        db.session.commit()
        return jsonify(usuario_schema.dump(usuario)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/usuarios/<int:id>', methods=['PUT'])
@login_required
def atualizar_usuario(id):
    if current_user.role != 'admin':
        return jsonify({'message': 'Acesso negado'}), 403
    try:
        usuario = Usuario.query.get_or_404(id)
        data = request.get_json()
        updated_data = usuario_schema.load(data, partial=True)
        for key, value in updated_data.items():
            setattr(usuario, key, value)
        db.session.commit()
        return jsonify(usuario_schema.dump(usuario)), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/usuarios/<int:id>', methods=['DELETE'])
@login_required
def deletar_usuario(id):
    if current_user.role != 'admin':
        return jsonify({'message': 'Acesso negado'}), 403
    try:
        usuario = Usuario.query.get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return jsonify({'message': 'Excluído com sucesso'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# -------------------------------------------------------------
# 16. Recuperação de Senha
# -------------------------------------------------------------
@app.route('/recuperar_senha', methods=['POST'])
def recuperar_senha():
    try:
        data = request.get_json()
        email = data.get('email')
        usuario = Usuario.query.filter_by(email=email).first()
        if usuario:
            token = generate_token()  # Função para gerar um token único
            usuario.reset_token = token
            db.session.commit()
            enviar_email_redefinicao(usuario.email, token)  # Função para enviar o e-mail de recuperação
            return jsonify({'message': 'E-mail de recuperação enviado'}), 200
        return jsonify({'message': 'Usuário não encontrado'}), 404
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# -------------------------------------------------------------
# 17. Redefinição de Senha
# -------------------------------------------------------------
@app.route('/redefinir_senha/<token>', methods=['POST'])
def redefinir_senha(token):
    try:
        data = request.get_json()
        nova_senha = data.get('nova_senha')
        usuario = Usuario.query.filter_by(reset_token=token).first()
        if usuario:
            usuario.senha = hash_password(nova_senha)  # Função para gerar o hash da nova senha
            usuario.reset_token = None
            db.session.commit()
            return jsonify({'message': 'Senha redefinida com sucesso'}), 200
        return jsonify({'message': 'Token inválido'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400