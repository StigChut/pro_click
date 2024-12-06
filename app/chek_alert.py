""" Модуль ветвления после кнопки "Запланировать". """

import time

import func.positive_result
import func.negative_result
import func.swith_bt2

from my_logger import logger


def alert_handler(title):
    
    alert_timeout = 15
    start_time = time.time()

    try:
        while True:

            # Положительный результат
            if func.positive_result.green_alert(title) or func.positive_result.button_trasfer(title):
                logger.info("Слот забронирован")
                time.sleep(1)
                return "success"
            
            # Отрицательный результат
            elif func.negative_result.red_alert(title):
                logger.info("Слот не забронирован. Не успели. Пробуем снова")
                time.sleep(1)
                return "repeat"
            
            elif func.negative_result.red_alert_time_date(title):
                logger.info("Слот не забронирован. Ошибка дипазаона дат.")
                func.swith_bt2.swith_bt2_down(title)
                logger.info("Просмотрели все кнопки 'Выбрать' ниже")
                time.sleep(1)
                return "repeat"
            
            elif func.negative_result.red_alert_error_bd(title):
                logger.info("Ошибка базы данных ВБ. Выход из скрипта")
                time.sleep(1)
                return "error"
            
            elif func.negative_result.red_alert_clone_error(title):
                logger.info("Ошибка базы данных ВБ. Выход из скрипта")
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


















