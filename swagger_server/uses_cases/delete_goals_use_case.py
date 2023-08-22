from swagger_server.models.response_delete_goals_vendor import ResponseDeleteGoalsVendor
from swagger_server.repository.delete_goals_repository import DeleteGoalsRepository
from swagger_server.utils.logs.logging import log as logging

class DeleteGoalsUseCase:

    def __init__(self, goals_respository: DeleteGoalsRepository, log: logging):
        self.log = log
        self.goals_respository = goals_respository
        self.msg_log = 'ITID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
    
    def delete_goals(self, id_goal: int, internalTransactionId: str):
        
        goals_data = self.goals_respository.delete_goals(id_goal, internalTransactionId)
        
        if goals_data:
            response = ResponseDeleteGoalsVendor(
                code="0",
                message="Meta eliminada exitosamente.",
                data=goals_data,
                internalTransactionId=internalTransactionId,
            )
            return response, 200
        else:
            response = ResponseDeleteGoalsVendor(
                code="1",
                message="La meta no existe.",
                data=[],
                internalTransactionId=internalTransactionId,
            )
            return response, 400
