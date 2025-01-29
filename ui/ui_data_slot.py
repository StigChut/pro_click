import tkinter as tk
from tkinter import messagebox

from my_logger import logger
from func.active_window import save_file

# Локальные уведомления (всплывающее окно)
def popup_info(message):
    messagebox.showinfo("Информация", message)

def popup_error(message):
    messagebox.showerror("Ошибка", message)

def input_data_slot(entry_mag, entry_slot, window):
    """
    Ввод данных пользователем
    """
    try:
        magasine = entry_mag.get().strip()
        sklad = entry_slot.get().strip()

        data = {'tg_lable': f"{sklad}, в {magasine}"}
        save_file(data)

        popup_info(f"Успешное сохранение {data}")
        logger.debug("Слот и магазины успешно сохранены")

        window.destroy()

    except Exception as e:
        popup_error("Ошибка сохранения данных")
        logger.debug(rf"Ошибка сохранения слота\магазина: {e}")

def open_user_input_slot(root):
    try:
        # Создаем новое окно
        input_window = tk.Toplevel(root)
        input_window.title("Ввод данных")
        input_window.geometry("350x150")
        input_window.transient(root)
        input_window.grab_set()

        # Фрейм для ввода данных
        input_frame = tk.Frame(input_window)
        input_frame.pack(padx=10, pady=10)

        # Поля ввода
        label_magazine = tk.Label(input_frame, text="Название магазина:")
        label_sklad = tk.Label(input_frame, text="Название склада:")

        label_magazine.grid(row=0, column=0, padx=10, pady=10)
        label_sklad.grid(row=1, column=0, padx=10, pady=10)

        entry_magazine = tk.Entry(input_frame)
        entry_sklad = tk.Entry(input_frame)

        entry_magazine.grid(row=0, column=1, padx=10, pady=10)
        entry_sklad.grid(row=1, column=1, padx=10, pady=10)

        # Кнопка подтверждения
        submit_button = tk.Button(
            input_frame,
            text="Подтвердить",
            command=lambda: input_data_slot(entry_magazine, entry_sklad, input_window)
        )
        submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    except Exception as e:
        popup_error("Ошибка")
        logger.debug(f"Ошибка: {e}")