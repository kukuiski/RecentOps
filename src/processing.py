import re
from collections import Counter
from typing import Any, Dict, List

import pandas as pd

from src.widget import get_date, mask_account_card


def filter_by_state(list_of_dicts: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    return [d for d in list_of_dicts if d.get("state") == state]


def sort_by_date(list_of_dicts: List[Dict[str, Any]], reverse_order: bool = True) -> List[Dict[str, Any]]:
    """Функция принимает список словарей и возвращает новый список, отсортированный по дате (date)
    Опциональный ключ задаёт порядок сортировки (по умолчанию — убывание)
    """
    return sorted(list_of_dicts, key=lambda x: x.get("date", ""), reverse=reverse_order)


def get_transactions(ops: List, pattern: str) -> List[Dict[str, Any]]:
    """
    Функция принимает список словарей с банковскими операциями и строку поиска,
    и возвращает список словарей с операциями, содержащими данную строку в поле description.
    """

    # Используем регулярное выражение для поиска pattern в поле description (регистр-независимо)
    result = []
    for operation in ops:
        description = operation.get('description', '')
        # Используем re.search() для поиска подстроки по регулярному выражению
        if re.search(pattern, description, flags=re.IGNORECASE):
            result.append(operation)

    # Возвращаем отфильтрованный список словарей
    return result


def count_operations_by_category(ops: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """
    Функция принимает список банковских операций и список категорий, и возвращает
    словарь, где ключи — это названия категорий, а значения — количество операций в каждой категории.
    """
    counter: Counter[str] = Counter()

    # Проходим по каждой категории
    for category in categories:
        # Получаем отфильтрованные транзакции по каждой категории с помощью get_transactions
        transactions = get_transactions(ops, category)
        # Увеличиваем счетчик для данной категории на количество найденных операций
        counter[category] = len(transactions)

    return dict(counter)


def print_operations(ops: pd.DataFrame) -> None:
    """Функция выводит данные об операциях в форматированном виде"""
    total_ops = ops.shape[0]
    if total_ops > 0:
        print(f"Всего банковских операций в выборке: {total_ops}\n")
        for _, row in ops.iterrows():
            date = get_date(str(row["date"]))
            print(f"{date} {row["description"]}")
            from_col = str(row["from"])
            if from_col:
                print(f"{mask_account_card(from_col)} -> ", end="")
            print(f"{mask_account_card(str(row["to"]))}")
            print(f"Сумма: {row["amount"]} {"руб." if row["currency_code"] == "RUB" else row["currency_code"]}")
            print()
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    return
