@echo off

REM Проверяем, существует ли виртуальное окружение
if not exist ".venv\Scripts\activate" (
    REM Установка политики выполнения для текущего пользователя
    REM (делается только один раз)
    powershell -Command "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force"

    REM Создание виртуального окружения, если не существует
    python -m venv .venv

    REM Активируем виртуальное окружение
    call .venv\Scripts\activate

    REM Устанавливаем зависимости из requirements.txt
    pip install -r requirements.txt

    REM Цикл для запуска main.py 2 раза
    for /l %%x in (1, 1, 2) do (
        echo Запуск main.py, итерация %%x...
        python main.py
        echo --------------------------------------

        REM Если это была вторая итерация, выходим из скрипта
        if %%x==2 exit
    )
) else (
    REM Активируем существующее виртуальное окружение
    call .venv\Scripts\activate
)

REM Запуск main.py (если окружение уже существует)
python main.py

REM Пауза, чтобы окно не закрылось автоматически (для второго и последующих запусков)
pause
