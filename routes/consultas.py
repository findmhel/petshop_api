from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, models_db
from ..database import get_db
from ..auth import get_current_username

router = APIRouter()

def enviar_mensagem(telefone: str, mensagem: str):
    print(f"[SIMULAÇÃO] Enviando mensagem para {telefone}: {mensagem}")

@router.post("/", status_code=201)
def criar_consulta(consulta: models.ConsultaCreate, db: Session = Depends(get_db)):
    novo = models_db.Consulta(**consulta.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)

    enviar_mensagem(consulta.telefone, f"Consulta marcada para {consulta.nome_pet} em {consulta.data}.")
    return {"msg": "Consulta marcada", "id": novo.id}