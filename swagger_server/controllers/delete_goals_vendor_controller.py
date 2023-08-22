import connexion
from flask.views import MethodView
from swagger_server.models.response_delete_goals_vendor import ResponseDeleteGoalsVendor  # noqa: E501
from swagger_server import util
from swagger_server.utils.logs.logging import log as logging
from swagger_server.resources.db import db
from swagger_server.repository.delete_goals_repository import DeleteGoalsRepository
from swagger_server.uses_cases.delete_goals_use_case import DeleteGoalsUseCase
from timeit import default_timer
from swagger_server.utils.transactions.transaction import generate_internalTransactionId

class DeleteGoalsView(MethodView):


    def __init__(self):
            log = logging()
            mysql = db
            self.log = log
            self.msg_log = 'ITID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
            self.msg_log_time = 'ITID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
            delete_goals_repository = DeleteGoalsRepository(mysql, log)
            self.delete_goals_use_case = DeleteGoalsUseCase(delete_goals_repository, log)


    def delete_goals_vendor(self, id_goal):  # noqa: E501
        """Eliminar goalsVendor.

        Eliminar un goalsVendor existente. # noqa: E501

        :param id_goal: 
        :type id_goal: int

        :rtype: ResponseDeleteGoalsVendor
        """
        response = ""
        internalTransactionId = str(generate_internalTransactionId())
        function_name = "delete_goals"
        package_name = __name__
        log = self.log
        start_time = default_timer()

        message = f"start request: {function_name}"
        log.info(
            self.msg_log,
            internalTransactionId, function_name, package_name, message)

        response = self.delete_goals_use_case.delete_goals(id_goal, internalTransactionId)

        end_time = default_timer()
        log.info("ITID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos", internalTransactionId, f"{function_name}", __name__, round((end_time-start_time)*1000))
        return response
