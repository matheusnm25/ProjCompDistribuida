# uvicorn servidor_rest_catalogo:app --port 8005

from fastapi import FastAPI, Request
import sqlite3

app = FastAPI()

@app.post("/catalogo/consultar")
async def consultar_produto(request: Request):
    dados = await request.json()
    produto_id = dados.get("produto_id")

    print(f"[Catálogo] Consultando produto_id={produto_id}")

    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()
    cursor.execute("SELECT produto_id, nome, preco, quantidade_estoque FROM produtos")
    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            "quantidade_estoque": row[3]
        }
    else:
        return {"erro": "Produto não encontrado"}
