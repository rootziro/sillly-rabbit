import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('PasswordGenerator')
logger.setlevel(logging.INFO)
logging.basicConfig(filename='app.log', level=logging.INFO)
