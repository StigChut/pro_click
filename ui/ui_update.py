import os

from my_logger import logger, BASE_DIR
<<<<<<< HEAD
from update.auto_update import perform_fresh_update, perform_stable_update

def run_fresh_update():
    try:
        perform_fresh_update()
=======
from update.fresh_update import check_fresh_update
from update.stable_update import check_stable_update

def run_fresh_update():

    try:
        check_fresh_update()
>>>>>>> debug
        print("Обновление завершено")
    except Exception as e:
        logger.exception(f"Error: {e}")
        print(f"Error: {e}")


def run_stable_update():

    try:
<<<<<<< HEAD
        perform_stable_update()
=======
        check_stable_update()
>>>>>>> debug
        print("Обновление завершено")
    except Exception as e:
        logger.exception(f"Error: {e}")
        print(f"Error: {e}")