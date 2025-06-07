from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, models_db
from ..database import get_db
from ..auth import get_current_username

router = APIRouter()

def enviar_mensagem(telefone: str, mensagem: str):
    print(f"[SIMULAÇÃO] Enviando mensagem para {telefone}: {mensagem}")

@router.post("/", status_code=201)
def realizar_compra(compra: models.CompraCreate, db: Session = Depends(get_db)):
    produto = db.query(models_db.Produto).filter(models_db.Produto.id == compra.produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    novo = models_db.Compra(**compra.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)

    enviar_mensagem(compra.telefone, f"Compra realizada: {produto.nome}. Obrigado!")
    return {"msg": "Compra realizada", "id": novo.id}
