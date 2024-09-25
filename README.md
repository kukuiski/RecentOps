# RecentOps

## Описание

Набор модулей, предназначенных для работы с номерами карт, счетов, а также для обработки данных и работы с датами. В проекте включены три основных модуля:

- `masks.py`: Модуль, который содержит функции для маскировки номеров карт и счетов.
- `processing.py`: Модуль, который предоставляет функции для фильтрации и сортировки данных.
- `widget.py`: Модуль для работы с маскировкой данных и форматированием дат.
- `generators.py`: Модуль с генераторами для обработки данных [описание ниже](#generatorspy). 

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
from src.masks import get_mask_card_number, get_mask_account

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
from src.processing import filter_by_state, sort_by_date

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
from src.widget import mask_account_card, get_date

masked_data = mask_account_card("Visa Platinum 7000792289606361")
formatted_date = get_date("2024-03-11T02:26:18.671407")
print(masked_data)    # Вывод: Visa Platinum 7000 79** **** 6361
print(formatted_date) # Вывод: 11.03.2024
```

### generators.py

Модуль `generators.py` предоставляет следующие функции:

- `filter_by_currency(transactions_list: List[Dict[str, Any]], currency_code: str) -> Generator`: Принимает на вход список словарей, представляющих транзакции и возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной.
- `transaction_descriptions(transactions_list: List[Dict[str, Any]]) -> Generator`: Принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
- `card_number_generator(start: int, stop: int) -> Generator`: Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.

Примеры использования:

```python
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160"
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229"
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "67314.70",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657"
    }
]


usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

"""
Вывод:
>>> {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
"""

descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

"""
Вывод:
>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
"""

for card_number in card_number_generator(1, 5):
    print(card_number)

"""
Вывод:
>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
"""
```

### utils.py

Предоставляет функции для работы с финансовыми транзакциями, включая загрузку транзакций из JSON-файла и конвертацию сумм транзакций в рубли (RUB).

- `get_transactions_from_json(path_to_json: str) -> Any`: Функция принимает путь до JSON-файла с данными о транзакциях и возвращает список транзакций в виде словарей. Если файл пустой, содержит невалидные данные или не найден, функция возвращает пустой список.
- `amount_of_transaction(transaction: Dict[str, Any]) -> float`: Функция принимает на вход транзакцию и возвращает сумму этой транзакции в рублях. Если сумма указана в другой валюте, она будет конвертирована в рубли с помощью внешнего API.

### external_api.py

Модуль предоставляет функции для работы с внекшними API

- `currency_convert(c_from: str, c_to: str, amount: float) -> Any`: Функция конвертирует из одной валюты в другую по текущему курсу с помощью Exchange Rates Data API

### decorators.py

Модуль `decorators.py` содержит декораторы:

- `def log(filename: str = '') -> Callable[[F], F]`: Декоратор для логирования действия оборачиваемой функции. Записывает строку в случае успешного или неуспешного выполнения в файл с указанным именем в качестве аргумента. Если имя файла отсутствует, логи выводятся в консоль. 

Примеры использования:

```python
from src.decorators import log

log_file = "log.txt"

@log(filename=str(log_file))
def test_func(x, y):
    return x + y
```

## Тестирование

Для тестирования модулей используйте встроенные тесты на базе `pytest`.
1. Убедитесь, что все зависимости установлены, и виртуальное окружение активировано:
```bash
poetry install
poetry shell
```

2. Тесты запускаются командой:
```bash
pytest
```

Тесты покроют все основные функции модулей:
- Проверка корректной маскировки номеров карт и счетов (`masks.py`).
- Тестирование фильтрации и сортировки данных по состоянию и дате (`processing.py`).
- Тестирование маскировки данных и форматирования дат (`widget.py`).

