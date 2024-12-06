import sys
import os

BASE_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
log_file = os.path.join(BASE_DIR, "logger.log")

from logging import getLogger, Formatter, DEBUG
from logging.handlers import RotatingFileHandler

FORMAT = '%(asctime)s : %(name)s : %(levelname)s : %(funcName)s : %(message)s'
formatter = Formatter(FORMAT)

file_handler = RotatingFileHandler(log_file, mode='w', encoding='utf-8', maxBytes=2*1024*1024, backupCount=0)
file_handler.setLevel(DEBUG)
file_handler.setFormatter(formatter)

logger = getLogger()
logger.setLevel(DEBUG)

logger.addHandler(file_handler)