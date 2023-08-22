import json
import os


def access():

    """Obtiene todas las credenciales del microservicio

    Returns:
        dict: credenciales del microservicio
    """  

    current_directory = os.path.dirname(os.path.realpath(__file__))
    access = os.path.join(current_directory, 'access.json')
    with open(access, "r") as file:
        json_response = json.load(file)
        return json_response