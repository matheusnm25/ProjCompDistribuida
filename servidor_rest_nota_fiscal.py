# uvicorn servidor_rest_nota_fiscal:app --port 8003

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class NotaFiscalRequest(BaseModel):
    pedido_id: int
    cpf: str

@app.post("/nota_fiscal/gerar")
async def gerar_nota_fiscal(request: NotaFiscalRequest):
    print(f"[Nota Fiscal] Gerando nota fiscal para pedido {request.pedido_id} com CPF {request.cpf}")
    return {
        "sucesso": True,
        "mensagem": f"Nota fiscal gerada para o pedido {request.pedido_id}"
    }
