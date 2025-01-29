import subprocess
import os

from my_logger import logger, BASE_DIR

def run_fresh_update():
    fresh = os.path.join(BASE_DIR, 'update', 'run_fresh.bat')
    assert os.path.exists(fresh), f"Файл не найден по указанному пути {fresh}"
    
    try:
        subprocess.run(fresh, check=True)
        print("Обновление завершено")
    except subprocess.CalledProcessError as e:
        logger.exception(f"Ошибка при выполнении файла {e}")
        print(f"Error: {e}")
    except Exception as e:
        logger.exception(f"Error: {e}")


def run_stable_update():
    fresh = os.path.join(BASE_DIR, 'update', 'run_stable.bat')
    assert os.path.exists(fresh), f"Файл не найден по указанному пути {fresh}"
    
    try:
        subprocess.run(fresh, check=True)
        print("Обновление завершено")
    except subprocess.CalledProcessError as e:
        logger.exception(f"Ошибка при выполнении файла {e}")
        print(f"Error: {e}")
    except Exception as e:
        logger.exception(f"Error: {e}")

