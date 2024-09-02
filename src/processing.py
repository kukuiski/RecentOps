from typing import List, Dict, Any


def filter_by_state(list_of_dicts: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    pass


def sort_by_date(list_of_dicts: List[Dict[str, Any]], reverse_order: bool = "True") -> List[Dict[str, Any]]:
    """Функция принимает список словарей и возвращает новый список, отсортированный по дате (date)
    Опциональный ключ задаёт порядок сортировки (по умолчению — убывание)
    """
    pass
