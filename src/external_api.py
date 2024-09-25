import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()


def currency_convert(c_from: str, c_to: str, amount: float) -> Any:
    """Функция конвертирует из одной валюты в другую по текущему курсу с помощью Exchange Rates Data API"""
    api_key = os.getenv("EXCHANGE_API_KEY")

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={c_to}&from={c_from}&amount={amount}"

    payload: Dict[str, Any] = {}
    headers = {
        "apikey": api_key
    }

    # Выполнение запроса
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code != 200:
        raise Exception(f"API запрос не успешен со статусом {response.status_code}")

    # Преобразование в JSON и проверка
    data = response.json()
    if not data.get("success", False):
        raise Exception("API запрос не успешен.")

    # Извлекаем результат конверсии
    result = data.get("result", None)
    if result is None:
        raise Exception("Курс обмена в RUB не найден")

    # Конвертация
    return result
