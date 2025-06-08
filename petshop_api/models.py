from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

#usuario

class UserCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str

class UserLogin(BaseModel):
    email: EmailStr
    senha: str

class User(BaseModel):
    id: int
    nome: str
    email: EmailStr

    class Config:
        orm_mode = True

#produtos

class ProdutoBase(BaseModel):
    nome: str
    descricao: Optional[str] = None
    preco: float
    categoria: str  # brinquedos, higiene, comida, roupas, utensílios, etc.

class ProdutoCreate(ProdutoBase):
    pass

class Produto(ProdutoBase):
    id: int

    class Config:
        orm_mode = True

#consultas veterinárias

class ConsultaBase(BaseModel):
    cliente_id: int
    nome_pet: str
    data_hora: str  # formato: YYYY-MM-DD HH:MM
    motivo: Optional[str] = None

class ConsultaCreate(ConsultaBase):
    pass

class Consulta(ConsultaBase):
    id: int

    class Config:
        orm_mode = True

#banho e tosa

class BanhoTosaBase(BaseModel):
    cliente_id: int
    nome_pet: str
    servico: str  # banho, tosa, banho e tosa
    data_hora: str

class BanhoTosaCreate(BanhoTosaBase):
    pass

class BanhoTosa(BanhoTosaBase):
    id: int

    class Config:
        orm_mode = True

#pedidos

class PedidoProduto(BaseModel):
    produto_id: int
    quantidade: int

class PedidoBase(BaseModel):
    cliente_id: int
    produtos: List[PedidoProduto]

class PedidoCreate(PedidoBase):
    pass

class Pedido(PedidoBase):
    id: int
    data_hora: datetime
    total: float

    class Config:
        orm_mode = True