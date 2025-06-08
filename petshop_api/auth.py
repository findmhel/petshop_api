from datetime import datetime, timedelta
from flask import request, jsonify
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "segredo")

def create_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=3)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def token_required(f):
    def decorator(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            bearer = request.headers['Authorization']
            token = bearer.split()[1] if len(bearer.split()) > 1 else None
        if not token:
            return jsonify({'mensagem': 'Token ausente!'}), 401
        user_id = decode_token(token)
        if not user_id:
            return jsonify({'mensagem': 'Token inválido!'}), 401
        return f(user_id, *args, **kwargs)
    decorator.__name__ = f.__name__
    return decorator