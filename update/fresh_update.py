import subprocess
import os
import sys

# **Конфигурация**
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # Папка, где лежит update.py
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))  # Путь к корню репозитория
REPO_URL = "https://github.com/StigChut/pro_click.git"   # URL публичного репозитория
BRANCH = "debug"  # Ваша ветка: main, master или другая

# **Функции**


def run_command(command, cwd=None):
    """
    Выполняет shell-команду и возвращает её результат. Если ошибка — выводит и завершает работу скрипта.
    """
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=cwd)
    if result.returncode != 0:
        print(f"Ошибка при выполнении команды: {command}")
        print(f"Ошибка: {result.stderr.strip()}")
        sys.exit(result.returncode)
    return result.stdout.strip()


def init_git_repo():
    """
    Инициализирует репозиторий, если он ещё отсутствует. В случае пустого репозитория — производит первый clone.
    """
    if not os.path.exists(os.path.join(BASE_DIR, ".git")):  # Проверяем, есть ли папка .git в корне
        print("Репозиторий не найден. Инициализация...")
        run_command("git init", cwd=BASE_DIR)  # Инициализация
        run_command(f"git remote add origin {REPO_URL}", cwd=BASE_DIR)  # Добавление удалённого репозитория
        run_command("git fetch origin", cwd=BASE_DIR)  # Скачивание содержимого
        try:
            # Попробуем переключить на указанную ветку
            run_command(f"git checkout -b {BRANCH} origin/{BRANCH}", cwd=BASE_DIR)
        except SystemExit:
            # Если ветка не существует (например, пустой репозиторий)
            print(f"Ветка {BRANCH} не найдена. Клонирую весь репозиторий...")
            run_command(f"git pull origin {BRANCH}", cwd=BASE_DIR)  # Клонируем содержимое ветки
        print("Репозиторий успешно инициализирован.")


def ensure_remote_repo():
    """
    Проверяет наличие удалённого репозитория. Если отсутствует — добавляет.
    """
    remotes = run_command("git remote -v", cwd=BASE_DIR)
    if "origin" not in remotes:
        print("Добавление удалённого репозитория...")
        run_command(f"git remote add origin {REPO_URL}", cwd=BASE_DIR)


def get_commit_hash(ref):
    """
    Возвращает hash коммита для указанной ссылки (HEAD, ветка, и т.д.).
    Если ссылка отсутствует (ошибка), возвращает None.
    """
    try:
        return run_command(f"git rev-parse {ref}", cwd=BASE_DIR)
    except SystemExit:
        print(f"Ссылка '{ref}' не найдена.")
        return None


def check_and_update():
    """
    Проверяет изменения в удалённом репозитории. Если найдены обновления, применяет их.
    """
    print("Проверяю репозиторий на изменения...")
    ensure_remote_repo()
    run_command("git fetch origin", cwd=BASE_DIR)  # Получаем обновления

    # Получаем текущий и удалённый коммит
    local_commit = get_commit_hash("HEAD")
    remote_commit = get_commit_hash(f"origin/{BRANCH}")

    if not local_commit:
        print("Локальный репозиторий пуст. Копирую содержимое...")

        # Удаляем конфликтующие файлы (если есть)
        print("Удаляю конфликтующие файлы...")
        run_command("git clean -f -d", cwd=BASE_DIR)  # Чистим директорию

        # Создаём ветку и переключаемся
        run_command(f"git checkout -b {BRANCH} origin/{BRANCH}", cwd=BASE_DIR)
        return

    if local_commit != remote_commit:  # Если есть различия
        print("Обнаружены изменения, выполняется сброс локальных изменений...")
        run_command("git reset --hard HEAD", cwd=BASE_DIR)  # Удаляем все локальные изменения

        # Удаляем конфликтующие файлы
        run_command("git clean -f -d", cwd=BASE_DIR)

        print("Локальные изменения сброшены.")
        print("Выполняется обновление...")
        run_command(f"git pull origin {BRANCH}", cwd=BASE_DIR)
        print("Обновление завершено!")
    else:
        print("Обновлений нет. Программа актуальна.")


def set_git_config():
    """
    Устанавливает имя и email пользователя для Git, если они не установлены.
    """
    # Проверяем, установлены ли уже имя и email
    user_name = run_command("git config user.name", cwd=BASE_DIR)
    user_email = run_command("git config user.email", cwd=BASE_DIR)
    
    if not user_name:
        run_command('git config user.name "Auto Updater"', cwd=BASE_DIR)
    if not user_email:
        run_command('git config user.email "auto-updater@example.com"', cwd=BASE_DIR)

# Инициализируем репозиторий, если его нет
init_git_repo()

# Устанавливаем конфигурацию Git
set_git_config()

# Проверяем обновления и обновляем
check_and_update()