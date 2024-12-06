""" Модуль для рандомного клика по полученному изображению """

import pyautogui
import random

from my_logger import logger


def rand_clik(image_button):
    try:
        if image_button is not None:
            # Достаем координаты изображения
            button_left_top_x = image_button.left
            button_left_top_y = image_button.top
            button_width = image_button.width
            button_height = image_button.height

            # Генерация случайных координат
            random_x = random.randint(button_left_top_x, button_left_top_x + button_width)
            random_y = random.randint(button_left_top_y, button_left_top_y + button_height)
            logger.debug(f"Координаты для {image_button}: x: {random_x}, y: {random_y}")

            # Делаем клик
            pyautogui.click(random_x, random_y)
            return True
        else:
            logger.debug(f"Кнопка {image_button} не найдена.")
            return False
    except Exception as e:
        logger.exception(f"Ошибка рандомного клика: {e}")
        return False