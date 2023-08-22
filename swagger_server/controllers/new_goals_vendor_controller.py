import connexion

from swagger_server.models.request_new_goals_vendor import RequestNewGoalsVendor

from flask.views import MethodView

from timeit import default_timer

from swagger_server.utils.transactions.transaction import generate_internalTransactionId
from swagger_server.utils.logs.logging import log as logging
from swagger_server.uses_cases.new_goals_use_case import NewGoalsUseCase
from swagger_server.repository.create_goals_repository import NewGoalsRepository
from swagger_server.resources.db import db


class NewGoalsView(MethodView):

    def __init__(self):
        log = logging()
        mysql = db
        self.log = log
        self.msg_log = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: %r '
        self.msg_log_time = 'ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos'
        new_goals_repository = NewGoalsRepository(mysql, log)
        self.new_goals_use_case = NewGoalsUseCase(new_goals_repository, log)


    def new_goals_vendor(self):  # noqa: E501
        """Crear un nuevo goalsVendor.

        Crear un nuevo goalsVendor. # noqa: E501

        :param body: 
        :type body: dict | bytes

        :rtype: ResponseNewGoalsVendor
        """
        response = ""
        internalTransactionId = str(generate_internalTransactionId())
        function_name = "new_goals"
        package_name = __name__
        log = logging()
        start_time = default_timer()

        if connexion.request.is_json:
            body = RequestNewGoalsVendor.from_dict(connexion.request.get_json())  # noqa: E501
            externalTransactionId = body.externalTransactionId
            message = f"start request: {function_name}"
            log.info(
                self.msg_log,
                internalTransactionId, externalTransactionId, function_name, package_name, message)

            response = self.new_goals_use_case.create_goals(body, internalTransactionId)

            end_time = default_timer()
            log.info("ITID: %r - ETID: %r - Funcion: %r - Paquete : %r - Mensaje: Fin de la transacción, procesada en : %r milisegundos", internalTransactionId, body.externalTransactionId, f"{function_name}", __name__, round((end_time-start_time)*1000))
            return response

