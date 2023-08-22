from swagger_server.models.db.goals_model import Goals
from swagger_server.repository.base_repository import BaseRepository

class GetGoalsRepository(BaseRepository):

    def error_message_format(self, ex):
        return "Error during the query in MySQL: {}".format(ex)

    def get_goals(self, body, internalTransactionId, externalTransactionId):
        try:
            id_goal = body.id_goal  # Asegúrate de que "commercial_conditions" sea el atributo correcto en tu modelo de categoría
            goals = Goals.query.filter_by(id_goal=id_goal).first()
            return goals.to_json() if goals else None  # Puede que la categoría no exista, en ese caso devuelve None
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log, internalTransactionId, externalTransactionId, "get_goals", __name__, error)
            return None  # Maneja el error adecuadamente en tu controlador
