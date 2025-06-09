from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
import os
from dotenv import load_dotenv
from functools import wraps
from app.database import cursor, db

# Carregar variáveis do .env
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

# Criar Blueprint
auth_bp = Blueprint('auth', __name__)

# Middleware de verificação de token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split()[1]

        if not token:
            return jsonify({'msg': 'Token ausente'}), 403

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user_id = data['user_id']
        except:
            return jsonify({'msg': 'Token inválido ou expirado'}), 403

        return f(current_user_id, *args, **kwargs)
    return decorated

# Rota de cadastro

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'msg': 'Preencha todos os campos'}), 400

    # Verifica se usuário já existe
    existing = cursor.execute("SELECT * FROM usuarios WHERE username = ?", (username,)).fetchone()
    if existing:
        return jsonify({'msg': 'Usuário já existe'}), 409

    hashed_password = generate_password_hash(password)
    cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, hashed_password))
    db.commit()
    return jsonify({'msg': 'Usuário cadastrado com sucesso!'}), 201

# Rota de login

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = cursor.execute("SELECT * FROM usuarios WHERE username = ?", (username,)).fetchone()
    if not user or not check_password_hash(user[2], password):
        return jsonify({'msg': 'Credenciais inválidas'}), 401

    # Cria o token
    token = jwt.encode({
        'user_id': user[0],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }, SECRET_KEY, algorithm='HS256')

    return jsonify({'token': token}), 200