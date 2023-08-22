from swagger_server.models.db.goals_model import Goals
from swagger_server.repository.base_repository import BaseRepository

class AllGoalsRepository(BaseRepository):

    def error_message_format(self, ex):
        return "Error durante la consulta en mysql : {}".format(ex)
    
    def get_all_goals(self, internalTransactionId, externalTransactionId):
        try:
            goals = Goals.query.all()
            if goals:
                data = [o.to_json() for o in goals]
                return data
            else:
                return []
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log,internalTransactionId, externalTransactionId, "get_all_goals", __name__, error)
            return ""