"""
Функция на хоткеях Alt+W

Основная логика работы приложения:

1. Читаем и сохраням активное окно из фала Temp.json
2. Проверяем что находимся в дефолтной точке окна, иначе перезагружам страницу
    - Если выполнена перезагрузка, но дефолтного состояния нет
        - Останавливаем скрипт, пуш в ТГ
...
Выполням рандомный клик\прокрутку на главном экране
Рандомный интервал 5 - 10 минут 
...
3. Ишем\нажимаем кнопку "Запланировать поставку"
...
Выполняем рандомный клик на втором экране
Интервал 10 - 15 минут
...
4. Ищем\нажимаем кнопку "Выбрать"
4.1 Если кнопка "Выбрать" найдена
    1. Ищем\нажимаем кнопку "Запланировать"
    1.1 Ищем алерты
        - Если нашли красный о том что уже запланирована
            - Закрываем его
            - Возвращаемся к п.2
        - Если нашли красный о том что дата не подходит
            - Закрываем его
            - Выполням п.2 снова. Ищем кнопку выбрать ниже
        - Если нашли зеленый
            - Останавливаем скрипт, пуш в ТГ
4.2 Если кнопка "Выбрать" не найдена
    1. Возвращаемся к п.2
"""
import func.defalt_state
import func.find_buttons

import app.tools
import push_service.messge_handler

import func
import func.active_window

from app.chek_alert import alert_handler
from push_service.config import GREEN_MESSAGE, STOP_MESSAGE, ERROR_MESSAGE
from my_logger import logger



def logical_workflow():
    """
    Alt + W
    Основной скрипт и логика работы
    """

    # Чтение активного окна из файла
    title = app.tools.safe_execute(
        func.active_window.read_file,
        "Чтение из файла активного окна - ДА",
        "Чтение из файла активного окна - НЕТ",
        "title"
    )

    # Чтение имя пользователя в Телеграмм
    username = app.tools.safe_execute(
        func.active_window.read_file,
        "Чтение из файла username - ДА",
        "Чтение из файла username - НЕТ",
        "username"
    )
    
    # Проеделяем название магазина и склада, который будем искать
    magazine_and_sklad = app.tools.safe_execute(
        app.tools.save_data_slot,
        "Описание итерации - ДА",
        "Описание итерации - НЕТ"
    )

    try:
        # Флаг для проверки выхода
        exited_by_success = False
        print("Поиск слотов запущен - ДА")

        # Разворачиваем основной цикл
        while True:
            
            # Задежка перед запуском
            app.tools.wait_random_delay()

            # Проверка соответсвия окон
            if not app.tools.safe_execute(
                app.tools.chek_window,
                "Окна совпадают - ДА",
                "Окна совпадают - НЕТ",
                title
            ):
                break
            
            # Проверка дефолтного состояния
            if not app.tools.safe_execute(
                app.tools.chek_default_satate,
                "Стартовая точка - ДА",
                "Стартовая точка - НЕТ",
                title
            ):
                break

            # Рандомное действие на главном экране
            if not app.tools.safe_execute(
                app.tools.random_main_screen,
                "Случайное действие - ДА",
                "Случайное действие - НЕТ",
                title
            ):
                pass

            # Поиск кнопки "Запланировать поставку"
            if not app.tools.safe_execute(
                app.tools.click_bt1_moveDown,
                "Запланировать поставку - ДА",
                "Запланировать поставку - НЕТ",
                title
            ):
                break
            
            # Задержка
            app.tools.wait_random_delay()

            # Рандомное действие на втором жкране
            if not app.tools.safe_execute(
                app.tools.random_second_screen,
                "Случайное действие - ДА",
                "Случайное действие - НЕТ",
                title
            ):
                pass

            # Поиск кнопки "Выбрать"
            if not app.tools.safe_execute(
                func.find_buttons.find_button_bt2,
                "Выбрать - ДА",
                "Выбрать - НЕТ",
                title
            ):
                continue
            
            else:

                # Поиск кнопки "Запланировать" 
                if not app.tools.safe_execute(
                    func.find_buttons.find_button_bt3,
                    "Запланировать - ДА",
                    "Запланировать - НЕТ",
                    title
                ):
                    break
                
                # Успешно нажили "Запланировать"
                else:
                    # Обработка алертов
                    alert_status = app.tools.safe_execute(
                        alert_handler,
                        "Проверка алертов - ДА",
                        "Проверка алертов- НЕТ",
                        title
                    )

                    if alert_status == "success":
                        """
                        app.tools.safe_execute(
                            push_service.messge_handler.push_message,
                            "Пуш в ТГ - ДА",
                            "Пуш в ТГ - НЕТ",
                            username,
                            GREEN_MESSAGE,
                            magazine_and_sklad
                        )
                        """
                        exited_by_success = True
                        break
                    
                    elif alert_status in ["repeat", "timeout"]:
                        continue

                    elif alert_status == "error":
                        break

        # Выполняется только если выход из цикла не по "success"
        if not exited_by_success:
            """
            print("Поиск слотов остановлен - ДА")
            app.tools.safe_execute(
                push_service.messge_handler.push_message,
                "Выход из цикла - ДА",
                "Выход из цикла - НЕТ",
                username,
                STOP_MESSAGE,
                magazine_and_sklad
            )
            """
    except Exception as e:
        app.tools.safe_execute(
            push_service.messge_handler.push_message,
            "Критическая ошибка - ДА",
            "Критическая ошибка - НЕТ",
            username,
            ERROR_MESSAGE,
            magazine_and_sklad
        )
        logger.exception(f"Ошибка в основном цикле: {e}")