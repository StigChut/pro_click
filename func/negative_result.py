""" Модуль содержит функции для отработки негативного сценария
Когда не успели забронировать слот или получили ошибку """

import os

from my_logger import logger, BASE_DIR
from func.image_screen import find_and_interact


# Поиск алерта "Не успели" после нажатия кнопки "Запланировать"
def red_alert(title: str):
    # Относительный путь к изображению
    image_path = os.path.join(BASE_DIR, 'image_button', 'red_alert.png')
    assert os.path.exists(image_path), f"Файл не найден по указанному пути: {image_path}"
    close_alert_path = os.path.join(BASE_DIR, 'image_button', 'close_red_alert.png')
    assert os.path.exists(close_alert_path), f"Файл не найден по указанному пути: {close_alert_path}"

    try:
        # Проверям алерт
        if find_and_interact(image_path, title, close_alert_path):
            logger.debug("Алерт обнаружен и закрыт")
            return True
        else:
            logger.debug("Алерт не обниружен или не закрыт")
            return False

    except Exception as e:
        logger.exception(f"Ошибка: {e}")


# Поиск алерта ошибки диапазона дат, после нажатия кнопки "Выбрать"
def red_alert_time_date(image_path, title: str):
    # Относительный путь к изображению
    close_alert_path = os.path.join(BASE_DIR, 'image_button', 'close_red_alert.png')
    assert os.path.exists(close_alert_path), f"Файл не найден по указанному пути: {close_alert_path}"

    try:
        # Проверям алерт
        if find_and_interact(image_path, title, close_alert_path):
            logger.debug("Алерт обнаружен и закрыт")
            return True
        else:
            logger.debug("Алерт не обниружен или не закрыт")
            return False

    except Exception as e:
        logger.exception(f"Ошибка: {e}")


# Поиск алерта ошибка базы данных
def red_alert_error_bd(title: str):

    # Относительный путь к изображению
    image_path = os.path.join(BASE_DIR, 'image_button', 'bd_error.png')
    assert os.path.exists(image_path), f"Файл не найден по указанному пути: {image_path}"
    close_alert_path = os.path.join(BASE_DIR, 'image_button', 'close_red_alert.png')
    assert os.path.exists(close_alert_path), f"Файл не найден по указанному пути: {close_alert_path}"
    
    try:
        # Проверям алерт
        if find_and_interact(image_path, title, close_alert_path):
            logger.debug("Алерт обнаружен и закрыт")
            return True
        else:
            logger.debug("Алерт не обнаружен или не закрыт")
            return False

    except Exception as e:
        logger.exception(f"Ошибка: {e}")


# Поиск алерта ошибки clone error
def red_alert_clone_error(title: str):

    # Относительный путь к изображению
    image_path = os.path.join(BASE_DIR, 'image_button', 'clone_error.png')
    assert os.path.exists(image_path), f"Файл не найден по указанному пути: {image_path}"
    close_alert_path = os.path.join(BASE_DIR, 'image_button', 'close_red_alert.png')
    assert os.path.exists(close_alert_path), f"Файл не найден по указанному пути: {close_alert_path}"

    try:
        # Проверям алерт
        if find_and_interact(image_path, title, close_alert_path):
            logger.debug("Алерт обнаружен и закрыт")
            return True
        else:
            logger.debug("Алерт не обнаружен или не закрыт")
            return False

    except Exception as e:
        logger.exception(f"Ошибка: {e}")
