from typing import Any, Dict, Generator, List


def filter_by_currency(transactions_list: List[Dict[str, Any]], currency_code: str) -> Generator:
    """Принимает на вход список словарей, представляющих транзакции и возвращает
    итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
    """
    for transaction in transactions_list:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction


def transaction_descriptions(transactions_list: List[Dict[str, Any]]) -> Generator:
    """Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions_list:
        yield transaction.get("description")


def card_number_generator(start: int, stop: int) -> Generator:
    """Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999
    """
    if 9999_9999_9999_9999 >= stop >= start >= 1:
        for number in range(start, stop + 1):
            number_string = ("0" * 15 + str(number))[-16:]
            yield f"{number_string[:4]} {number_string[4:8]} {number_string[8:12]} {number_string[12:16]}"
