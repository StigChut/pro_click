#!D:\Case\00.Junk_Code_Py\LickClick\.venv\Scripts\python.exe
import app.choice_user
import app.choice_window
import app.main_logical
import update.stable_update

from my_logger import logger


def main():
    try:
        update.stable_update.check_and_update()

        import keyboard
        # Отображение инструкций
        print(
            "Добро пожаловать в LickClick!\n"
            "'Shift + Q' - чтобы привязать свой username в ТГ, нужно для призыва в оповещениях.\n"
            "'Shift + A' - для того чтобы привязать свой браузер и окно поиска.\n"
            "'Alt + W' - чтобы запустить поиск слотов.\n"
            "'Ctrl + T' - открывает новую вкладку, останавливает скрипт. Либо клик на другое окно.\n"
        )
        
        # Привязка горячих клавиш
        keyboard.add_hotkey('shift+q', app.choice_user.app_choise_user)
        keyboard.add_hotkey('shift+a', app.choice_window.app_choise_window)
        keyboard.add_hotkey('alt+w', app.main_logical.logical_workflow)
        
        # Ожидание нажатий клавиш
        keyboard.wait()
        
    except Exception as e:
        logger.error(f"Ошибка в главной функции: {e}")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Остановка скрипта...")
