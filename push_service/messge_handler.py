import telebot

from push_service.config import tg_token
from push_service.config import chat_id, alert_slot
from func.active_window import save_file
from my_logger import logger


# Создание экземпляра бота
def init_bot(token=None):
    if token is None:
        raise ValueError("Токен для бота не установлен")
    return telebot.TeleBot(token)

bot = init_bot(tg_token)

# Получаем ник пользователя в ТГ, для того чтобы призывать его  в чате
def user_login():
    try:
        # Окно приветствия \ Пользовательский ввод
        print("Введи свой username в ТГ.(Пример: https://t.me/yesimfine_thanks)")
        user_input = input("Enter username:").strip()
        logger.debug(f"Пользователь ввел: {user_input}")

        # Преобразование 
        if "https://t.me/" in user_input:
            # Находим всю часть после "https://t.me/"
            username = user_input.split("https://t.me/")[-1].strip()
        else:
            username = user_input.strip()

        user_data = {'username': username}
        print(f"username: {username} сохранен")
        save_file(user_data)
        logger.debug(f"Сохранили имя пользователя в ТГ")
    except Exception as e:
        logger.debug(f"Ошибка сохранения данных пользователя")


# Принимаем на вход текст, отправляем его в чат
def push_message(username, message_text, shop_sklad):
    try:
        # Формируес сообщение для пользователя
        text = f"@{username}, {message_text} {shop_sklad}"
        logger.debug(f"Сообщение пользователю сформировано: {text}")

        # Отправляем сообщение пользователю
        bot.send_message(
            chat_id=chat_id,
            reply_to_message_id=alert_slot,
            text=text
        )
        logger.debug("Сообщение в чат отправлено")
        return True
    except Exception as e:
        logger.debug(f"Ошибка отправки сообщения в чат: {e}")
        return False