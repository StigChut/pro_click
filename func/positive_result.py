""" Модуль содержит функции для отработки позитивного сценария
Когда нашли зерелный алерт или кнопку "Редактировать заказ" """

import pyautogui
import os

from my_logger import logger, BASE_DIR
from func.image_screen import find_and_interact


def green_alert(image_path, title: str):
    """ Поиск алерта после нажатия кнопки "Запланировать" или "Переместить" """
    
    try:
        # Проверяем алерт
        if find_and_interact(image_path, title):
            logger.debug("Алерт обнаружен")
            return True
        else:
            logger.debug("Алерт не обнаружен")
            return False
        
    except Exception as e:
        logger.exception(f"Ошибка: {e}")


# Поиск кнопки "Перенести поставку", если алерт пропущен по каким-то причинам
def button_trasfer(title: str):
    # Относительный путь к изображению
    image_path = os.path.join(BASE_DIR, 'image_button', 'transer_button.png')
    assert os.path.exists(image_path), f"Файл не найден по указанному пути: {image_path}"

    try:
        # Проверяем кнопку
        if find_and_interact(image_path, title):
            logger.debug("Кнопка обнаружена")
            return True
        else:
            logger.debug("Кнопка не обнаружена")
            return False
        
    except Exception as e:
        logger.exception(f"Ошибка: {e}")
         