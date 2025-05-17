# uvicorn servidor_rest_logistica:app --port 8004

from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class LogisticaRequest(BaseModel):
    pedido_id: int
    endereco: str

@app.post("/logistica/entregar")
async def agendar_entrega(request: LogisticaRequest):
    print(f"[Logistica] Agendando entrega do pedido {request.pedido_id} para o endereço: {request.endereco}")
    return {"sucesso": True, "mensagem": "Entrega agendada"}