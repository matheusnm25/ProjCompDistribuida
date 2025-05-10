import grpc
from concurrent import futures
import pagamento_pb2
import pagamento_pb2_grpc

class PagamentoService(pagamento_pb2_grpc.PagamentoServiceServicer):
    def ProcessarPagamento(self, request, context):
        print(f"Pagamento processado: {request.produto_id}, valor R$ {request.valor:.2f}")
        return pagamento_pb2.PagamentoResponse(sucesso=True, mensagem="Pagamento aprovado.")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pagamento_pb2_grpc.add_PagamentoServiceServicer_to_server(PagamentoService(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()