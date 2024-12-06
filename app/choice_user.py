import app.tools
from push_service.messge_handler import user_login

def app_choise_user():
    """
    Shift+A
    Вызывается и записывает ник юзера в телеграмм для того чтобы пушнуть его в чате
    Принимает на вход: https://t.me/... или чистый usermane
    """
    app.tools.safe_execute(
        user_login,
        "Username - ДА",
        "Username - НЕТ"
    )