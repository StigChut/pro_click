@echo off
echo Запуск stable_update.py...
python update\stable_update.py
if %errorlevel% neq 0 (
    echo Ошибка при выполнении stable_update.py. Код ошибки: %errorlevel%
    pause
    exit /b %errorlevel%
)
echo Обновление завершено успешно.
exit /b 0