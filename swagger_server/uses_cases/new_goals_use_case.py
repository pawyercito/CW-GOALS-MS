from swagger_server.repository.create_goals_repository import NewGoalsRepository
from swagger_server.utils.logs.logging import log as Logging
from swagger_server.models.request_new_goals_vendor import RequestNewGoalsVendor
from swagger_server.models.response_new_goals_vendor import ResponseNewGoalsVendor

class NewGoalsUseCase:

    def __init__(self, goals_repository: NewGoalsRepository, log: Logging):
        self.log = log
        self.goals_repository = goals_repository
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
    
    def create_goals(self, body: RequestNewGoalsVendor, internalTransactionId: str):
        goals = body.data.to_dict()
        data = self.goals_repository.create_goals(goals, internalTransactionId, body.externalTransactionId)
        
        if data:
            response = ResponseNewGoalsVendor(
                code="0",
                message="Meta creada exitosamente.",
                data=data,
                internalTransactionId=internalTransactionId,
                externalTransactionId=body.externalTransactionId
            )
            return response
        else:
            response = ResponseNewGoalsVendor(
                code="1",
                message="No se logró crear una Meta.",
                data=[],
                internalTransactionId=internalTransactionId,
                externalTransactionId=body.externalTransactionId
            )
            return response, 404