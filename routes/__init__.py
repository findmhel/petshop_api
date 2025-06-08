from flask import Blueprint

from .produtos import produtos_bp
from .clientes import clientes_bp
from .consultas import consultas_bp
from .banho_tosa import banho_tosa_bp
from .pedidos import pedidos_bp

def register_routes(petshop_api):
    petshop_api.register_blueprint(produtos_bp, url_prefix="/produtos")
    petshop_api.register_blueprint(clientes_bp, url_prefix="/clientes")
    petshop_api.register_blueprint(consultas_bp, url_prefix="/consultas")
    petshop_api.register_blueprint(banho_tosa_bp, url_prefix="/banho_tosa")
    petshop_api.register_blueprint(pedidos_bp, url_prefix="/pedidos")