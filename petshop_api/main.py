from fastapi import FastAPI
from app.routes import produtos, clientes, pedidos, consultas, banho_tosa

app = FastAPI(title="Petshop API")

# Incluir rotas
app.include_router(produtos.router)
app.include_router(clientes.router)
app.include_router(pedidos.router)
app.include_router(consultas.router)
app.include_router(banho_tosa.router)

@app.get("/")
def home():
    return {"mensagem": "API do Petshop está online!"}
