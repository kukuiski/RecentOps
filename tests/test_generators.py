import pytest
from typing import List, Dict, Any
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


# Тестирование функции filter_by_currency

@pytest.mark.parametrize("currency_code, expected_ids", [
    ("USD", [939719570, 142264268, 895315941]),  # Должен вернуть транзакции с USD
    ("RUB", [873106923, 594226727]),  # Должен вернуть транзакции с Рублями
    ("EUR", []),  # Транзакций с Евро нет, ожидаем пустой результат
])
def test_filter_by_currency(transactions, currency_code, expected_ids):
    result = list(filter_by_currency(transactions, currency_code))
    result_ids = [transaction["id"] for transaction in result]
    assert result_ids == expected_ids


def test_filter_by_currency_empty_list():
    result = list(filter_by_currency([], "USD"))
    assert result == []  # Пустой список на входе, пустой результат


def test_filter_by_currency_no_match(transactions):
    result = list(filter_by_currency(transactions, "EUR"))
    assert result == []  # В списке нет транзакций с валютой EUR


# Тестирование функции transaction_descriptions

@pytest.mark.parametrize("expected_descriptions", [
    (["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет", "Перевод с карты на карту",
      "Перевод организации"]),
])
def test_transaction_descriptions(transactions, expected_descriptions):
    result = list(transaction_descriptions(transactions))
    assert result == expected_descriptions


def test_transaction_descriptions_empty_list():
    result = list(transaction_descriptions([]))
    assert result == []  # Пустой список на входе, ожидаем пустой результат


# Тестирование генератора card_number_generator

@pytest.mark.parametrize("start, stop, expected_cards", [
    (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
    (9999_9999_9999_9998, 9999_9999_9999_9999, ["9999 9999 9999 9998", "9999 9999 9999 9999"]),
])
def test_card_number_generator(start, stop, expected_cards):
    result = list(card_number_generator(start, stop))
    assert result == expected_cards


def test_card_number_generator_large_range():
    start = 1
    stop = 5
    expected_cards = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005"
    ]
    result = list(card_number_generator(start, stop))
    assert result == expected_cards


def test_card_number_generator_empty_range():
    result = list(card_number_generator(5, 4))
    assert result == []  # Пустой диапазон должен возвращать пустой результат
