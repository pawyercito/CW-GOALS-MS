from swagger_server.models.db.goals_model import Goals
from swagger_server.repository.base_repository import BaseRepository

class NewGoalsRepository(BaseRepository):

    def error_message_format(self, ex):
        return "Error durante la consulta en mysql : {}".format(ex)
    
    def create_goals(self, goals, internalTransactionId: str, externalTransactionId: str):
        try:
            new_goals = Goals(goals)
            new_goals.save()
            return new_goals.to_json()
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log,internalTransactionId, externalTransactionId, "new_goals", __name__, error)
            return ""