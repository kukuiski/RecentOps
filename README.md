# RecentOps

## Описание

Набор модулей, предназначенных для работы с номерами карт, счетов, а также для обработки данных и работы с датами. В проекте включены три основных модуля:

- `masks.py`: Модуль, который содержит функции для маскировки номеров карт и счетов.
- `processing.py`: Модуль, который предоставляет функции для фильтрации и сортировки данных.
- `widget.py`: Модуль для работы с маскировкой данных и форматированием дат.

## Установка

Для установки всех зависимостей используйте [Poetry](https://python-poetry.org/):

```bash
poetry install
```

Poetry автоматически создаст и активирует виртуальное окружение. Для доступа к этому окружению, вы можете использовать:
```bash
poetry shell
```

## Использование

### masks.py

Модуль `masks.py` предоставляет следующие функции:

- `get_mask_card_number(card_number: int) -> str`: Принимает на вход номер карты и возвращает его маску.
- `get_mask_account(account_number: int) -> str`: Принимает на вход номер счета и возвращает его маску.

Пример использования:

```python
from recentops.masks import get_mask_card_number, get_mask_account

masked_card = get_mask_card_number(7000792289606361)
masked_account = get_mask_account(73654108430135874305)
print(masked_card)  # Вывод: 7000 79** **** 6361
print(masked_account)  # Вывод: **4305
```

### processing.py

Модуль `processing.py` предоставляет следующие функции:

- `filter_by_state(list_of_dicts: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]`: Функция возвращает новый список словарей, содержащий только те словари, у которых ключ `state` соответствует указанному значению.
- `sort_by_date(list_of_dicts: List[Dict[str, Any]], reverse_order: bool = True) -> List[Dict[str, Any]]`: Функция принимает список словарей и возвращает новый список, отсортированный по дате (`date`). Опциональный ключ задаёт порядок сортировки (по умолчанию — от более ранней до более поздней даты).

Пример использования:

```python
from recentops.processing import filter_by_state, sort_by_date

data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

filtered_data = filter_by_state(data, state="EXECUTED")
sorted_data = sort_by_date(filtered_data)
print(filtered_data)
# Вывод: [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
print(sorted_data)
# Вывод: [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
```

### widget.py

Модуль `widget.py` предоставляет следующие функции:

- `mask_account_card(account_or_card_type_and_number: str) -> str`: Принимает один аргумент — строку, содержащую тип и номер карты или счета. Возвращает строку с замаскированным номером.
- `get_date(date_str: str) -> str`: Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024").

Пример использования:

```python
from recentops.widget import mask_account_card, get_date

masked_data = mask_account_card("Visa Platinum 7000792289606361")
formatted_date = get_date("2024-03-11T02:26:18.671407")
print(masked_data)    # Вывод: Visa Platinum 7000 79** **** 6361
print(formatted_date) # Вывод: 11.03.2024
```
