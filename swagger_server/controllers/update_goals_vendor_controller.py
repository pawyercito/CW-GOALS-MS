import connexion

from swagger_server.models.request_edit_goals_vendor import RequestEditGoalsVendor  # noqa: E501

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internalTransactionId
from swagger_server.utils.logs.logging import log as logging
from swagger_server.uses_cases.update_goals_use_case import UpdateGoalsUseCase
from swagger_server.repository.update_goals_repository import UpdateGoalsRepository
from swagger_server.resources.db import db

class UpdateGoalsView(MethodView):

    def __init__(self):
        log = logging()
        mysql = db
        self.log = log
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
        update_goals_repository = UpdateGoalsRepository(mysql, log)
        self.update_goals_use_case = UpdateGoalsUseCase(update_goals_repository, log)


    def edit_goals_vendor(self, id_goal):  # noqa: E501
        """Actualizar goalsVendor.

        Actualizar goalsVendor. # noqa: E501

        :param id_goal: 
        :type id_goal: int
        :param body: 
        :type body: dict | bytes

        :rtype: ResponseEditGoalsVendor
        """
        response = ""
        internalTransactionId = str(generate_internalTransactionId())
        function_name = "update_goals"
        package_name = __name__
        log = logging()
        start_time = default_timer()

        if connexion.request.is_json:

            body = RequestEditGoalsVendor.from_dict(connexion.request.get_json())  # noqa: E501
            externalTransactionId = body.externalTransactionId
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internalTransactionId, externalTransactionId, function_name, package_name, message)

            response = self.update_goals_use_case.update_goals(id_goal, body, internalTransactionId)

            end_time = default_timer()
            log.info("ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos", internalTransactionId, body.externalTransactionId, f"{function_name}", __name__, round((end_time-start_time)*1000))
            return response
