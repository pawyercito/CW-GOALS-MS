import connexion
from flask.views import MethodView
from swagger_server.models.request_get_all_goals_vendor import RequestGetAllGoalsVendor  # noqa: E501
from swagger_server.utils.logs.logging import log as logging
from swagger_server.utils.transactions.transaction import generate_internalTransactionId
from swagger_server.resources.db import db
from swagger_server.repository.get_all_goals_repository import AllGoalsRepository
from swagger_server.uses_cases.all_goals_use_case import AllGoalsUseCase
from timeit import default_timer

class AllGoalsView(MethodView):

    def __init__(self):
        log = logging()
        mysql = db
        self.log = log
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
        all_goals_repository = AllGoalsRepository(mysql, log)
        self.all_goals_use_case = AllGoalsUseCase(all_goals_repository, log)


    def get_all_goals_vendor(self):  # noqa: E501
        """Obtener todos los goalsVendor.

        Obtener todos los goalsVendor. # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseGetAllGoalsVendor
        """
        response = ""
        internalTransactionId = str(generate_internalTransactionId())
        function_name = "all_goals"
        package_name = __name__
        log = logging()
        start_time = default_timer()

        if connexion.request.is_json:

            body = RequestGetAllGoalsVendor.from_dict(connexion.request.get_json())  # noqa: E501
            externalTransactionId = body.externalTransactionId
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internalTransactionId, externalTransactionId, function_name, package_name, message)

            response = self.all_goals_use_case.get_all_goals(body, internalTransactionId)

            end_time = default_timer()
            log.info("ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos", internalTransactionId, body.externalTransactionId, f"{function_name}", __name__, round((end_time-start_time)*1000))
            return response
