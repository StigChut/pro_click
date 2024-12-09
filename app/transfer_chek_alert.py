import os
import time

import func.positive_result
import func.negative_result
import func.swith_bt2

from my_logger import logger, BASE_DIR


def alert_handler(image_bt3, title):
    """ Модуль ветвления после кнопки "Запланировать". """
    image_green = os.path.join(BASE_DIR, 'image_button', 'transfer_green_alert.png')
    assert os.path.exists(image_green), f"Файл не найден по указанному пути: {image_green}"

    image_alert = os.path.join(BASE_DIR, 'image_button', 'transfer_red_alert_date.png')
    assert os.path.exists(image_alert),  f"Файл не найден по указанному пути: {image_alert}"

    alert_timeout = 15
    start_time = time.time()

    try:
        while True:

            # Положительный результат
            if func.positive_result.green_alert(image_green, title):
                logger.info("Поставка перенесана")
                time.sleep(1)
                return "success"
            
            # Негативный результат
            elif func.negative_result.red_alert_time_date(image_alert, title):
                logger.debug("Выбрали туже дату, начинам искать ниже")
                func.swith_bt2.swith_bt2_down(image_bt3, image_alert, title)
                logger.info("Посмотрели все кнопки 'Выбрать' ниже")
                time.sleep(1)
                return "repeat"

            elif func.negative_result.red_alert_error_bd(title):
                logger.info("Ошибка базы данных ВБ. Выход из скрипта")
                time.sleep(1)
                return "error"
            
            elif func.negative_result.red_alert_clone_error(title):
                logger.info("Ошибка фунции. Выход из скрипта")
                time.sleep(1)
                return "error"
            
            # Таймаут на ожидание
            if time.time() - start_time > alert_timeout:
                logger.info("Не дождались алертов перехода за 15 сек.")
                return "timeout"
            
            # Шаг проверки
            time.sleep(0.5)
    
    except Exception as e:
        logger.exception(f"Ошибка: {e}")
        return "error"