from swagger_server.models.response_get_all_goals_vendor import ResponseGetAllGoalsVendor
from swagger_server.repository.get_all_goals_repository import AllGoalsRepository
from swagger_server.utils.logs.logging import log as Logging
from swagger_server.models.request_get_all_goals_vendor import RequestGetAllGoalsVendor

class AllGoalsUseCase:

    def __init__(self, goals_repository: AllGoalsRepository, log: Logging):
        self.log = log
        self.goals_repository = goals_repository
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
    
    def get_all_goals(self, body: RequestGetAllGoalsVendor, internalTransactionId: str):

        goals_data = self.goals_repository.get_all_goals(body.externalTransactionId, internalTransactionId)
        
        if goals_data:
            response = ResponseGetAllGoalsVendor(
                code="0",
                message="Datos obtenidos exitosamente",
                data=goals_data,
                internalTransactionId=internalTransactionId,
                externalTransactionId=body.externalTransactionId
            )
        else:
            response = ResponseGetAllGoalsVendor(
                code="1",
                message="No hay condiciones comerciales registradas.",
                data=[],
                internalTransactionId=internalTransactionId,
                externalTransactionId=body.externalTransactionId
            )
        return response