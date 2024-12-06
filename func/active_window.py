import pygetwindow
import json
import os

from pynput import mouse
from my_logger import logger

FILE = 'temp.json'

""" Функции для взаимодействия с JSON """

# Сохранение файла
def save_file(data):
    try:
        # Проверка существования файла, если существует загружаем
        if os.path.exists(FILE):
            with open(FILE, 'r', encoding='utf8') as f:
                current_data = json.load(f)
        # Если фйла нет, пустой словарь
        else:
            current_data = {}
        
        # Обновление данных
        current_data.update(data)

        # Сохрание обновленных данных
        with open(FILE, 'w', encoding='utf-8') as f:
            json.dump(current_data, f, ensure_ascii=False, indent=4)
        logger.debug("Данные сохранены в файл")
    
    except json.JSONDecodeError as e:
        logger.exception(f"Ошибка декодирования JSON в файле {FILE}: {e}")
        
    except Exception as e:
        logger.exception(f"Ошибка чтения активного окна: {e}")


# Чтение файла с сохраненным активным окном
def read_file(key):
    try:
        # Проверка соществования файла
        if not os.path.exists(FILE):
            logger.debug("Файл не найден")
        
        # Открываем и читаем файл
        with open(FILE, 'r', encoding='utf-8') as f:
            current_data = json.load(f)
        
        # Получаем значение по ключу
        value = current_data.get(key, None)
        logger.debug("Прочитали файл и получили значение по ключу")
        return value
    except FileNotFoundError:
        logger.exception(f"Файл {FILE} не найден")
    
    except json.JSONDecodeError as e:
        logger.exception(f"Ошибка декодирования JSON в файле {FILE}: {e}")

    except Exception as e:
        logger.exception(f"Ошибка чтения активного окна: {e}")



""" Функция выбора активного окна браузера и взаимодействия с пользоватем """


# Клик
def on_click(x, y, button, pressed):
    if pressed:
        logger.debug(f'Клик мышкой в точке: {x}, {y}, {button}')
        return False


# Получаем активное окно пользователя
def active_window():
    try:
        print("Режим выбора активного окна...")

        # Ожидание клика
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()

        # Получение активного окна
        window = pygetwindow.getActiveWindow()
        
        # Проверка на наличие активного окна
        if not window:
            print("Активное окно отсутствует")
            logger.debug("Активное окно отсутствует")
            return
        print(f"Активное окно: {window.title}")
        
        # Пользовательский ввод
        user_input = input("Eсли верно нажми Y, если нет N: ").strip().upper()
        
        # Условия ввода
        if user_input == "Y":
                # Делаем словарь
                window_data = {'title': window.title}
                print(f"Активное окно {window_data} сохранено")
                # Сохраняем в файл
                if save_file(window_data):
                    logger.debug(f"Активное окно {window_data} сохранено")
                    return True
                
                else:
                    return False
        
        elif user_input == "N":
            print("Попробуйте снова")
            logger.debug("Попробуйте снова")
        
        else:
            print("Некорректный ввод")
            logger.debug("Некорректный ввод")
    
    except Exception as e:
        logger.exception(f"Ошибка получения активного окна: {e}")
        raise

