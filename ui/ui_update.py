import os

from my_logger import logger, BASE_DIR
from update.fresh_update import perform_fresh_update
from update.stable_update import check_stable_update

def run_fresh_update():
    try:
        perform_fresh_update()
        print("Обновление завершено")
    except Exception as e:
        logger.exception(f"Error: {e}")
        print(f"Error: {e}")


def run_stable_update():

    try:
        check_stable_update()
        print("Обновление завершено")
    except Exception as e:
        logger.exception(f"Error: {e}")
        print(f"Error: {e}")