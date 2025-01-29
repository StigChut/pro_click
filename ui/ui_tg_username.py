import tkinter as tk

from tkinter import messagebox
from my_logger import logger
from func.active_window import save_file

# Локальные уведомления (всплывающее окно)
def popup_info(message):
    messagebox.showinfo("Информация", message)

def popup_error(message):
    messagebox.showerror("Ошибка", message)


def handle_user_input(entry_field, window):
    """
    Обработка ввода пользователя
    """
    try:
        # Получаем и обрабатываем текст, введенный пользователем
        user_input = entry_field.get().strip()
        logger.debug(f"Пользователь ввел: {user_input}")

        # Преобразование имени пользователя
        if "https://t.me/" in user_input:
            username = user_input.split("https://t.me/")[-1].strip()
        else:
            username = user_input.strip()

        # Проверяем валидность username
        if not username:
            popup_error("Имя пользователя не может быть пустым!")
            return

        # Сохраняем данные
        user_data = {'username': username}
        save_file(user_data)

        # Успешное уведомление
        popup_info(f"Имя пользователя '{username}' сохранено!")
        logger.debug("Имя пользователя успешно сохранено!")

        # Закрываем окно ввода
        window.destroy()

    except Exception as e:
        logger.exception("Произошла ошибка при сохранении данных.")
        popup_error("Не удалось сохранить имя пользователя. Попробуйте ещё раз.")


def open_user_input_window(root):
    """
    Открывает отдельное окно для ввода имени пользователя
    """
    # Создаем новое окно
    input_window = tk.Toplevel()
    input_window.title("Ввод Telegram Username")
    input_window.geometry("350x200")
    input_window.transient(root)
    input_window.grab_set()


    # Добавляем метку-инструкцию
    label = tk.Label(input_window, text="Введите свой username в Telegram\n(Пример: https://t.me/yesimfine_thanks)", wraplength=300, justify="center")
    label.pack(pady=10)

    # Поле ввода
    entry = tk.Entry(input_window, width=30)
    entry.pack(pady=10)

    # Кнопка для сохранения
    btn_save = tk.Button(input_window, text="Сохранить", command=lambda: handle_user_input(entry, input_window))
    btn_save.pack(pady=10)

    input_window.wait_window(input_window)