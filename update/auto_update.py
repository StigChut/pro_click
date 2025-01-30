# update/fresh_update.py

import subprocess
import os
import sys

# **Конфигурация**
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
REPO_URL = "https://github.com/StigChut/pro_click.git"

def run_command(command, cwd=None, ignore_errors=False):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=cwd)
    if result.returncode != 0 and not ignore_errors:
        print(f"Ошибка при выполнении команды: {command}")
        print(f"Ошибка: {result.stderr.strip()}")
        sys.exit(result.returncode)
    return result.stdout.strip()

def init_git_repo(branch):
    if not os.path.exists(os.path.join(BASE_DIR, ".git")):
        print("Репозиторий не найден. Инициализация...")
        run_command("git init", cwd=BASE_DIR)
        run_command(f"git remote add origin {REPO_URL}", cwd=BASE_DIR)
        run_command("git fetch origin", cwd=BASE_DIR)

        branches = run_command("git branch -r", cwd=BASE_DIR)
        if f"origin/{branch}" in branches:
            run_command(f"git checkout -b {branch} origin/{branch}", cwd=BASE_DIR)
        else:
            run_command(f"git checkout -b {branch}", cwd=BASE_DIR)
        print("Репозиторий успешно инициализирован.")
    else:
        print("Репозиторий уже инициализирован.")

def set_git_config():
    user_name = run_command("git config user.name", cwd=BASE_DIR, ignore_errors=True)
    user_email = run_command("git config user.email", cwd=BASE_DIR, ignore_errors=True)
    
    if not user_name:
        print("Устанавливаю имя пользователя Git...")
        run_command('git config user.name "Auto Updater"', cwd=BASE_DIR)
    if not user_email:
        print("Устанавливаю email пользователя Git...")
        run_command('git config user.email "auto-updater@example.com"', cwd=BASE_DIR)

def check_updates(branch):
    print(f"Проверяю обновления для ветки {branch}...")
    run_command("git reset --hard", cwd=BASE_DIR, ignore_errors=True)
    run_command("git clean -fd", cwd=BASE_DIR, ignore_errors=True)
    run_command(f"git checkout {branch}", cwd=BASE_DIR)

    try:
        current_branch = run_command("git rev-parse --abbrev-ref HEAD", cwd=BASE_DIR)
        print(f"Текущая ветка: {current_branch}")
        run_command("git fetch origin", cwd=BASE_DIR)
        run_command(f"git pull origin {branch}", cwd=BASE_DIR)
    except SystemExit:
        print("Не удалось определить текущую ветку. Попробуем переключиться на ветку по умолчанию.")
        run_command("git clean -fd", cwd=BASE_DIR, ignore_errors=True)
        run_command("git reset --hard", cwd=BASE_DIR, ignore_errors=True)
        run_command(f"git checkout {branch}", cwd=BASE_DIR)
        run_command(f"git pull origin {branch}", cwd=BASE_DIR)

def perform_stable_update():
    init_git_repo("stable")
    if os.path.exists(os.path.join(BASE_DIR, ".git")):
        current_branch = run_command("git rev-parse --abbrev-ref HEAD", cwd=BASE_DIR)
        print(f"Текущая ветка: {current_branch}")
        set_git_config()
        check_updates("stable")
    else:
        print("Ошибка: репозиторий не инициализирован.")
        sys.exit(1)

def perform_fresh_update():
    init_git_repo("debug")
    if os.path.exists(os.path.join(BASE_DIR, ".git")):
        current_branch = run_command("git rev-parse --abbrev-ref HEAD", cwd=BASE_DIR)
        print(f"Текущая ветка: {current_branch}")
        set_git_config()
        check_updates("debug")
    else:
        print("Ошибка: репозиторий не инициализирован.")
        sys.exit(1)