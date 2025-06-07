from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, models_db
from ..database import get_db

router = APIRouter()

def enviar_mensagem(telefone: str, mensagem: str):
    print(f"[SIMULAÇÃO] Enviando mensagem para {telefone}: {mensagem}")

@router.post("/", status_code=201)
def agendar_banho_tosa(agendamento: models.BanhoTosaCreate, db: Session = Depends(get_db)):
    novo = models_db.BanhoTosa(**agendamento.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)

    enviar_mensagem(agendamento.telefone, f"Banho e tosa agendado para {agendamento.nome_pet} em {agendamento.data}.")
    return {"msg": "Banho e tosa agendado", "id": novo.id}
