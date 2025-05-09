import grpc
from concurrent import futures
import logistica_pb2
import logistica_pb2_grpc

class LogisticaService(logistica_pb2_grpc.LogisticaServiceServicer):
    def AgendarEnvio(self, request, context):
        print(f"Envio agendado: Nota {request.nota_id}, Produto {request.produto_id}, Qtde {request.quantidade}")
        return logistica_pb2.EnvioResponse(sucesso=True, mensagem="Envio agendado com sucesso.")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    logistica_pb2_grpc.add_LogisticaServiceServicer_to_server(LogisticaService(), server)
    server.add_insecure_port('[::]:50055')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()