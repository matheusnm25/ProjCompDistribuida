import grpc
import pedido_pb2, pedido_pb2_grpc
import pagamento_pb2, pagamento_pb2_grpc
import estoque_pb2, estoque_pb2_grpc
import fiscal_pb2, fiscal_pb2_grpc
import logistica_pb2, logistica_pb2_grpc
import catalogo_pb2, catalogo_pb2_grpc

def testar_servicos():
    # Catalogo
    with grpc.insecure_channel('localhost:50056') as channel:
        stub = catalogo_pb2_grpc.CatalogoServiceStub(channel)
        resposta = stub.ListarProdutos(catalogo_pb2.Empty())
        print("Produtos no catálogo:")
        for p in resposta.produtos:
            print(f"- {p.nome} (Estoque: {p.estoque})")

    # Pedido
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pedido_pb2_grpc.PedidoServiceStub(channel)
        resp = stub.CriarPedido(pedido_pb2.PedidoRequest(produto_id="1", quantidade=2, valor_total=200.0))
        print("Pedido:", resp.mensagem)

    # Pagamento
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = pagamento_pb2_grpc.PagamentoServiceStub(channel)
        resp = stub.ProcessarPagamento(pagamento_pb2.PagamentoRequest(produto_id="1", quantidade=2, valor=200.0))
        print("Pagamento:", resp.mensagem)

    # Estoque
    with grpc.insecure_channel('localhost:50053') as channel:
        stub = estoque_pb2_grpc.EstoqueServiceStub(channel)
        resp = stub.SepararEstoque(estoque_pb2.EstoqueRequest(produto_id="1", quantidade=2))
        print("Estoque:", resp.mensagem)

    # Fiscal
    with grpc.insecure_channel('localhost:50054') as channel:
        stub = fiscal_pb2_grpc.FiscalServiceStub(channel)
        resp = stub.EmitirNota(fiscal_pb2.NotaRequest(produto_id="1", quantidade=2, valor_total=200.0))
        print("Nota Fiscal:", resp.mensagem, "ID:", resp.nota_id)

    # Logística
    with grpc.insecure_channel('localhost:50055') as channel:
        stub = logistica_pb2_grpc.LogisticaServiceStub(channel)
        resp = stub.AgendarEnvio(logistica_pb2.EnvioRequest(nota_id="1234", produto_id="1", quantidade=2))
        print("Logística:", resp.mensagem)

if __name__ == '__main__':
    testar_servicos()
