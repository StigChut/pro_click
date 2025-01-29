import tkinter as tk

from tkinter import messagebox
from my_logger import logger
from func.active_window import save_file

# Уведомления 
def popup_info(message):
    messagebox.showinfo("Информация", message)

def popup_error(message):
    messagebox.showerror("Ошибка", message)

