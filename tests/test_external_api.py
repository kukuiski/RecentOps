import os
from unittest.mock import patch

from src.external_api import currency_convert


# Тест с мокированием вызова API
@patch("requests.request")
def test_currency_convert(mock_request):
    """Тестируем функцию currency_convert с мокированием запроса к API"""

    # Настройка мока для ответа API
    mock_response = {
        "date": "2024-09-23",
        "info": {"rate": 103.18754, "timestamp": 1727117776},
        "query": {"amount": 12, "from": "EUR", "to": "RUB"},
        "result": 1238.25048,
        "success": "true",
    }

    # Настраиваем мок на возврат нужных данных
    mock_request.return_value.status_code = 200
    mock_request.return_value.json.return_value = mock_response

    # Вызов функции с тестовыми данными
    result = currency_convert("EUR", "RUB", 12)

    # Проверяем, что результат конверсии корректен
    assert result == 1238.25048

    # Проверяем, что запрос был сделан с правильными параметрами
    mock_request.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=12",
        headers={"apikey": os.getenv("EXCHANGE_API_KEY")},
        data={},
    )
