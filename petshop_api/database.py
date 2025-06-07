from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Consulta(Base):
    __tablename__ = 'consultas'
    id = Column(Integer, primary_key=True, index=True)
    nome_pet = Column(String, index=True)
    dono = Column(String)
    telefone = Column(String)
    data = Column(String)

class BanhoTosa(Base):
    __tablename__ = 'banho_tosa'
    id = Column(Integer, primary_key=True, index=True)
    nome_pet = Column(String)
    dono = Column(String)
    telefone = Column(String)
    data = Column(String)

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    categoria = Column(String)
    preco = Column(Float)

class Compra(Base):
    __tablename__ = 'compras'
    id = Column(Integer, primary_key=True, index=True)
    comprador = Column(String)
    telefone = Column(String)
    produto_id = Column(Integer, ForeignKey('produtos.id'))
    produto = relationship("Produto")
