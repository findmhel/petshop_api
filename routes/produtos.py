from flask import Blueprint, request, jsonify
from petshop_api import db
from petshop_api.models import Produto

bp = Blueprint('produtos', __name__)

@bp.route('/', methods=['GET'])
def listar_produtos():
    produtos = Produto.query.all()
    return jsonify([{
        "id": p.id,
        "nome": p.nome,
        "categoria": p.categoria,
        "preco": p.preco,
        "estoque": p.estoque
    } for p in produtos])

@bp.route('/', methods=['POST'])
def adicionar_produto():
    data = request.json
    novo = Produto(
        nome=data['nome'],
        categoria=data['categoria'],
        preco=data['preco'],
        estoque=data['estoque']
    )
    db.session.add(novo)
    db.session.commit()
    return jsonify({"mensagem": "Produto adicionado com sucesso."}), 201