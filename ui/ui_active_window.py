import tkinter as tk
import pygetwindow
import time

from pynput import mouse
from tkinter import messagebox
from my_logger import logger
from func.active_window import save_file

# Глобальная переменная для хранения активного окна
active_window_data = None

# Функция обработки щелчка мышкой
def on_click(x, y, button, pressed):
    if pressed:
        logger.debug(f'Клик мышкой в точке: {x}, {y}, {button}')
        return False  # Остановить слушателя после первого щелчка
    
# Локальные уведомления (всплывающее окно)
def popup_info(message):
    messagebox.showinfo("Информация", message)

def popup_error(message):
    messagebox.showerror("Ошибка", message)

# Основная логика выбора активного окна
def get_active_window():
    try:
        # Вводим в режим выбора окна
        popup_info("Режим выбора активного окна. Щелкните мышью на рабочем столе!")
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()  # Ждем клика

        time.sleep(0.2)  # Короткая пауза для корректного определения активного окна
        window = pygetwindow.getActiveWindow()

        # Проверяем наличие активного окна
        if not window:
            popup_error("Активное окно отсутствует. Попробуйте еще раз!")
            return None

        # Возвращаем данные активного окна
        return {'title': window.title}

    except Exception as e:
        logger.exception(f"Ошибка получения активного окна: {e}")
        popup_error(f"Ошибка получения активного окна: {e}")
        return None

# Создание модального окна подтверждения
def create_window_confirmation(root, active_data):
    # Создаем новое окно для подтверждения
    confirmation_window = tk.Toplevel(root)
    confirmation_window.title("Подтверждение выбора")
    confirmation_window.geometry("400x200")

    # Сообщение пользователю
    tk.Label(confirmation_window, text=f"Активное окно: {active_data['title']}", wraplength=350, justify="center").pack(pady=10)

    # Кнопка для подтверждения
    tk.Button(confirmation_window, text="Сохранить",
              command=lambda: save_active_window(confirmation_window, active_data)).pack(side="left", padx=20, pady=20)

    # Кнопка для повторного выбора
    tk.Button(confirmation_window, text="Выбрать снова",
              command=lambda: (confirmation_window.destroy(), choose_active_window(root))).pack(side="right", padx=20, pady=20)

# Кнопка "Сохранить"
def save_active_window(confirmation_window, active_data):
    # Логика сохранения данных
    if save_file(active_data):
        logger.debug(f"Активное окно '{active_data}' успешно сохранено!")
        confirmation_window.destroy()
        popup_info(f"Активное окно '{active_data['title']}' сохранено!")
    else:
        popup_error("Ошибка при сохранении окна. Проверьте файл или доступ для записи!")


# Логика выбора активного окна
def choose_active_window(root):
    active_data = get_active_window()
    if active_data:
        # Показываем подтверждение в новом окне
        create_window_confirmation(root, active_data)



