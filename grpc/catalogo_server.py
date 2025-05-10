import grpc
from concurrent import futures
import catalogo_pb2
import catalogo_pb2_grpc

class CatalogoService(catalogo_pb2_grpc.CatalogoServiceServicer):
    def ListarProdutos(self, request, context):
        produtos = [
            catalogo_pb2.Produto(produto_id="1", nome="Produto A", estoque=100),
            catalogo_pb2.Produto(produto_id="2", nome="Produto B", estoque=50),
        ]
        return catalogo_pb2.ListaProdutos(produtos=produtos)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    catalogo_pb2_grpc.add_CatalogoServiceServicer_to_server(CatalogoService(), server)
    server.add_insecure_port('[::]:50056')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()