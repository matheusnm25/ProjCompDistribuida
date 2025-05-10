from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class EstoqueRequest(BaseModel):
    produto_id: int
    quantidade: int

@app.post("/estoque/separar")
async def separar_estoque(request: EstoqueRequest):
    print(f"[Estoque] Separando {request.quantidade} unidades do produto {request.produto_id}")
    return {"sucesso": True, "mensagem": "Estoque separado"}
