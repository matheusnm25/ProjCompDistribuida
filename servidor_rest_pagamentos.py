from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class PagamentoRequest(BaseModel):
    pedido_id: int
    valor: float

@app.post("/pagamentos")
async def processar_pagamento(request: PagamentoRequest):
    print(f"[Pagamento] Processando pagamento do pedido {request.pedido_id} com valor R${request.valor}")
    return {"sucesso": True, "mensagem": "Pagamento processado com sucesso"}

