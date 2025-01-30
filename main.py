from my_logger import logger
from gui import run_gui
from update.auto_update import perform_stable_update


def main():
    try:
        perform_stable_update()
        print("Добро пожаловать...")
        
    except Exception as e:
        logger.error(f"Ошибка в главной функции: {e}")

if __name__ == '__main__':
    try:
        main()
        run_gui()
    except KeyboardInterrupt:
        print("Остановка скрипта...")
        