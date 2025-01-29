import tkinter as tk

from ui.ui_data_slot import open_user_input_slot
from ui.ui_tg_username import open_user_input_window
from ui.ui_active_window import choose_active_window
from ui.ui_update import run_fresh_update, run_stable_update
from app.booking_logical import logical_workflow_booking
from app.transfer_logical import logical_workflow_transfer

def create_button(root, text, command, pady=20):
    button = tk.Button(root, text=text, command=command)
    button.pack(pady=pady)
    return button

def safe_command(command):
    def wrapper():
        try:
            command()
        except Exception as e:
            print(f"Ошибка: {e}")
    return wrapper

# Главное окно приложения
root = tk.Tk()
root.title("Главное окно")
root.geometry("300x500")

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Создание кнопок
create_button(button_frame, "Запустить бронирование", safe_command(logical_workflow_booking))
create_button(button_frame, "Запустить перенос", safe_command(logical_workflow_transfer))
create_button(button_frame, "Записать слот, магазин", lambda:open_user_input_slot(root))
create_button(button_frame, "Выбрать активное окно", lambda: choose_active_window(root))
create_button(button_frame, "Привязать Телеграмм", lambda: open_user_input_window(root))
create_button(button_frame, "stable update", safe_command(run_stable_update))
create_button(button_frame, "fresh update", safe_command(run_fresh_update))

root.mainloop()