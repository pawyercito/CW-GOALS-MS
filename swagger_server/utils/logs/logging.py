import logging
from logging.handlers import RotatingFileHandler
import datetime
import os

def log():
    """Generador de logs para el microservicio

    Returns:
        function: logging
    """  
    now = datetime.datetime.now()
    format_logger = now.strftime('%Y-%m-%d')
    logger = logging.getLogger('')
    logger.setLevel(logging.INFO)
    
    # Verificar si el directorio de registro existe, si no, créalo
    log_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    rthandler = RotatingFileHandler(
        os.path.join(log_dir, f'goals-ms-{format_logger}.log'),
        maxBytes=2 * 1024 * 1024,
        backupCount=5
    )
    
    formatter = logging.Formatter('%(asctime)s %(levelname)s | %(message)s')
    rthandler.setFormatter(formatter)

    if(logger.hasHandlers()):
        logger.handlers.clear()

    logger.addHandler(rthandler)
    
    return logger
