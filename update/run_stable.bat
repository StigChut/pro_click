@echo off
echo Запуск stable_update.py...
python update\stable_update.py >> update.log 2>&1
if %errorlevel% neq 0 (
    echo Ошибка при выполнении stable_update.py. Код ошибки: %errorlevel%
    exit /b %errorlevel%
)
echo Обновление завершено успешно.
exit /b 0