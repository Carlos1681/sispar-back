from flask import Blueprint, request, jsonify
from src.model.reembolso_model import Reembolso
from src.model import db
from flasgger import swag_from
from sqlalchemy import select

bp_reembolso = Blueprint('reembolso', __name__, url_prefix='/reembolso')


@bp_reembolso.route('/solicitar', methods=['POST'])
@swag_from('../docs/reembolso/solicitar.yml')  
def solicitar_reembolso():
    dados = request.get_json()

    try:
        novo_reembolso = Reembolso(
            colaborador=dados['colaborador'],
            empresa=dados['empresa'],
            num_prestacao=dados['num_prestacao'],
            descricao=dados.get('descricao'),
            data=dados['data'],
            tipo_reembolso=dados['tipo_reembolso'],
            centro_custo=dados['centro_custo'],
            ordem_interna=dados.get('ordem_interna'),
            divisao=dados.get('divisao'),
            pep=dados.get('pep'),
            moeda=dados['moeda'],
            distancia_km=dados.get('distancia_km'),
            valor_km=dados.get('valor_km'),
            valor_faturado=dados['valor_faturado'],
            despesa=dados.get('despesa'),
            id_colaborador=dados['id_colaborador'],
            status=dados.get('status', 'Em analise')
        )

        db.session.add(novo_reembolso)
        db.session.commit()

        return jsonify({'mensagem': 'Reembolso solicitado com sucesso'}), 201

    except KeyError as e:
        return jsonify({'erro': f'Campo obrigatório ausente: {str(e)}'}), 400

    except Exception as e:
        return jsonify({'erro': str(e)}), 500


@bp_reembolso.route('/<int:num_prestacao>', methods=['GET'])
def visualizar_reembolso_por_num_prestacao(num_prestacao):
    reembolso = db.session.execute(
        select(Reembolso).where(Reembolso.num_prestacao == num_prestacao)
    ).scalar()

    if not reembolso:
        return jsonify({'mensagem': 'Reembolso não encontrado'}), 404

    return jsonify({
        'id': reembolso.id,
        'colaborador': reembolso.colaborador,
        'empresa': reembolso.empresa,
        'num_prestacao': reembolso.num_prestacao,
        'descricao': reembolso.descricao,
        'data': reembolso.data.isoformat(),
        'tipo_reembolso': reembolso.tipo_reembolso,
        'centro_custo': reembolso.centro_custo,
        'ordem_interna': reembolso.ordem_interna,
        'divisao': reembolso.divisao,
        'pep': reembolso.pep,
        'moeda': reembolso.moeda,
        'distancia_km': reembolso.distancia_km,
        'valor_km': float(reembolso.valor_km) if reembolso.valor_km else None,
        'valor_faturado': float(reembolso.valor_faturado),
        'despesa': float(reembolso.despesa) if reembolso.despesa else None,
        'id_colaborador': reembolso.id_colaborador,
        'status': reembolso.status
    }), 200
