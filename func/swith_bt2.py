"""
Модуль ветвления в основном цикле, после получения алерта
с ошибкой диапазона дат.

Нажимает кнопку "Отменить" и ищет кнопку "Выбрать" по координатам ниже 
"""

import pyautogui
import random
import time
import os

from my_logger import logger, BASE_DIR
from func.random_clic import rand_clik
from func.negative_result import red_alert_time_date
from func.find_buttons import find_button_bt3


# Повторный поиск кнопки "Выбрать", ниже текущей
def swith_bt2_down(title: str):
    # Относительный путь к изображению
    image_path_bt2 = os.path.join(BASE_DIR, 'image_button', 'bt2.png')
    assert os.path.exists(image_path_bt2), f"Файл не найден по указанному пути: {image_path_bt2}"
    image_path_undo = os.path.join(BASE_DIR, 'image_button', 'undo.png')
    assert os.path.exists(image_path_undo), f"Файл не найден по указанному пути: {image_path_undo}"

    # Глубина прокрутки
    depth_scroll = random.randint(-700, -400)
    # Счетчики цикла 
    scroll_iter = 0
    # Выбираем максимальное количество прокруток
    max_scroll = random.randint(1, 3)
    # Высота экрана, которую будем учитывать для поиска
    screen_region = pyautogui.size()  # Получаем размер экрана -> (ширина, высота)
    current_y = 0  # Минимум области, выше этого Y мы не ищем (обновляем координату на каждой итерации)
    
    try:
        
        # Основной цикл
        while scroll_iter < max_scroll:
            try:
                button_undo = pyautogui.locateOnScreen(image_path_undo,
                                                      confidence=0.8,
                                                      region=(0, current_y, screen_region.width, screen_region.height - current_y)
                                                      )
                # Если нашли "Отмена"
                if button_undo is not None and rand_clik(button_undo):
                    logger.debug(f"Нажата кнопка 'Выбрать' в области: {button_undo}")

                    # Обновляем минимальный Y для поиска (теперь ищем ниже на экране)
                    current_y = button_undo.top + button_undo.height
                    logger.debug(f"Текущая координата {current_y}")
                # Ищем на экране кнопку "Выбрать", но только в области ниже `current_y`
                button_two = pyautogui.locateOnScreen(image_path_bt2,
                                                      confidence=0.8,
                                                      region=(0, current_y, screen_region.width, screen_region.height - current_y)
                                                      )
                
                # Если нашли "Выбрать"
                if button_two is not None and rand_clik(button_two):
                    logger.debug(f"Нажата кнопка 'Выбрать' в области: {button_two}")
                    
                    # Обновляем минимальный Y для поиска (теперь ищем ниже на экране)
                    current_y = button_two.top + button_two.height
                    logger.debug(f"Текущая координата {current_y}")

                    # Нажимаем "Запланировать"
                    if find_button_bt3(title) == True and red_alert_time_date(title) == False:
                        time.sleep(3)
                        break
                            
            except pyautogui.ImageNotFoundException as e:
                logger.debug(f"Не нашли изображение {e}")
                pass

            # Если скролл всё-таки нужен
            pyautogui.scroll(depth_scroll)
            time.sleep(0.15)
            scroll_iter += 1
            logger.info(f"Прокрутка экрана: ({scroll_iter}/{max_scroll} попыток)")

        # Если не нашли за скроллы - выходим
        if scroll_iter >= max_scroll:
            pyautogui.press('esc')
            logger.debug("Кнопка 'Выбрать' не найдена, нажата ESC")
            return False

    except Exception as e:
        logger.exception(f"Ошибка: {e}")     
