from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class NotaFiscalRequest(BaseModel):
    pedido_id: int
    cpf: str

@app.post("/notafiscal/gerar")
async def gerar_nota_fiscal(request: NotaFiscalRequest):
    print(f"[Nota Fiscal] Gerando nota fiscal para pedido {request.pedido_id} com CPF {request.cpf}")
    return {"sucesso": True, "mensagem": "Nota fiscal gerada"}
