from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from petshop_api.database import db, cursor
from petshop_api.models import UserCreate, UserLogin
from petshop_api.auth import gerar_token
from flask_cors import cross_origin

clientes_bp = Blueprint("clientes", __name__)

#rota de cadastro 

@clientes_bp.route("/cadastro", methods=["POST"])
@cross_origin()
def cadastrar_usuario():
    dados = request.get_json()

    try:
        user = UserCreate(**dados)
    except Exception as e:
        return jsonify({"erro": "Dados inválidos"}), 400

    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (user.email,))
    if cursor.fetchone():
        return jsonify({"erro": "Email já cadastrado"}), 400

    senha_hash = generate_password_hash(user.senha)
    cursor.execute(
        "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
        (user.nome, user.email, senha_hash)
    )
    db.commit()

    return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 201

#rotas de login 

@clientes_bp.route("/login", methods=["POST"])
@cross_origin()
def login_usuario():
    dados = request.get_json()

    try:
        user_login = UserLogin(**dados)
    except Exception:
        return jsonify({"erro": "Dados inválidos"}), 400

    cursor.execute("SELECT id, nome, email, senha FROM usuarios WHERE email = ?", (user_login.email,))
    resultado = cursor.fetchone()

    if not resultado:
        return jsonify({"erro": "Email não encontrado"}), 404

    user_id, nome, email, senha_hash = resultado

    if not check_password_hash(senha_hash, user_login.senha):
        return jsonify({"erro": "Senha incorreta"}), 401

    token = gerar_token(user_id)

    return jsonify({
        "mensagem": "Login realizado com sucesso!",
        "token": token,
        "usuario": {
            "id": user_id,
            "nome": nome,
            "email": email
        }
    }), 200