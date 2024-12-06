

import app.tools
from func.active_window import active_window

def app_choise_window():
    """
    Shift+Q
    Вызывается первый раз для записи и сохранения активного окна браузера
    """
    app.tools.safe_execute(
        active_window,
        "Выбор окна - ДА",
        "Выбор окна - НЕТ"
    )