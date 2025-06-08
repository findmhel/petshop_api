from flask import Blueprint, request, jsonify
from petshop_api import db
from petshop_api.models import BanhoTosa
from petshop_api.notifications import enviar_mensagem

bp = Blueprint('banho_tosa', __name__)

@bp.route('/', methods=['POST'])
def agendar_banho_tosa():
    data = request.json
    agendamento = BanhoTosa(
        cliente_id=data['cliente_id'],
        tipo_servico=data['tipo_servico'],
        data=data['data'],
        hora=data['hora']
    )
    db.session.add(agendamento)
    db.session.commit()

    enviar_mensagem(f"{data['tipo_servico']} agendado para {data['data']} às {data['hora']}.")

    return jsonify({"mensagem": "Agendamento realizado com sucesso."}), 201