"""
    Модуль поиска дефолтного состояния
    и стандартного положения курсора после bt1
"""

import pyautogui
import time
import os

from my_logger import logger, BASE_DIR
from func.image_screen import find_and_interact


# Поиск стартового полежения на экране для того чтобы начать выполение скрипта
def default_state(title: str):
    # Относительный путь к изображению
    image_path = os.path.join(BASE_DIR, 'image_button', 'default_state.png')
    assert os.path.exists(image_path), f"Файл не найден по указанному пути: {image_path}"

    try:
        if find_and_interact(image_path, title):
            return True
        else:
            pyautogui.press('f5')
            time.sleep(5)
            logger.debug("Не найдено дефолтное состояние скрипта. Выполнена перезагрузка страницы")
            return False
    except Exception as e:
        logger.exception(f"Ошибка: {e}")
        raise


# TODO: Перемещение курсора в область image_for_moveCur после bt1
def move_cur(title):
    try:
        # Относительный путь к изображению
        image_path = os.path.join(BASE_DIR, 'image_button', 'image_for_moveCur.png')
        assert os.path.exists(image_path), f"Файл не найден по указанному пути: {image_path}"

        # Определяем изображение
        image = pyautogui.locateOnWindow(image_path, title, confidence=0.5)

        # Проверяем, что изображение найдено
        if image is None:
            logger.debug(f"Изображение {image_path} не найдено в активном окне")
            raise ValueError(f"Изображение {image_path} не найдено для заголовка {title}")

        # Определяем регион
        region = (int(image.left), int(image.top), int(image.width), int(image.height))
        logger.debug(f"Регион: {region}")

        # Вычисляем центр координат
        center_x = int(region[0] + region[2] / 2)
        center_y = int(region[1] + region[3] / 2)
        logger.debug(f"center_x: {center_x}, center_y: {center_y}, для изображения")

        # Перемещаем курсор
        pyautogui.moveTo(center_x, center_y, duration=0.1)
        logger.debug(f"Курсор перемещен в координаты {center_x}, {center_y}")
        return True
    
    except pyautogui.ImageNotFoundException:
        pass

    except Exception as e:
        logger.exception(f"Ошибка перемещения курсора после bt1: {e}")
        return False


