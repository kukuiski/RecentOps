import json
from unittest.mock import mock_open, patch

from src.utils import amount_of_transaction, get_transactions_from_json

# Словарь, который нужно добавить
transaction = [
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }
]

# Преобразуем словарь в JSON строку
json_data = json.dumps(transaction)


# Тест для проверки чтения из файла
@patch("builtins.open")
def test_open_operations_json(mock_open_file):
    """Тестирование корректного открытия operations.json"""
    path = "../../data/operations.json"  # Здесь путь может быть любым, т.к. open подменен.
    mock_open_file.return_value = mock_open(read_data=json_data).return_value

    # Вызов функции для чтения файла
    transactions = get_transactions_from_json(path)

    # Проверка, что возвращается список с правильными транзакциями
    assert transactions == transaction


@patch("src.utils.currency_convert")
def test_amount_of_transaction(mock_currency_convert):
    mock_currency_convert.return_value = 7500.0
    amount_in_rub = amount_of_transaction(transaction[0])
    assert amount_in_rub == 7500.0
    mock_currency_convert.assert_called_once_with("USD", "RUB", 8221.37)
