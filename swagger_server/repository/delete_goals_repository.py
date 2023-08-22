from swagger_server.models.db.goals_model import Goals
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db


class DeleteGoalsRepository:

    def __init__(self, mysql: db, log: logging ) -> None:
        self.log = log
        self.mysql = mysql
        self.sql_error_message = "Error durante la consulta en mysql :"
        self.msg_log = 'ITID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '

    def error_message_format(self, ex):
        return "Error durante la consulta en mysql : {}".format(ex)
    
    def delete_goals(self, id_goal, internalTransactionId):
        try:
            goals = Goals.query.get(id_goal)
            if goals:
                goals.destroy()
                return goals.to_json()
            else:
                return []
        except Exception as ex:
            error = self.error_message_format(ex)
            self.log.info(self.msg_log, internalTransactionId, "delete_goals", __name__, error)
            return ""