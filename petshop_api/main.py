from flask import Flask
from flask_cors import CORS
from petshop_api.routes.produtos import produtos_bp
from petshop_api.routes.consultas import consultas_bp
from petshop_api.routes.banho_tosa import banho_tosa_bp
from petshop_api.routes.pedidos import pedidos_bp
from petshop_api.routes.clientes import clientes_bp  # Inclui cadastro e login
from petshop_api.database import criar_tabelas

def create_petshop_api():
    petshop_api = Flask(__name__)
    CORS(petshop_api)  # Libera o uso da API por front-ends em outros domínios

    # Criar tabelas no banco
    criar_tabelas()

    # Registrar blueprints
    petshop_api.register_blueprint(produtos_bp, url_prefix="/produtos")
    petshop_api.register_blueprint(consultas_bp, url_prefix="/consultas")
    petshop_api.register_blueprint(banho_tosa_bp, url_prefix="/banho-tosa")
    petshop_api.register_blueprint(pedidos_bp, url_prefix="/pedidos")
    petshop_api.register_blueprint(clientes_bp)  # Rotas /cadastro e /login

    @petshop_api.route("/")
    def home():
        return {"mensagem": "API Petshop está no ar!"}

    return petshop_api

if __name__ == "__main__":
    petshop_api = create_petshop_api()
    petshop_api.run(debug=True)