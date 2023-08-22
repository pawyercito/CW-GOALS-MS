import connexion
from swagger_server.models.request_get_single_goals_vendor import RequestGetSingleGoalsVendor  # noqa: E501
from flask.views import MethodView
from timeit import default_timer
from swagger_server.utils.transactions.transaction import generate_internalTransactionId
from swagger_server.utils.logs.logging import log as logging
from swagger_server.repository.get_goals import GetGoalsRepository
from swagger_server.resources.db import db

class GetGoalsView(MethodView):


    def __init__(self):
            log = logging()
            mysql = db
            self.log = log
            self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
            self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
            get_goals_repository = GetGoalsRepository(mysql, log)
            self.get_goals_use_case = GetGoalsRepository(get_goals_repository, log)

    def get_single_goals_vendor(self):  # noqa: E501
        """Obtener un goalsVendor específico.

        Obtener un goalsVendor específico por su ID. # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseGetSingleGoalsVendor
        """
        response = ""
        internalTransactionId = str(generate_internalTransactionId())
        function_name = "get_goals"
        package_name = __name__
        log = logging()
        start_time = default_timer()

        if connexion.request.is_json:
            body = RequestGetSingleGoalsVendor.from_dict(connexion.request.get_json())  # noqa: E501
            externalTransactionId = body.externalTransactionId
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internalTransactionId, externalTransactionId, function_name, package_name, message)

            response = self.get_goals_use_case.get_goals(body, internalTransactionId, body.externalTransactionId)

            end_time = default_timer()
            log.info("ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos", internalTransactionId, body.externalTransactionId, f"{function_name}", __name__, round((end_time-start_time)*1000))
            return response

