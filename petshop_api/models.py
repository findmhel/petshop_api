from pydantic import BaseModel
from typing import Optional

class Produto(BaseModel):
    id: Optional[int] = None
    nome: str
    preco: float
    descricao: str
    estoque: int
    categoria: str

class Cliente(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str
    telefone: str

class Pedido(BaseModel):
    id: Optional[int] = None
    cliente_nome: str
    produto_id: int
    quantidade: int
    total: float

class Consulta(BaseModel):
    id: Optional[int] = None
    cliente_nome: str
    pet_nome: str
    data_hora: str
    veterinario: str
    observacoes: Optional[str] = None

class BanhoTosa(BaseModel):
    id: Optional[int] = None
    cliente_nome: str
    pet_nome: str
    servico: str
    data_hora: str
