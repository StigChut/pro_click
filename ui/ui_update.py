import os

from my_logger import logger, BASE_DIR
from update.auto_update import perform_fresh_update, perform_stable_update

def run_fresh_update():
    try:
        perform_fresh_update()
        print("Обновление завершено")
    except Exception as e:
        logger.exception(f"Error: {e}")
        print(f"Error: {e}")


def run_stable_update():

    try:
        perform_stable_update()
        print("Обновление завершено")
    except Exception as e:
        logger.exception(f"Error: {e}")
        print(f"Error: {e}")