from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():
    load_dotenv()
    petshop_api = Flask(__name__)

    petshop_api.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///petshop.db'
    petshop_api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_petshop_api(petshop_api)

    from .routes import produtos, clientes, pedidos, consultas, banho_tosa
    petshop_api.register_blueprint(produtos.bp, url_prefix="/produtos")
    petshop_api.register_blueprint(clientes.bp, url_prefix="/clientes")
    petshop_api.register_blueprint(pedidos.bp, url_prefix="/pedidos")
    petshop_api.register_blueprint(consultas.bp, url_prefix="/consultas")
    petshop_api.register_blueprint(banho_tosa.bp, url_prefix="/banho-tosa")

    return petshop_api