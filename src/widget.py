from src import masks


def mask_account_card(account_or_card_type_and_number: str) -> str:
    """
    Принимает один аргумент — строку, содержащую тип и номер карты или счета.
    Возвращает строку с замаскированным номером.
    """

    result_string: str

    # Находим первое слово в строке и если оно 'Счет', то обрабатываем как счёт
    list_of_strings = account_or_card_type_and_number.split()
    if list_of_strings[0] == "Счет":
        result_string = "Счет " + masks.get_mask_account(int(list_of_strings[-1]))
    else:
        result_string = " ".join(list_of_strings[:-1]) + " " + masks.get_mask_card_number(int(list_of_strings[-1]))

    return result_string


def get_date(date_str: str) -> str:
    """
    Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")
    """

    year = date_str[0:4]
    month = date_str[5:7]
    day = date_str[8:10]

    return f"{day}.{month}.{year}"
