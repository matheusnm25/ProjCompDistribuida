# uvicorn servidor_rest_pagamentos:app --port 8001

from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class PagamentoRequest(BaseModel):
    id: int
    quantidade_estoque: int
    valor: float

@app.post("/pagamentos")
async def processar_pagamento(request: PagamentoRequest):
    print(f"[Pagamento] Processando pagamento do pedido {request.id} com valor R${request.valor}")
    return {"sucesso": True, "mensagem": "Pagamento processado com sucesso"}

