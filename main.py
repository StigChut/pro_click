<<<<<<< HEAD
=======
#!D:\Case\00.Junk_Code_Py\LickClick\.venv\Scripts\python.exe
import app.choice_user
import app.choice_window
import app.booking_logical

>>>>>>> debug
from my_logger import logger
from update.auto_update import perform_stable_update


def main():
    try:
<<<<<<< HEAD
        perform_stable_update()
=======

>>>>>>> debug
        print("Добро пожаловать. Для начала работы перезапустите программу.")
        
    except Exception as e:
        logger.error(f"Ошибка в главной функции: {e}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Остановка скрипта...")
        