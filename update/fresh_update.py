import subprocess
import os
import sys

# **Конфигурация**
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # Папка, где лежит update.py
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))  # Путь к корню репозитория
REPO_URL = "https://github.com/StigChut/pro_click.git"   # URL публичного репозитория
BRANCH = "debug"  # Ваша ветка: main, master или другая

# **Функции**
def run_command(command, cwd=None, ignore_errors=False):
    """
    Выполняет shell-команду и возвращает её результат.
    Если ignore_errors=True, ошибки не приводят к завершению скрипта.
    """
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=cwd)
    if result.returncode != 0 and not ignore_errors:
        print(f"Ошибка при выполнении команды: {command}")
        print(f"Ошибка: {result.stderr.strip()}")
        sys.exit(result.returncode)
    return result.stdout.strip()

def init_git_repo():
    """
    Инициализирует репозиторий, если он ещё отсутствует.
    """
    if not os.path.exists(os.path.join(BASE_DIR, ".git")):  # Проверяем, есть ли папка .git в корне
        print("Репозиторий не найден. Инициализация...")
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
        print("Репозиторий успешно инициализирован.")
    else:
        print("Репозиторий уже инициализирован.")

def set_git_config():
    """
    Устанавливает имя и email пользователя для Git, если они не установлены.
    """
    # Проверяем, установлены ли уже имя и email (игнорируем ошибки, если они не установлены)
    user_name = run_command("git config user.name", cwd=BASE_DIR, ignore_errors=True)
    user_email = run_command("git config user.email", cwd=BASE_DIR, ignore_errors=True)
    
    if not user_name:
        print("Устанавливаю имя пользователя Git...")
        run_command('git config user.name "Auto Updater"', cwd=BASE_DIR)
    if not user_email:
        print("Устанавливаю email пользователя Git...")
        run_command('git config user.email "auto-updater@example.com"', cwd=BASE_DIR)

def check_and_update():
    """
    Проверяет наличие обновлений и выполняет их.
    """
    print("Проверяю обновления...")
    run_command("git fetch origin", cwd=BASE_DIR)
    try:
        current_branch = run_command("git rev-parse --abbrev-ref HEAD", cwd=BASE_DIR)
        print(f"Текущая ветка: {current_branch}")
        run_command(f"git pull origin {current_branch}", cwd=BASE_DIR)
    except SystemExit:
        print("Не удалось определить текущую ветку. Попробуем переключиться на ветку по умолчанию.")
        # Полная очистка рабочего дерева
        run_command("git clean -fd", cwd=BASE_DIR, ignore_errors=True)
        # Сброс всех изменений до последнего коммита
        run_command("git reset --hard", cwd=BASE_DIR, ignore_errors=True)
        # Переключаемся на ветку по умолчанию
        run_command(f"git checkout {BRANCH}", cwd=BASE_DIR)
        # Проверяем обновления
        run_command(f"git pull origin {BRANCH}", cwd=BASE_DIR)

# Инициализируем репозиторий, если его нет
init_git_repo()

# Проверяем, что репозиторий инициализирован
if os.path.exists(os.path.join(BASE_DIR, ".git")):
    # Устанавливаем конфигурацию Git
    set_git_config()
    # Проверяем обновления и обновляем
    check_and_update()
else:
    print("Ошибка: репозиторий не инициализирован.")
    sys.exit(1)