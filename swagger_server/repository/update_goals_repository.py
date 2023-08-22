from swagger_server.models.db.goals_model import Goals
from swagger_server.repository.base_repository import BaseRepository


class UpdateGoalsRepository(BaseRepository):

    def error_message_format(self, ex):
        return "Error during the query in MySQL: {}".format(ex)

    def save_changes(self, goals_exist, goals_data, internalTransactionId, externalTransactionId):
        try:
            goals_exist.internet_dolar = goals_data.get("internet_dolar")
            goals_exist.internet_volumen = goals_data.get("internet_volumen")
            goals_exist.telefonia_dolar = goals_data.get("telefonia_dolar")
            goals_exist.telefonia_volumen = goals_data.get("telefonia_volumen")
            goals_exist.television_dolar = goals_data.get("television_dolar")
            goals_exist.television_volumen = goals_data.get("television_volumen")
            goals_exist.goal_date = goals_data.get("goal_date")
            goals_exist.created_at = goals_data.get("created_at")
            goals_exist.id_user = goals_data.get("id_user")

            goals_exist.save()
            return goals_exist.to_json()
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log, internalTransactionId, externalTransactionId, "save_changes", __name__, error)
            return ""

    def check_goals(self, id_commercial_conditions, internalTransactionId, externalTransactionId):
        try:
            goals = Goals.query.get(id_commercial_conditions)
            return goals
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log, internalTransactionId, externalTransactionId, "check_goals", __name__, error)
            return ""