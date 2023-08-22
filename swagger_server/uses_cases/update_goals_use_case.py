from swagger_server.models.response_edit_goals_vendor import ResponseEditGoalsVendor
from swagger_server.repository.update_goals_repository import UpdateGoalsRepository
from swagger_server.utils.logs.logging import log as Logging
from swagger_server.models.request_edit_goals_vendor import RequestEditGoalsVendor

class UpdateGoalsUseCase:

    def __init__(self, goals_repository: UpdateGoalsRepository, log: Logging):
        self.log = log
        self.goals_repository = goals_repository
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
    
    def update_goals(self, id_goal, body: RequestEditGoalsVendor, internalTransactionId: str):
        
        goals_exist = self.goals_repository.check_goals(id_goal, internalTransactionId, body.externalTransactionId)
        
        if goals_exist is None:
            response = ResponseEditGoalsVendor(
                code="1",
                message="No hay metas registradas.",
                data=[],
                internalTransactionId=internalTransactionId,
                externalTransactionId=body.externalTransactionId
            )
            return response, 404
        
        goals_data = body.data.to_dict()
        data = self.goals_repository.save_changes(goals_exist, goals_data, internalTransactionId, body.externalTransactionId)
        
        if data:
            response = ResponseEditGoalsVendor(
                code="0",
                message="Metas actualizadas exitosamente.",
                data=data,
                internalTransactionId=internalTransactionId,
                externalTransactionId=body.externalTransactionId
            )
            return response
        else:
            return 400