from flask import Blueprint, request, jsonify
from petshop_api import db
from petshop_api.models import Produto
from app.auth import token_required

bp = Blueprint('produtos', __name__)

@produtos_bp.route('/produtos', methods=['GET'])
@token_required
def listar_produtos(current_user_id):
    produtos = cursor.execute("SELECT * FROM produtos").fetchall()
    return jsonify([{'id': p[0], 'nome': p[1], 'preco': p[2]} for p in produtos])

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

