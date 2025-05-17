# uvicorn servidor_rest_estoque:app --port 8002

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

class EstoqueRequest(BaseModel):
    produto_id: int
    quantidade: int

@app.post("/estoque/separar")
async def separar_estoque(request: EstoqueRequest):
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()

    cursor.execute("SELECT quantidade_estoque FROM produtos WHERE id = ?", (request.id))
    resultado = cursor.fetchone()

    if not resultado:
        conn.close()
        raise HTTPException(status_code=404, detail="Produto não encontrado no estoque")

    quantidade_atual = resultado[0]
    if quantidade_atual < request.quantidade_estoque:
        conn.close()
        raise HTTPException(status_code=400, detail="Estoque insuficiente")

    nova_quantidade = quantidade_atual - request.quantidade_estoque
    cursor.execute("UPDATE produtos SET quantidade_estoque = ? WHERE id = ?", (nova_quantidade, request.id))
    conn.commit()
    conn.close()

    print(f"[Estoque] Separando {request.quantidade_estoque} unidades do produto {request.id}")
    return {"sucesso": True, "mensagem": "Estoque separado com sucesso"}
