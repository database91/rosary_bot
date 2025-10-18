import os
from aiogram import Bot
from aiogram.utils.token import TokenValidationError
from dotenv import load_dotenv

def error_checker():
    # Загружаем переменные из .env
    load_dotenv()

    token = os.getenv("TOKEN")

    # Проверяем тип и пустоту
    if not isinstance(token, str) or not token:
        raise TokenValidationError(f"Token is invalid! It must be a non-empty string, got {type(token)}")

    # Проверяем, что токен подходит под формат Telegram
    try:
        Bot(token=token)
    except TokenValidationError as e:
        print("Ошибка токена при создании бота:", e)
        exit(1)

    return token