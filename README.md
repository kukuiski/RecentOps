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


### main.py

Модуль `main.py` реализует основной рабочий процесс программы, взаимодействуя с пользователем через меню и работая с данными транзакций. 

#### Основной рабочий процесс

1. **Выбор источника данных:** Пользователь может выбрать, из какого файла (JSON, CSV или XLSX) загружать данные о транзакциях.
2. **Фильтрация по статусу:** Программа предлагает пользователю выбрать статус транзакции для фильтрации (например, `EXECUTED`, `CANCELED`).
3. **Сортировка данных по дате:** Пользователь может выбрать, нужно ли отсортировать транзакции по дате в порядке возрастания или убывания.
4. **Фильтрация по валюте:** Пользователь может выбрать, следует ли выводить только рублевые транзакции.
5. **Фильтрация по ключевому слову в описании транзакций:** Пользователь может выбрать фильтрацию по определенному слову, введенному в поле `description`.
6. **Вывод данных:** Программа выводит отфильтрованный и отсортированный список транзакций.

Пример использования:

```bash
$ python main.py
```
```text
Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
Ваш выбор: 1

Для обработки выбран JSON-файл.

Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING
Ваш выбор: EXECUTED

Операции отфильтрованы по статусу "EXECUTED"

Отсортировать операции по дате? Да/Нет: Да
Отсортировать по возрастанию или по убыванию? По возрастанию/По убыванию: По возрастанию

Выводить только рублевые транзакции? Да/Нет: Да

Отфильтровать список транзакций по определенному слову в описании? Да/Нет: Нет

Распечатываю итоговый список транзакций...
```

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
- `get_transactions(ops: List[Dict[str, Any]], pattern: str) -> List[Dict[str, Any]]`: Функция принимает список словарей с банковскими операциями и строку поиска, и возвращает список операций, содержащих данную строку в поле description.
- `count_operations_by_category(ops: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]`: Функция принимает список банковских операций и список категорий, возвращая словарь, где ключи — это названия категорий, а значения — количество операций в каждой категории.
- `print_operations(ops: pd.DataFrame) -> None`: Функция выводит отформатированные данные о банковских операциях, полученные из DataFrame, включая дату, транзакцию и сумму.

- Пример использования:

```python
from src.processing import filter_by_state, sort_by_date, get_transactions, count_operations_by_category

# Фильтрация по состоянию
data = [{'id': 1, 'state': 'EXECUTED', 'date': '2024-03-11', 'description': 'Открытие вклада'},
        {'id': 2, 'state': 'CANCELED', 'date': '2024-03-12', 'description': 'Перевод организации'}]
executed_operations = filter_by_state(data)

# Сортировка по дате
sorted_operations = sort_by_date(executed_operations)

# Поиск по ключевым словам
found_operations = get_transactions(data, "услуг")

# Подсчет операций по категориям
categories = ['Оплата', 'Покупка']
operations_count = count_operations_by_category(data, categories)
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

- `get_transactions_from_json(path_to_json: str) -> Any`: Функция принимает путь до JSON-файла с данными о транзакциях и возвращает список транзакций в виде словарей. Если файл пустой, содержит невалидные данные или не найден, функция возвращает пустой список. Логирование успешного чтения или ошибок.
- `amount_of_transaction(transaction: Dict[str, Any]) -> float`: Функция принимает на вход транзакцию и возвращает сумму этой транзакции в рублях. Если сумма указана в другой валюте, она будет конвертирована в рубли с помощью функции `currency_convert` из модуля `external_api`. Логирование успешных операций или ошибок при конвертации и чтении данных. 

Пример использования:

```python
from src.utils import get_transactions_from_json, amount_of_transaction

transactions = get_transactions_from_json("data/transactions.json")
if transactions:
    for transaction in transactions:
        try:
            amount_in_rub = amount_of_transaction(transaction)
            print(f"Сумма транзакции в рублях: {amount_in_rub}")
        except Exception as e:
            print(f"Ошибка обработки транзакции: {e}")
```

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

### data_loaders.py

Модуль `data_loaders.py` предоставляет функции для загрузки данных из CSV, Excel и JSON-файлов:

- `def read_data_from_csv(file_path: str) -> Any`: Читает данные из CSV-файла и возвращает их в виде списка словарей. Логирует успешное чтение или ошибки.
- `read_data_from_excel(file_path: str) -> Any`: Читает данные из Excel-файла и возвращает их в виде списка словарей. Логирует успешное чтение или ошибки.
- `read_normalized_json(file_path: str) -> Any` : Читает и нормализует данные из JSON-файла, приводит индексы в соответствие с CSV и возвращает pandas DataFrame.

Пример использования:
```python
from src.data_loaders import read_data_from_csv, read_data_from_excel, read_normalized_json

csv_data = read_data_from_csv('data/transactions.csv')
excel_data = read_data_from_excel('data/transactions.xlsx')
json_data = read_normalized_json('data/transactions.json')

print(csv_data)
print(excel_data)
print(json_data)
```

### menu.py

Модуль `menu.py` предоставляет функции для взаимодействия с пользователем:

- `ask_user_format() -> str`: Спрашивает у пользователя, данные из какого файла загружать (JSON, CSV или XLSX), и возвращает выбранный вариант.
- `ask_user_state(states: List[str]) -> str`: Спрашивает у пользователя, какой статус фильтрации применить, и возвращает выбранный статус из предоставленного списка.
- `ask_two_options(question, opt1, opt2) -> bool`: Спрашивает у пользователя выбрать из двух вариантов (например, Да или Нет) и возвращает `True` для первого варианта и `False` для второго.
- `ask_word(question) -> str`: Спрашивает у пользователя ввести слово, возвращает результат только если строка не пустая.

Пример использования:

```python
from src.menu import ask_user_format, ask_user_state, ask_two_options, ask_word

# Выбор формата файла
file_format = ask_user_format()

# Выбор статуса из списка
statuses = ["EXECUTED", "CANCELED", "PENDING"]
selected_status = ask_user_state(statuses)

# Выбор между двумя опциями
is_continue = ask_two_options("Продолжить выполнение?", "Да", "Нет")

# Ввод слова
user_word = ask_word("Введите ключевое слово для поиска: ")
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
- Проверка корректной маскировки номеров карт и счетов `masks.py`.
- Тестирование фильтрации и сортировки данных по состоянию и дате `processing.py`.
- Тестирование маскировки данных и форматирования дат `widget.py`.
- Тестирование загрузки данных `data_loaders.py`
- Тестирование взаимодействия с пользователем `menu.py`
- Тестирование обработки данных `utils.py`
- Тестирование основного модуля `main.py`

## Логгирование

Логгирование добавлено в следующие модули:

1. **utils.py**: Логирование ошибок связанных с чтением JSON
2. **masks.py**: Логгирование функций маскирования номеров счетов и карт.
3. **data_loaders.py**: Логгирование функций считывания данных из CSV, Excel и JSON-файлов 

Логи обновляются при каждом запуске и хранятся в файлах:
- `logs/utils_logfile.log`
- `logs/masks_logfile.log`
- `logs/data_loaders_logfile.log`
