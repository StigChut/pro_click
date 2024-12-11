""" Модуль рандомных действий на первом и втором экране """

import pyautogui
import random
import time
import os

from my_logger import logger, BASE_DIR
from func.image_screen import find_and_interact


# Поиск изображения на главном экране и рандомный клик на него
def occasional_click_main_screen(title: str):
    # Относительный путь к изображениям
    path_main_screen_click = os.path.join(BASE_DIR, 'image_button', 'main_screen_clic_new.png')
    assert os.path.exists(path_main_screen_click), f"Файл не найден по указанному пути: {path_main_screen_click}"
    try:
        # Ищем изображение на главном экране
        if find_and_interact(path_main_screen_click, title, self_click=True):
            logger.debug("Выполнен рандомный клик")
            return True
        else:
            logger.debug("Не выполнен рандомный клик")
            return False
    except Exception as e:
        logger.exception(f"Ошибка: {e}")


# Поиск изображения на втором, после клика на bt1 экране и рандомный клик на него
def occasional_click_second_screen(title: str):
    # Относительный путь к изображениям
    path_after_bt1_click = os.path.join(BASE_DIR, 'image_button', 'after_bt1_click.png')
    assert os.path.exists(path_after_bt1_click), f"Файл не найден по указанному пути: {path_after_bt1_click}"
    path_after_bt1_click2 = os.path.join(BASE_DIR, 'image_button', 'after_bt1_click2.png')
    assert os.path.exists(path_after_bt1_click2), f"Файл не найден по указанному пути: {path_after_bt1_click2}"

    try:
        # Выбираем надомный путь к изображению
        r_path = random.choice([path_after_bt1_click, path_after_bt1_click2])

        # Ищем изображение на второстепенном экране
        if find_and_interact(r_path, title, self_click=True):
            logger.debug(f"Выбрали {r_path} и кликнули на него")
            return True
        else:
            logger.debug(f"Ошибка в выборе второго изображения: {r_path}")
            return False

    except Exception as e:
        logger.exception(f"Ошибка: {e}")


# Рандомные прокрутки вниз на главном экране
def occasional_scroll_down():
    try:
        # Глубина прокрутки вниз
        depth_down = random.randint(-30, -5)
        logger.debug(f"depth_down: {depth_down}")

        logger.debug("Выполняется рандомная прокрутка")
        # Прокрутка
        time.sleep(0.1)
        pyautogui.scroll(depth_down)
        time.sleep(0.1)
    except Exception as e:
        logger.exception(f"Ошибка: {e}")


# Рандомные прокрутки вверх на главном экране
def occasional_scroll_up():
    try:
        # Глубина прокрутки вверх
        depth_up = random.randint(10, 40)
        logger.debug(f"depth_up: {depth_up}")

        logger.debug("Выполняется рандомная прокрутка")
        # Прокрутка
        time.sleep(0.1)
        pyautogui.scroll(depth_up)
        time.sleep(0.1)
    except Exception as e:
        logger.exception(f"Ошибка: {e}")