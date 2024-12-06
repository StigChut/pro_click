import os

from dotenv import load_dotenv
load_dotenv()

# Токен бота
tg_token = os.getenv('tg_token')

# ID Чата
chat_id = os.getenv('id_chat')

# ID Тем в группе
alert_slot = os.getenv('id_theme')


# Стандартные пуши пользователя
INFO_MESSAGE = "Запущен поиск слотов" # Инофрмационное сообщение, можно отключить потом
GREEN_MESSAGE = "Слот забронирован для:" # Текст для сообщения в чат об успешном бронировании
STOP_MESSAGE = "Скрипт остановил работу для:" # Текст для сообщения в чат при остановке скрипта 
ERROR_MESSAGE = "Скрипт остановил из-за ошибки работу для:" # Текст для сообщения в чат при остановке из ошибки 

