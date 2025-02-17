import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('PasswordGenerator')
logger.setLevel(logging.INFO)

# Creating handler
handler = RotatingFileHandler('password_generator.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter) # Formats the log messages.

# Adding handler to logger
logger.addHandler(handler)

# Log messages
logger.info('example log message')