#!D:\Case\00.Junk_Code_Py\LickClick\.venv\Scripts\python.exe
import tkinter as tk

from ui.ui_tg_username import open_user_input_window
from ui.ui_active_window import choose_active_window
from ui.ui_update import run_fresh_update, run_stable_update
from app.booking_logical import logical_workflow_booking
from app.transfer_logical import logical_workflow_transfer

# Главное окно приложения
root = tk.Tk()
root.title("Главное окно")
root.geometry("400x600")

# Кнопка для открытия окна с привязкой тг
btn_open = tk.Button(root, text="Привязать Телеграмм", command=open_user_input_window)
btn_open.pack(pady=20)

# Кнопка запуска выбора окна
btn_window = tk.Button(root, text="Выбрать активное окно", command=lambda: choose_active_window(root))
btn_window.pack(pady=20)

# Обновление
btn_stable_up = tk.Button(root, text="stable update", command=run_stable_update)
btn_stable_up.pack(pady=20)
btn_fresh_up = tk.Button(root, text="fresh update", command=run_fresh_update)
btn_fresh_up.pack(pady=20)

# Запуск основной функции
btn_booking = tk.Button(root, text="Запустить бронирование", command=logical_workflow_booking)
btn_booking.pack(pady=20)

btn_booking = tk.Button(root, text="Запустить перенос", command=logical_workflow_transfer)
btn_booking.pack(pady=20)


root.mainloop()