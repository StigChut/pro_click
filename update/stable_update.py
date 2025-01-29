import subprocess
import os
import sys
import logging

# Настройка логирования
logging.basicConfig(filename='update.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# **Конфигурация**
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # Папка, где лежит ui_update.py
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))  # Путь к корню репозитория
REPO_URL = "https://github.com/StigChut/pro_click.git"   # URL публичного репозитория
BRANCH = "stable"  # Ваша ветка: main, master или другая

# **Функции**
def run_command(command, cwd=None, ignore_errors=False):
    """
    Выполняет shell-команду и возвращает её результат.
    Если ignore_errors=True, ошибки не приводят к завершению скрипта.
    """
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=cwd)
    if result.returncode != 0 and not ignore_errors:
        logger.error(f"Ошибка при выполнении команды: {command}")
        logger.error(f"Ошибка: {result.stderr.strip()}")
        sys.exit(result.returncode)
    return result.stdout.strip()

def init_git_repo():
    """
    Инициализирует репозиторий, если он ещё отсутствует.
    """
    if not os.path.exists(os.path.join(BASE_DIR, ".git")):  # Проверяем, есть ли папка .git в корне
        logger.info("Репозиторий не найден. Инициализация...")
        run_command("git init", cwd=BASE_DIR)  # Инициализация
        run_command(f"git remote add origin {REPO_URL}", cwd=BASE_DIR)  # Добавление удалённого репозитория
        run_command("git fetch origin", cwd=BASE_DIR)  # Скачивание содержимого

        # Проверяем, существует ли ветка BRANCH в удаленном репозитории
        branches = run_command("git branch -r", cwd=BASE_DIR)
        if f"origin/{BRANCH}" in branches:
            # Переключаемся на существующую ветку
            run_command(f"git checkout -b {BRANCH} origin/{BRANCH}", cwd=BASE_DIR)
        else:
            # Создаем новую ветку, если она не существует в удаленном репозитории
            run_command(f"git checkout -b {BRANCH}", cwd=BASE_DIR)
        logger.info("Репозиторий успешно инициализирован.")
    else:
        logger.info("Репозиторий уже инициализирован.")

def set_git_config():
    """
    Устанавливает имя и email пользователя для Git, если они не установлены.
    """
    # Проверяем, установлены ли уже имя и email (игнорируем ошибки, если они не установлены)
    user_name = run_command("git config user.name", cwd=BASE_DIR, ignore_errors=True)
    user_email = run_command("git config user.email", cwd=BASE_DIR, ignore_errors=True)
    
    if not user_name:
        logger.info("Устанавливаю имя пользователя Git...")
        run_command('git config user.name "Auto Updater"', cwd=BASE_DIR)
    if not user_email:
        logger.info("Устанавливаю email пользователя Git...")
        run_command('git config user.email "auto-updater@example.com"', cwd=BASE_DIR)

def check_and_update():
    """
    Проверяет наличие обновлений и выполняет их.
    """
    logger.info("Проверяю обновления...")
    run_command("git fetch origin", cwd=BASE_DIR)
    try:
        current_branch = run_command("git rev-parse --abbrev-ref HEAD", cwd=BASE_DIR)
        logger.info(f"Текущая ветка: {current_branch}")
        run_command(f"git pull origin {current_branch}", cwd=BASE_DIR)
    except SystemExit:
        logger.error("Не удалось определить текущую ветку. Попробуем переключиться на ветку по умолчанию.")
        # Полная очистка рабочего дерева
        run_command("git clean -fd", cwd=BASE_DIR, ignore_errors=True)
        # Сброс всех изменений до последнего коммита
        run_command("git reset --hard", cwd=BASE_DIR, ignore_errors=True)
        # Переключаемся на ветку по умолчанию
        run_command(f"git checkout {BRANCH}", cwd=BASE_DIR)
        # Проверяем обновления
        run_command(f"git pull origin {BRANCH}", cwd=BASE_DIR)

def run_fresh_update():
    fresh = os.path.join(BASE_DIR, 'update', 'run_fresh.bat')
    assert os.path.exists(fresh), f"Файл не найден по указанному пути {fresh}"
    
    try:
        logger.info(f"Запуск батника: {fresh}")
        result = subprocess.run(fresh, check=True, shell=True)
        logger.info("Обновление завершено успешно.")
        print("Обновление завершено")
    except subprocess.CalledProcessError as e:
        logger.exception(f"Ошибка при выполнении файла {e}")
        print(f"Error: {e}")
    except Exception as e:
        logger.exception(f"Error: {e}")

# Инициализируем репозиторий, если его нет
init_git_repo()

# Проверяем, что репозиторий инициализирован
if os.path.exists(os.path.join(BASE_DIR, ".git")):
    # Устанавливаем конфигурацию Git
    set_git_config()
    # Проверяем обновления и обновляем
    check_and_update()
    # Запускаем полное обновление
    run_fresh_update()
else:
    logger.error("Ошибка: репозиторий не инициализирован.")
    print("Ошибка: репозиторий не инициализирован.")
    sys.exit(1)