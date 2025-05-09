import grpc
from concurrent import futures
import estoque_pb2
import estoque_pb2_grpc

class EstoqueService(estoque_pb2_grpc.EstoqueServiceServicer):
    def SepararEstoque(self, request, context):
        print(f"Estoque separado: {request.produto_id}, {request.quantidade} unidades")
        return estoque_pb2.EstoqueResponse(sucesso=True, mensagem="Estoque reservado.")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    estoque_pb2_grpc.add_EstoqueServiceServicer_to_server(EstoqueService(), server)
    server.add_insecure_port('[::]:50053')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()