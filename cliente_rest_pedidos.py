import requests

def chamar(endpoint, json):
    print(f"[Pedido] Chamando {endpoint} com {json}")
    try:
        r = requests.post(endpoint, json=json)
        print(f"→ Status {r.status_code}: {r.json()}")
    except Exception as e:
        print(f"→ Erro: {e}")

def realizar_pedido():
    pedido_id = 1
    valor = 150.75
    produto_id = 101
    quantidade = 2
    endereco = "Rua Exemplo, 123"

    chamar("http://localhost:8001/pagamentos", {"pedido_id": pedido_id, "valor": valor})
    chamar("http://localhost:8002/estoque/separar", {"produto_id": produto_id, "quantidade": quantidade})
    chamar("http://localhost:8003/nota_fiscal/gerar", {"pedido_id": pedido_id, "valor": valor})
    chamar("http://localhost:8004/logistica/entregar", {"pedido_id": pedido_id, "endereco": endereco})
    chamar("http://localhost:8005/catalogo/consultar", {"produto_id": produto_id})

if __name__ == "__main__":
    realizar_pedido()
