import grpc
from concurrent import futures
import fiscal_pb2
import fiscal_pb2_grpc
import uuid

class FiscalService(fiscal_pb2_grpc.FiscalServiceServicer):
    def EmitirNota(self, request, context):
        nota_id = str(uuid.uuid4())
        print(f"Nota emitida para {request.produto_id}, ID: {nota_id}")
        return fiscal_pb2.NotaResponse(sucesso=True, mensagem="Nota gerada com sucesso.", nota_id=nota_id)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    fiscal_pb2_grpc.add_FiscalServiceServicer_to_server(FiscalService(), server)
    server.add_insecure_port('[::]:50054')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()