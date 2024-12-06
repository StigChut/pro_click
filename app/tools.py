"""
Модуль cодержит функции:
короткой записи,
рандомных задежек,
записи магазина и склада
...
"""

import func.defalt_state
import func.find_buttons
import func.humanity

import pygetwindow
import random
import time
import sys

from my_logger import logger
from pynput import mouse


# Вызов и логгирование
def safe_execute(action, success_message, failure_message, *args, **kwargs):
    """
    Функция для безопасного вызова callable (функция/метод)
    Возвращает результат работы `action`, либо None в случае ошибки.
    
    :param action: вызываемая функция
    :param success_message: сообщение при успешном выполнении
    :param failure_message: сообщение при неуспешном завершении
    :param *args: позиционные аргументы для функции action
    :param **kwargs: именованные аргументы для функции action
    :return: результат работы action либо None, если произошла ошибка
    """
    try:
        logger.info(f"Вызов функции {action.__name__} с аргументами args={args}, kwargs={kwargs}")
        result = action(*args, **kwargs)  # Выполнение функции
        if result:  # Если результат действия положительный (например, True)
            logger.debug(success_message)
        else:       # Если результат действия - False
            logger.info(failure_message)
        return result  # Возвращаем результат самой вызываемой функции
    except Exception as e:
        logger.exception(f"Ошибка выполнения действия {action.__name__}: {e}")
        return None  # Возвращаем None в случае исключения


# Задержки
def wait_random_delay(min_delay=0.1, max_delay=0.4):
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)


# Выбор магазина и склада
def save_data_slot():
    try:
        magazine = input("Название магазина в котором ищем слот: ").strip()
        skald = input("Название склада для которого ищем слот: ").strip()

        result = f"{skald}, в {magazine}"

        def on_click(x, y, button, pressed):
            if pressed:
                logger.debug(f'Клик мышкой в точке: {x}, {y}, {button}')
                return False

        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
        
        return result
    
    except Exception as e:
        logger.exception(f"Ошибка: {e}")


# Проверка активного окна
def chek_window(title):
    try:
        active_window = pygetwindow.getActiveWindow()

        # Сравниваем окна
        if active_window is not None and title is not None and active_window.title == title:
            logger.info(f"Активное окно {active_window.title} и {title} соответсвует условиям")
            return True
        
        else:
            logger.error(f"Активное окно {active_window.title} и {title} не соответвствует условиям. Выход из скрипта")
            print("Активное окно не указано или отличается")
            return False
    
    except Exception as e:
        logger.exception(f"Ошибка активного окна: {e}")
        return False


# Проверка состояния дефолтноего положения
def chek_default_satate(title):
    
    max_iter = 2
    coint_iter = 0

    try:
        while coint_iter < max_iter:

            if func.defalt_state.default_state(title) == False:
                coint_iter += 1
                continue
            else:
                return True

        logger.debug("Не смогли найти дефолтное состояние за 2 перезагрузки")
        print("Не найдена стратовая точка")
        return False
    
    except Exception as e:
        logger.exception(f"Ошибка: {e}")
        return False


# Рандомный блок на главном экране
def random_main_screen(title):
        
    if random.random() < 0.05:
        try:
            random_action = random.choice([
                (func.humanity.occasional_click_main_screen, True),
                (func.humanity.occasional_scroll_down, False),
                (func.humanity.occasional_scroll_up, False)
            ])
            if random_action[1]:        
                random_action[0](title)
            else:
                random_action[0]()
            logger.debug("Выбрано рандомное действие на главном экране")
    
        except Exception as e:
            logger.exception(f"Ошибка рандомного действия на главном экране: {e}")
            return False


# Рандомный блок на втором экране
def random_second_screen(title):
    if random.random() < 0.02:
        try:
            if func.humanity.occasional_click_second_screen(title):
                logger.info("Выполнен рандомный клик на втором экране")

        except Exception as e:
            logger.error(f"Ошибка выполнения рандомного клика на втором экране: {e}")
            return False


# Нажитие первой кнопки и перемещение курсора вниз
def click_bt1_moveDown(title):
    try:
        # Проверка первой кнопки
        if func.find_buttons.find_button_bt1(title):
            time.sleep(0.1)
            # Перемещение курсора
            if func.defalt_state.move_cur(title):
                return True
            else:
                logger.debug(f"Ошибка перемещения курсора")
                return False
        else:
            logger.debug(f"Ошибка нажатия первой кнопки")
            return False
    
    except Exception as e:
        logger.exception(f"Ошибка модуля первой кнопки: {e}")
        return False


# Безопастный ввод данных
def safe_input():
    user_input = None

    while not user_input:
        try:
            sys.stdin.flush()
            user_input = input("> ").strip()
            logger.debug(f"{user_input}")
        except EOFError:
            continue
        if not user_input:
            print("Полен не может быть пустым")
            logger.debug("Пустой ввод")
        else:
            break

    return user_input