import grpc
from concurrent import futures
import pedido_pb2
import pedido_pb2_grpc

class PedidoService(pedido_pb2_grpc.PedidoServiceServicer):
    def CriarPedido(self, request, context):
        print(f"Pedido recebido: {request.produto_id}, {request.quantidade} un, R$ {request.valor_total:.2f}")
        # Aqui chamaria PagamentoService, omitido por simplicidade
        return pedido_pb2.PedidoResponse(sucesso=True, mensagem="Pedido criado com sucesso.")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pedido_pb2_grpc.add_PedidoServiceServicer_to_server(PedidoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()