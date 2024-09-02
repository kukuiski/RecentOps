from typing import List, Dict, Any


def filter_by_state(list_of_dicts: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    return [d for d in list_of_dicts if d.get('state') == state]


def sort_by_date(list_of_dicts: List[Dict[str, Any]], reverse_order: bool = True) -> List[Dict[str, Any]]:
    """Функция принимает список словарей и возвращает новый список, отсортированный по дате (date)
    Опциональный ключ задаёт порядок сортировки (по умолчанию — убывание)
    """
    return sorted(list_of_dicts, key=lambda x: x.get('date'), reverse=reverse_order)
