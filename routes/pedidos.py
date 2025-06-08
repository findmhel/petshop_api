from flask import Blueprint, request, jsonify
from petshop_api import db
from petshop_api.models import Pedido
from petshop_api.notifications import enviar_mensagem

bp = Blueprint('pedidos', __name__)

@bp.route('/', methods=['POST'])
def realizar_pedido():
    data = request.json
    pedido = Pedido(
        cliente_id=data['cliente_id'],
        produto_id=data['produto_id'],
        quantidade=data['quantidade']
    )
    db.session.add(pedido)
    db.session.commit()

    enviar_mensagem(f"Pedido realizado com sucesso! ID do pedido: {pedido.id}")

    return jsonify({"mensagem": "Pedido registrado com sucesso."}), 201