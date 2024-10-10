from typing import Dict, List


def ask_user_format() -> str:
    """Спрашиваем у пользователя, данные из какого файла загружать"""
    menu: Dict = {"1": "Получить информацию о транзакциях из JSON-файла",
                  "2": "Получить информацию о транзакциях из CSV-файла",
                  "3": "Получить информацию о транзакциях из XLSX-файла"}
    answer = ""

    while answer not in menu.keys():
        print("Выберите необходимый пункт меню:")
        for key, message in menu.items():
            print(f"{key}. {message}")
        answer = input("Ваш выбор: ").strip()

    return answer


def ask_user_state(states: List[str]) -> str:
    """Выбор из списка строк"""
    answer = ""
    while answer.upper() not in states:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы:", ", ".join(states))
        answer = input("Ваш выбор: ").strip()
        if answer.upper() not in states:
            print(f"Статус операции \"{answer}\" недоступен.")
    return answer.upper()


def ask_two_options(question: str = "Введите ответ: ", opt1: str = "Да", opt2: str = "Нет") -> bool:
    """Выбор из двух опций. Если выбрана первая, возвращает True, если вторая — False"""
    answer = opt1 + opt2 + "1"
    options = {opt1.casefold(): True, opt2.casefold(): False}

    while answer not in options:
        answer = input(f"{question} {opt1}/{opt2}: ").strip().casefold()
        print()

    return options[answer]


def ask_word(question: str = "Введите слово: ") -> str:
    """Запрашиваем слово"""
    while True:
        word = input(question).strip()  # Убираем пробелы в начале и конце строки
        if word:  # Если строка не пустая, возвращаем результат
            return word
        print("Введите непустое слово.")
