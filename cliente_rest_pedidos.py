import requests
import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

def chamar(endpoint, json):
    print(f"[Pedido] Chamando {endpoint} com {json}")
    try:
        r = requests.post(endpoint, json=json)
        print(f"→ Status {r.status_code}: {r.json()}")
    except Exception as e:
        print(f"→ Erro: {e}")

def realizar_pedido():
    id = 1
    produto_id = 101
    quantidade = 2
    #valor = ("SELECT FROM produtos 
    #CONSULTAR VALOR DA TABELA PRODUTOS
    endereco = "Rua Exemplo, 123"
    cpf = "440.598.840-49"
    conn.commit()

    chamar("http://localhost:8001/pagamentos", {"id": id, "quantidade_estoque":quantidade})
    #chamar("http://localhost:8002/estoque/separar", {"id": id,"quantidade_estoque": quantidade})
    #hamar("http://localhost:8003/nota_fiscal/gerar", {"pedido_id": pedido_id, "valor": valor, "cpf": cpf})
    #chamar("http://localhost:8004/logistica/entregar", {"pedido_id": pedido_id, "endereco": endereco})
    #chamar("http://localhost:8005/catalogo/consultar", {"produto_id": id})

if __name__ == "__main__":
    realizar_pedido()
