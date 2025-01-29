import os
import sys
from logging import getLogger, Formatter, DEBUG
from logging.handlers import RotatingFileHandler

# Установка базовой директории
BASE_DIR = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
log_file = os.path.join(BASE_DIR, "logger.log")

# Формат логов
FORMAT = '%(asctime)s : %(name)s : %(levelname)s : %(funcName)s : %(message)s'
formatter = Formatter(FORMAT)

# Настройка ротации файла
file_handler = RotatingFileHandler(
    log_file,
    mode='a',             # Режим append (добавление)
    encoding='utf-8',
    maxBytes=2 * 1024 * 1024, # 2 МБ
    backupCount=1         # Храним одну резервную копию
)
file_handler.setLevel(DEBUG)
file_handler.setFormatter(formatter)

# Настройка логера
logger = getLogger()

# Удаляем старые обработчики, чтобы избежать конфликтов
while logger.hasHandlers():
    logger.removeHandler(logger.handlers[0])

# Добавляем обработчик
logger.setLevel(DEBUG)
logger.addHandler(file_handler)