""" Модуль поиска кнопок в осовном цикле """

import pyautogui
import random
import time
import os

from my_logger import logger, BASE_DIR
from func.image_screen import find_and_interact


def find_button_bt1(image_path, title: str):
    """ Поиск первой кнопки в итерации """

    try:
        # Ищем первую кнопку "bt1"
        if find_and_interact(image_path, title, self_click=True):
            logger.debug("Кнопка 'Запланировать' нажата")
            return True
        else:
            logger.debug("Кнопка 'Запланировать поставку' не нажата")
            return False
        
    except Exception as e:
        logger.exception(f"Ошибка нажатия bt1: {e}")
        raise


# Поиск кнопки "Выбрать"
def find_button_bt2(title: str, mode=["booking", "transfer"]):
    """
    Функция для поиска кнопки "Выбрать"
    param: mode - booking - бронирование, transfer - перенос
    """

    # Относительный путь к изображению
    image_path = os.path.join(BASE_DIR, 'image_button', 'bt2.png')
    assert os.path.exists(image_path), f"Файл не найден по указанному пути: {image_path}"

    if mode == "booking":
        # Глубина прокрутки
        depth_scroll = random.randint(-700, -400)
        # Счетчики цикла 
        max_scroll = random.randint(2, 4)
    elif mode == "transfer":
        # Глубина прокрутки
        depth_scroll = -900
        # Счетчики цикла 
        max_scroll = 1

    scroll_iter = 0

    try:
        # Основной цикл
        while scroll_iter < max_scroll:
            
            pyautogui.scroll(depth_scroll)
            time.sleep(0.4)

            # Ищем на экране кнопку Выбрать
            if find_and_interact(image_path, title, self_click=True):
                logger.debug(f"Нажата кнопка 'Выбрать'")
                return True
            
            time.sleep(0.4)
            scroll_iter += 1
            logger.info(f"Прокрутка экрана: ({scroll_iter}/{max_scroll} попыток)")
        
        # Если не нашли за скроллы выходим
        if scroll_iter >= max_scroll:
            pyautogui.press('esc')
            logger.debug("Кнопка 'Выбрать не найдена, нажат ESC'")
            return False
        
    except Exception as e:
        logger.exception(f"Ошибка нажатия bt2: {e}")
        raise



def find_button_bt3(image_path, title: str):
    """ Поиск третьей кнопки в итерации """
    
    try:
        # Ищем третью кнопку bt3
        if find_and_interact(image_path, title, self_click=True):
            logger.debug(f"Нажата кнопка 'Запланировать'")
            return True
        else:
            logger.debug(f"Кнопка 'Запланировать' не нажата")
            return False
    except Exception as e:
        logger.exception(f"Ошибка нажатия bt3: {e}")
        raise