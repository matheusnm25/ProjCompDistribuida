from fastapi import FastAPI

app = FastAPI()

@app.get("/catalogo/produtos")
async def listar_produtos():
    print("[Catálogo] Listando produtos disponíveis")
    return [
        {"id": 101, "nome": "Produto A", "preco": 50.0},
        {"id": 102, "nome": "Produto B", "preco": 75.0},
    ]
