from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, models_db
from ..database import get_db
from ..auth import get_current_username

router = APIRouter()

@router.post("/", status_code=201)
def adicionar_produto(produto: models.ProdutoCreate, db: Session = Depends(get_db)):
    novo = models_db.Produto(**produto.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return {"msg": "Produto adicionado", "id": novo.id}

@router.get("/", response_model=List[models.ProdutoCreate])
def listar_produtos(db: Session = Depends(get_db)):
    produtos = db.query(models_db.Produto).all()
    return produtos
