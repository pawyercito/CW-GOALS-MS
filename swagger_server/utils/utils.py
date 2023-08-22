from datetime import datetime
from pytz import timezone
import os
import re
import random
import hashlib

# Funciones de utilidad para el sistema completo.

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def filter_dict(dict, fields):
    # Filtra el diccionario entrante, retornando nuevo diccionario
    # sólo con los campos definidos y descartando los demás.

    filtered_dict = {}

    for key in dict:

        if key in fields:
            filtered_dict[key] = dict[key]

    return filtered_dict


def format_date(datetime):
    # Retorna una representación en String de una fecha/hora dada.

    return datetime.strftime(DATE_FORMAT)


def get_current_datetime():
    # Retorna la fecha actual en su correspondiente timezone

    return datetime.now(timezone('America/Guayaquil'))


def check_email(email):
    """
    Valida el email

    Args:
        email (String): correo electronico

    Returns:
        True or False si mail es valido o invalido
    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False

