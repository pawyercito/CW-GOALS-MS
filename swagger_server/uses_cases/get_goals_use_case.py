from swagger_server.models.response_get_single_goals_vendor import ResponseGetSingleGoalsVendor # Importa la clase correcta para la respuesta de categoría
from swagger_server.repository.get_goals import GetGoalsRepository  # Importa el repositorio de categoría
from swagger_server.utils.logs.logging import log as Logging
from swagger_server.models.request_get_single_goals_vendor import RequestGetSingleGoalsVendor  # Importa la clase correcta para la solicitud de categoría

class GetGoalsUseCase:

    def __init__(self, goals_repository: GetGoalsRepository, log: Logging):
        self.log = log
        self.goals_repository = goals_repository
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
    
    def get_goals(self, body: RequestGetSingleGoalsVendor, internalTransactionId: str, externalTransactionId: str):
        print(body)
        data = self.goals_repository.get_goals(body, internalTransactionId, externalTransactionId)
       
        if data:
            response = ResponseGetSingleGoalsVendor(
                code="0",
                message="Datos obtenidos exitosamente",
                data=data,
                internalTransactionId=internalTransactionId,
                externalTransactionId=externalTransactionId
            )
            return response
        else:
            response = ResponseGetSingleGoalsVendor(
                code="1",
                message="No hay una meta registrada con ese ID.",
                data=[],
                internalTransactionId=internalTransactionId,
                externalTransactionId=externalTransactionId
            )
            return response, 404