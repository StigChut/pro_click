@echo off

REM Проверяем, существует ли виртуальное окружение
if not exist ".venv\Scripts\activate" (
    REM Установка политики выполнения для текущего пользователя (делается только один раз)
    powershell -Command "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force"

    REM Создание виртуального окружения, если не существует
    python -m venv .venv

    REM Активируем виртуальное окружение
    call .venv\Scripts\activate

    REM Устанавливаем зависимости из requirements.txt
    pip install -r requirements.txt
) else (
    REM Активируем существующее виртуальное окружение
    call .venv\Scripts\activate
)

REM Запускаем Python-скрипт
python main.py

REM Пауза, чтобы окно не закрылось автоматически
pause
