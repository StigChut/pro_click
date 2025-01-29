@echo off
echo Запуск fresh_update.py...
python update\fresh_update.py >> update.log 2>&1
if %errorlevel% neq 0 (
    echo Ошибка при выполнении fresh_update.py. Код ошибки: %errorlevel%
    exit /b %errorlevel%
)
echo Обновление завершено успешно.
exit /b 0