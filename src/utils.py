import json
from typing import Any, Dict, Optional

from src.external_api import currency_convert


def get_transactions_from_json(path_to_json: str) -> Any:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""
    try:
        with open(path_to_json, 'r') as json_file:
            result = json.load(json_file)
            if not isinstance(result, list):
                result = []
    except (FileNotFoundError, json.JSONDecodeError, TypeError, ValueError):
        result = []
    return result


def amount_of_transaction(transaction: Dict[str, Any]) -> float:
    """Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""
    amount_str: Optional[str] = transaction.get("operationAmount", {}).get("amount", None)
    if amount_str is None:
        raise Exception("Сумма не найдена")

    amount = float(amount_str)

    currency: Optional[str] = transaction.get("operationAmount", {}).get("currency", {}).get("code", None)
    if currency is None:
        raise Exception("Валюта не указана")

    if currency != "RUB":
        amount = currency_convert(currency, "RUB", amount)

    return amount
